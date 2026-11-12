"""Turn trials_clean.csv into docs/data.js (window.TRIALS = [...]) for the website."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
RACES = ["American Indian or Alaska Native", "Asian", "Native Hawaiian or Other Pacific Islander",
         "Black or African American", "White", "More than one race", "Unknown or Not Reported"]
ETHNICITIES = ["Hispanic or Latino", "Not Hispanic or Latino", "Unknown or Not Reported"]
def f(v):
    try: return float(v)
    except Exception: return None
def flag(v):
    """1 or 0 for a location flag, None when the trial lists no location."""
    return int(v) if v in ("0", "1") else None
rows = []
with open(os.path.join(HERE, "trials_clean.csv")) as fh:
    for r in csv.DictReader(fh):
        rows.append({
            "id": r["nct_id"], "c": r["condition"], "t": r["title"], "p": r["phases"],
            "y": r["start_year"], "n": f(r["baseline_n"]) or f(r["enrollment"]),
            "rf": r["race_format"], "fe": f(r.get("female")), "ma": f(r.get("male")),
            "r": [f(r.get("race_" + x)) or 0 for x in RACES],
            "uo": flag(r.get("us_only")), "au": flag(r.get("any_us_site")),
            # ethnicity [Hispanic, not Hispanic, unknown], only when the trial reported it
            "e": [f(r.get("eth_" + x)) or 0 for x in ETHNICITIES] if r.get("ethnicity_reported") == "1" else None,
            "ag": f(r.get("age_value")), "ap": r.get("age_param") or None,
        })
with open(os.path.join(HERE, "docs", "data.js"), "w") as fh:
    fh.write("window.TRIALS = " + json.dumps(rows, separators=(",", ":")) + ";\n")
print(f"Wrote docs/data.js with {len(rows)} trials")
