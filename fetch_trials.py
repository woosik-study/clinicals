"""
Clinicals project: pull participant demographics from ClinicalTrials.gov (API v2).

Scope: interventional trials with posted results, started 2010 or later,
for 4 conditions. Saves:
  trials_raw/<condition>.jsonl   raw API records (for re-processing)
  trials_clean.csv               one row per trial, demographics from the "Total" group
  summary_by_condition.csv       per condition: race reporting rate + participant shares

Run:  python3 fetch_trials.py          (full pull)
      python3 fetch_trials.py --test   (5 trials per condition, quick check)
"""
import csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error

CONDITIONS = {
    "breast_cancer": "breast cancer",
    "prostate_cancer": "prostate cancer",
    "type_2_diabetes": "type 2 diabetes",
    "heart_failure": "heart failure",
}
BASE = "https://clinicaltrials.gov/api/v2/studies"
FIELDS = "NCTId,BriefTitle,Phase,StartDate,EnrollmentCount,StudyType,BaselineCharacteristicsModule"
ADV = "AREA[StudyType]INTERVENTIONAL AND AREA[StartDate]RANGE[2010-01-01,MAX]"
HERE = os.path.dirname(os.path.abspath(__file__))
TEST = "--test" in sys.argv

OMB_RACE = ["American Indian or Alaska Native", "Asian", "Native Hawaiian or Other Pacific Islander",
            "Black or African American", "White", "More than one race", "Unknown or Not Reported"]
OMB_ETH = ["Hispanic or Latino", "Not Hispanic or Latino", "Unknown or Not Reported"]


def get(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "clinicals-class-project/1.0", "Accept": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 400:
                raise
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("failed: " + url)


def fetch(cond_query):
    params = {"query.cond": cond_query, "filter.advanced": ADV, "aggFilters": "results:with",
              "fields": FIELDS, "pageSize": 5 if TEST else 200, "countTotal": "true", "format": "json"}
    try:
        first = get(params)
    except urllib.error.HTTPError:
        params.pop("fields")  # fall back to full records if a field name is rejected
        first = get(params)
    print(f"  total matching: {first.get('totalCount')}")
    page, studies = first, []
    while True:
        studies += page.get("studies", [])
        tok = page.get("nextPageToken")
        if TEST or not tok:
            break
        params["pageToken"] = tok
        page = get(params)
        print(f"  fetched {len(studies)}", end="\r")
        time.sleep(0.3)
    print(f"  fetched {len(studies)}      ")
    return studies


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except Exception:
        return None


def parse(study, cond):
    ps, rs = study.get("protocolSection", {}), study.get("resultsSection", {})
    ident, design, status = ps.get("identificationModule", {}), ps.get("designModule", {}), ps.get("statusModule", {})
    bl = rs.get("baselineCharacteristicsModule", {})
    row = {"nct_id": ident.get("nctId"), "condition": cond, "title": ident.get("briefTitle"),
           "phases": "|".join(design.get("phases", []) or []),
           "start_year": (status.get("startDateStruct", {}).get("date") or "")[:4],
           "enrollment": design.get("enrollmentInfo", {}).get("count")}
    groups = bl.get("groups", [])
    total = next((g["id"] for g in groups if (g.get("title") or "").strip().lower() == "total"), None)
    if total is None and len(groups) == 1:
        total = groups[0]["id"]
    for d in bl.get("denoms", []):
        if d.get("units", "").lower() == "participants":
            for c in d.get("counts", []):
                if c.get("groupId") == total:
                    row["baseline_n"] = num(c.get("value"))
    row["race_format"] = "none"
    row["sex_reported"] = 0
    row["ethnicity_reported"] = 0
    for m in bl.get("measures", []):
        title = (m.get("title") or "").lower()
        cats = {}
        for cl in m.get("classes", []):
            for cat in cl.get("categories", []):
                for meas in cat.get("measurements", []):
                    if meas.get("groupId") == total:
                        name = cat.get("title") or cl.get("title") or ""
                        cats[name] = num(meas.get("value"))
        if title.startswith("sex"):
            row["sex_reported"] = 1
            for k, v in cats.items():
                if k.lower() in ("female", "male"):
                    row[k.lower()] = v
        elif "race" in title and "nih/omb" in title:
            row["race_format"] = "omb"
            for r in OMB_RACE:
                row["race_" + r] = cats.get(r, 0)
        elif "ethnicity" in title and "nih/omb" in title:
            row["ethnicity_reported"] = 1
            for e in OMB_ETH:
                row["eth_" + e] = cats.get(e, 0)
        elif "race" in title and row["race_format"] == "none":
            row["race_format"] = "customized"
        elif title.startswith("age") and "continuous" in title:
            for cl in m.get("classes", []):
                for cat in cl.get("categories", []):
                    for meas in cat.get("measurements", []):
                        if meas.get("groupId") == total:
                            row["age_value"] = num(meas.get("value"))
                            row["age_param"] = m.get("paramType")
    row["has_total_group"] = int(total is not None)
    return row


def main():
    raw_dir = os.path.join(HERE, "trials_raw")
    os.makedirs(raw_dir, exist_ok=True)
    rows = []
    for key, q in CONDITIONS.items():
        print(f"{key} ({q})")
        studies = fetch(q)
        with open(os.path.join(raw_dir, key + ".jsonl"), "w") as f:
            for s in studies:
                f.write(json.dumps(s) + "\n")
        rows += [parse(s, key) for s in studies]

    cols = ["nct_id", "condition", "title", "phases", "start_year", "enrollment", "baseline_n", "has_total_group",
            "sex_reported", "female", "male", "race_format"] + ["race_" + r for r in OMB_RACE] + \
           ["ethnicity_reported"] + ["eth_" + e for e in OMB_ETH] + ["age_value", "age_param"]
    with open(os.path.join(HERE, "trials_clean.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    summ = []
    for key in CONDITIONS:
        rs = [r for r in rows if r["condition"] == key]
        omb = [r for r in rs if r["race_format"] == "omb"]
        tot = sum(sum(r.get("race_" + x) or 0 for x in OMB_RACE) for r in omb)
        sx = [r for r in rs if r.get("female") is not None or r.get("male") is not None]
        fem = sum(r.get("female") or 0 for r in sx)
        sxt = fem + sum(r.get("male") or 0 for r in sx)
        s = {"condition": key, "trials": len(rs),
             "pct_trials_reporting_race_omb": round(100 * len(omb) / len(rs), 1) if rs else None,
             "pct_trials_reporting_race_any": round(100 * sum(r["race_format"] != "none" for r in rs) / len(rs), 1) if rs else None,
             "participants_in_omb_race_trials": int(tot),
             "pct_female": round(100 * fem / sxt, 1) if sxt else None}
        for x in OMB_RACE:
            s["pct_" + x] = round(100 * sum(r.get("race_" + x) or 0 for r in omb) / tot, 1) if tot else None
        summ.append(s)
    with open(os.path.join(HERE, "summary_by_condition.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summ[0].keys()))
        w.writeheader()
        w.writerows(summ)
    print("\nDone. Wrote trials_clean.csv and summary_by_condition.csv in", HERE)


if __name__ == "__main__":
    main()
