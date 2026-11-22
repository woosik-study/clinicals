"""Compute PPR (Participation to Prevalence Ratio) from trials_clean.csv and prevalence.csv.

PPR = a group's share of trial participants / that group's share of patients.

Rules (decided by the team, see BACKLOG.md section 5):
  - Trials: only us_only trials (all sites in the US).
  - Race: only trials using standard NIH/OMB race categories. "Unknown or Not Reported"
    is left out of the denominator.
  - Ethnicity: only trials that reported NIH/OMB ethnicity. Unknown ethnicity is left out.
  - Prostate cancer: trials also listed under breast cancer are left out.
  - Groups are not labeled. The site shows each value next to a reference line at 1.0.

Patient data comes from prevalence.csv. A row is used only when all of these hold:
  - It has a case_count. PPR needs each group's share of ALL patients, so rows that
    only give a rate inside one group (prevalence_pct, incidence_per_100000) are not used.
  - Its status is not in NEVER_USE.
  - Its race_ethnicity label is one of the labels in GROUPS or ETHNICITY below.
  - The condition has an "All" row with a case_count for the same measure and years.
Counts for female and male rows are added together.

For the two cancers, each trial group is compared with the closest SEER group:
  trial group                        label in prevalence.csv            SEER group
  White                              White (includes Hispanic)          White (includes Hispanic)
  Black or African American          Black (includes Hispanic)          Black (includes Hispanic)
  Asian + Native Hawaiian or
    Other Pacific Islander           Asian                              Non-Hispanic Asian / Pacific Islander
  American Indian or Alaska Native   American Indian / Alaska Native    Non-Hispanic American Indian / Alaska Native
  Hispanic or Latino (ethnicity)     Hispanic                           Hispanic (any race)
  More than one race                 none                               none, so trial share only
The plain "White" and "Black" rows in prevalence.csv are not used, because trial counts
include Hispanic participants and those rows are not confirmed to include them.

A group or condition without usable patient data is "pending": it gets a trial share
but no PPR.

Sensitivity check: for each group, the trial that contributed the most participants to
that group is found and left out (from both the group count and the denominator), and
the trial share and PPR are computed again. Readers can compare the two values to see
how much one trial drives the result.

Type 2 diabetes uses CDC's estimated counts of adults with diagnosed diabetes in 2021
(prevalence.csv condition "diabetes", measure "diagnosed_adults"). The CDC report does not
separate type 2 from other diabetes for adults, so the team uses diagnosed diabetes as a
stand-in for type 2. CDC's White, Black, and Asian groups exclude Hispanic adults while the
trial groups include them, so those comparisons are approximate. American Indian or Alaska
Native adults are not shown in the CDC table, so that group has no patient group.

Heart failure is pending until prevalence.csv has patient counts by group for it.

Writes ppr_by_condition.csv and docs/ppr.js (for the website).
Run:  python3 build_ppr.py
"""
import csv, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
UNKNOWN = "Unknown or Not Reported"
CONDITIONS = ["breast_cancer", "prostate_cancer", "type_2_diabetes", "heart_failure"]

# trial group label, race_ columns to add up, label in prevalence.csv, SEER group
GROUPS = [
    ("White", ["White"], "White (includes Hispanic)", "White (includes Hispanic)"),
    ("Black or African American", ["Black or African American"],
     "Black (includes Hispanic)", "Black (includes Hispanic)"),
    ("Asian or Pacific Islander", ["Asian", "Native Hawaiian or Other Pacific Islander"],
     "Asian", "Non-Hispanic Asian / Pacific Islander"),
    ("American Indian or Alaska Native", ["American Indian or Alaska Native"],
     "American Indian / Alaska Native", "Non-Hispanic American Indian / Alaska Native"),
    ("More than one race", ["More than one race"], None, None),
]
ETHNICITY = ("Hispanic or Latino", "Hispanic", "Hispanic (any race)")
# Conditions whose patient groups are matched above, with the measure to read.
PATIENT_MEASURE = {"breast_cancer": "incidence", "prostate_cancer": "incidence",
                   "type_2_diabetes": "diagnosed_adults"}
# Condition name in prevalence.csv when it differs from the name above.
PATIENT_CONDITION = {"type_2_diabetes": "diabetes"}
# Conditions whose patient groups differ from GROUPS and ETHNICITY above:
# trial group -> (label in prevalence.csv, group name to show). (None, None) = no patient group.
PATIENT_GROUPS = {
    "type_2_diabetes": {
        "White": ("White (non-Hispanic)", "CDC: White, non-Hispanic"),
        "Black or African American": ("Black (non-Hispanic)", "CDC: Black, non-Hispanic"),
        "Asian or Pacific Islander": ("Asian (non-Hispanic)", "CDC: Asian, non-Hispanic"),
        "American Indian or Alaska Native": (None, None),  # not shown in the CDC table
        "Hispanic or Latino": ("Hispanic", "CDC: Hispanic"),
    },
}
LEAVE_OUT = {"prostate_cancer": "breast_cancer"}  # condition -> leave out trials also listed here

# The status column in prevalence.csv. Rows not yet checked against their source are never used.
NEVER_USE = {"verify_source"}
# "verify_group_label" rows have a transcribed count, but the exact SEER group name is
# not confirmed yet. They feed the Asian or Pacific Islander and American Indian or
# Alaska Native values. Set this to False to hold those values back as pending.
USE_UNCONFIRMED_GROUP_LABELS = True

CSV_COLUMNS = ["condition", "trial_group", "trials_used", "trial_participants", "trial_denominator",
               "trial_share_pct", "largest_trial_share_pct", "seer_group", "seer_share_pct", "ppr",
               "largest_trial_id", "trial_share_without_largest_pct", "ppr_without_largest"]


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def usable(row):
    """True when a prevalence.csv row can be used as a patient count."""
    status = (row.get("status") or "").strip()
    if status in NEVER_USE:
        return False
    if status == "verify_group_label" and not USE_UNCONFIRMED_GROUP_LABELS:
        return False
    return num(row.get("case_count")) > 0


def patient_count(rows, label, used=None):
    """Patient count for one label: the "all" sexes row if there is one, else female plus male."""
    by_sex = {}
    for r in rows:
        if (r.get("race_ethnicity") or "").strip() == label and usable(r):
            by_sex[(r.get("sex") or "").strip()] = r
    if not by_sex:
        return None
    picked = [by_sex["all"]] if "all" in by_sex else list(by_sex.values())
    if used is not None:
        used.update(id(r) for r in picked)
    return sum(num(r["case_count"]) for r in picked)


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "trials_clean.csv"), encoding="utf-8")))
    patients = list(csv.DictReader(open(os.path.join(HERE, "prevalence.csv"), encoding="utf-8")))
    needed = {"condition", "sex", "race_ethnicity", "measure", "case_count", "status"}
    missing = needed - set(patients[0].keys() if patients else [])
    if missing:
        sys.exit(f"prevalence.csv is missing columns: {', '.join(sorted(missing))}")

    listed = defaultdict(set)
    for r in rows:
        listed[r["nct_id"]].add(r["condition"])

    out, used = [], set()
    for cond in CONDITIONS:
        drop = LEAVE_OUT.get(cond)
        base = [r for r in rows if r["condition"] == cond and r["us_only"] == "1"
                and not (drop and drop in listed[r["nct_id"]])]
        race_trials = [r for r in base if r["race_format"] == "omb"]
        eth_trials = [r for r in base if r["ethnicity_reported"] == "1"]

        def known_race(r):
            return sum(num(r[k]) for k in r if k.startswith("race_") and k != "race_format"
                       and k != "race_" + UNKNOWN)

        def known_eth(r):
            return num(r["eth_Hispanic or Latino"]) + num(r["eth_Not Hispanic or Latino"])

        race_den = sum(known_race(r) for r in race_trials)
        eth_den = sum(known_eth(r) for r in eth_trials)

        # Patient rows for this condition, same measure as its "All" row.
        measure = PATIENT_MEASURE.get(cond)
        pcond = PATIENT_CONDITION.get(cond, cond)
        cond_patients = [p for p in patients if p["condition"] == pcond and p["measure"] == measure] if measure else []
        total = patient_count(cond_patients, "All", used)
        total_years = {p["years"] for p in cond_patients if p["race_ethnicity"] == "All" and usable(p)}
        cond_patients = [p for p in cond_patients if p["years"] in total_years]

        over = PATIENT_GROUPS.get(cond, {})
        specs = [(label, race_trials, race_den, lambda r, cols=cols: sum(num(r["race_" + c]) for c in cols),
                  known_race, *over.get(label, (plabel, sg)))
                 for label, cols, plabel, sg in GROUPS]
        specs.append((ETHNICITY[0], eth_trials, eth_den, lambda r: num(r["eth_Hispanic or Latino"]),
                      known_eth, *over.get(ETHNICITY[0], (ETHNICITY[1], ETHNICITY[2]))))

        for label, trials, den, count, known, plabel, sg in specs:
            per_trial = sorted((count(r) for r in trials), reverse=True)
            n = sum(per_trial)
            # Sensitivity check: leave out the trial with the most participants in this group.
            top = max(trials, key=count) if trials and n else None
            den_wo = den - known(top) if top else 0
            share_wo = (n - count(top)) / den_wo if top and den_wo > 0 else None
            share = n / den if den else None
            group_count = patient_count(cond_patients, plabel, used) if (plabel and total) else None
            seer_share = group_count / total if group_count and group_count <= total else None
            if not measure:
                status, sg = "pending", "pending"   # no patient groups matched for this condition yet
            elif not sg:
                status = "no_patient_group"
            else:
                status = "computed" if (share is not None and seer_share) else "pending"
            out.append({
                "condition": cond,
                "trial_group": label,
                "trials_used": len(trials),
                "trial_participants": int(n),
                "trial_denominator": int(den),
                "trial_share_pct": round(100 * share, 1) if share is not None else "",
                "largest_trial_share_pct": round(100 * per_trial[0] / n, 1) if n else "",
                "seer_group": sg or "",
                "seer_share_pct": round(100 * seer_share, 1) if seer_share else "",
                "ppr": round(share / seer_share, 2) if status == "computed" else "",
                "status": status,
                "largest_trial_id": top["nct_id"] if top else "",
                "trial_share_without_largest_pct": round(100 * share_wo, 1) if share_wo is not None else "",
                "ppr_without_largest": round(share_wo / seer_share, 2) if status == "computed" and share_wo is not None else "",
            })

    path = os.path.join(HERE, "ppr_by_condition.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    with open(os.path.join(HERE, "docs", "ppr.js"), "w", encoding="utf-8") as f:
        f.write("window.PPR = " + json.dumps(out, separators=(",", ":")) + ";\n")
    print(f"Wrote ppr_by_condition.csv and docs/ppr.js with {len(out)} rows")
    print(f"{'condition':<17}{'group':<34}{'trials':>7}{'people':>8}{'trial %':>9}{'patient %':>11}{'PPR':>9}{'top trial %':>13}{'PPR w/o top':>13}")
    shown = {"pending": "pending", "no_patient_group": "n/a"}
    for r in out:
        print(f"{r['condition']:<17}{r['trial_group']:<34}{r['trials_used']:>7}{r['trial_participants']:>8}"
              f"{r['trial_share_pct']!s:>9}{r['seer_share_pct']!s:>11}{shown.get(r['status'], r['ppr'])!s:>9}"
              f"{r['largest_trial_share_pct']!s:>13}{r['ppr_without_largest']!s:>13}")
    print(f"\nUsed {len(used)} of {len(patients)} rows in prevalence.csv. The rest are marked for checking, "
          f"give a rate with no patient count, or have a group label that is not matched to a trial group.")
    print("pending = no usable patient share yet. n/a = no matching patient group.")


if __name__ == "__main__":
    main()
