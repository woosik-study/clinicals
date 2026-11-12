"""Compute PPR (Participation to Prevalence Ratio) from trials_clean.csv and prevalence.csv.

PPR = a group's share of trial participants / that group's share of patients.

Rules (decided by the team, see BACKLOG.md section 5):
  - Trials: only us_only trials (all sites in the US).
  - Race: only trials using standard NIH/OMB race categories. "Unknown or Not Reported"
    is left out of the denominator.
  - Ethnicity: only trials that reported NIH/OMB ethnicity. Unknown ethnicity is left out.
  - Prostate cancer: trials also listed under breast cancer are left out.
  - Groups are not labeled. The site shows each value next to a reference line at 1.0.

Each trial group is compared with the closest SEER group:
  White                      -> White (includes Hispanic)
  Black or African American  -> Black (includes Hispanic)
  Asian + Native Hawaiian or Other Pacific Islander -> Non-Hispanic Asian / Pacific Islander
  American Indian or Alaska Native -> Non-Hispanic American Indian / Alaska Native
  Hispanic or Latino (ethnicity)   -> Hispanic (any race)
  More than one race: no SEER group, so trial share only.

Writes ppr_by_condition.csv. Rows whose SEER count is blank in prevalence.csv get no PPR.
Run:  python3 build_ppr.py
"""
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
UNKNOWN = "Unknown or Not Reported"
# trial group label -> (race_ columns to add up, SEER group), or ethnicity
GROUPS = [
    ("White", ["White"], "White (includes Hispanic)"),
    ("Black or African American", ["Black or African American"], "Black (includes Hispanic)"),
    ("Asian or Pacific Islander", ["Asian", "Native Hawaiian or Other Pacific Islander"],
     "Non-Hispanic Asian / Pacific Islander"),
    ("American Indian or Alaska Native", ["American Indian or Alaska Native"],
     "Non-Hispanic American Indian / Alaska Native"),
    ("More than one race", ["More than one race"], None),
]
ETHNICITY = ("Hispanic or Latino", "Hispanic (any race)")
LEAVE_OUT = {"prostate_cancer": "breast_cancer"}  # condition -> leave out trials also listed here


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "trials_clean.csv"), encoding="utf-8")))
    seer = {(r["condition"], r["seer_group"]): r
            for r in csv.DictReader(open(os.path.join(HERE, "prevalence.csv"), encoding="utf-8"))}
    listed = defaultdict(set)
    for r in rows:
        listed[r["nct_id"]].add(r["condition"])

    out = []
    for cond in sorted({c for c, _ in seer}):
        drop = LEAVE_OUT.get(cond)
        base = [r for r in rows if r["condition"] == cond and r["us_only"] == "1"
                and not (drop and drop in listed[r["nct_id"]])]
        race_trials = [r for r in base if r["race_format"] == "omb"]
        eth_trials = [r for r in base if r["ethnicity_reported"] == "1"]

        def known_race(r):
            return sum(num(r[k]) for k in r if k.startswith("race_") and k != "race_format"
                       and k != "race_" + UNKNOWN)

        race_den = sum(known_race(r) for r in race_trials)
        eth_den = sum(num(r["eth_Hispanic or Latino"]) + num(r["eth_Not Hispanic or Latino"])
                      for r in eth_trials)

        specs = [(label, race_trials, race_den, lambda r, cols=cols: sum(num(r["race_" + c]) for c in cols), sg)
                 for label, cols, sg in GROUPS]
        specs.append((ETHNICITY[0], eth_trials, eth_den, lambda r: num(r["eth_Hispanic or Latino"]), ETHNICITY[1]))

        for label, trials, den, count, sg in specs:
            per_trial = sorted((count(r) for r in trials), reverse=True)
            n = sum(per_trial)
            share = n / den if den else None
            s = seer.get((cond, sg)) if sg else None
            seer_share = num(s["seer_count"]) / num(s["seer_total"]) if s and s["seer_count"] else None
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
                "ppr": round(share / seer_share, 2) if share is not None and seer_share else "",
            })

    path = os.path.join(HERE, "ppr_by_condition.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"Wrote ppr_by_condition.csv with {len(out)} rows")
    print(f"{'condition':<17}{'group':<34}{'trials':>7}{'people':>8}{'trial %':>9}{'SEER %':>8}{'PPR':>6}{'top trial %':>13}")
    for r in out:
        print(f"{r['condition']:<17}{r['trial_group']:<34}{r['trials_used']:>7}{r['trial_participants']:>8}"
              f"{r['trial_share_pct']!s:>9}{r['seer_share_pct']!s:>8}{r['ppr']!s:>6}{r['largest_trial_share_pct']!s:>13}")


if __name__ == "__main__":
    main()
