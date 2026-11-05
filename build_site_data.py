"""Turn trials_clean.csv into site/data.js (window.TRIALS = [...]) for the website."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
RACES = ["American Indian or Alaska Native", "Asian", "Native Hawaiian or Other Pacific Islander",
         "Black or African American", "White", "More than one race", "Unknown or Not Reported"]
def f(v):
    try: return float(v)
    except Exception: return None
rows = []
with open(os.path.join(HERE, "trials_clean.csv")) as fh:
    for r in csv.DictReader(fh):
        rows.append({
            "id": r["nct_id"], "c": r["condition"], "t": r["title"], "p": r["phases"],
            "y": r["start_year"], "n": f(r["baseline_n"]) or f(r["enrollment"]),
            "rf": r["race_format"], "fe": f(r.get("female")), "ma": f(r.get("male")),
            "r": [f(r.get("race_" + x)) or 0 for x in RACES],
        })
with open(os.path.join(HERE, "site", "data.js"), "w") as fh:
    fh.write("window.TRIALS = " + json.dumps(rows, separators=(",", ":")) + ";\n")
print(f"Wrote site/data.js with {len(rows)} trials")
