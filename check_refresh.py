"""Safety checks for the daily data refresh. Run after fetch_trials.py, build_site_data.py, and build_ppr.py.

Compares the freshly built files with the snapshot committed in this repo. If any
check fails, the script exits with an error, so the daily job stops and the live
site keeps yesterday's data.

Checks:
  1. trials_clean.csv has every column the snapshot has.
  2. No condition has more than 10% fewer trials than the snapshot.
  3. docs/data.js is not empty and has one record per row of trials_clean.csv.
  4. Every PPR value the snapshot has for breast and prostate cancer is still computed.
  5. data_updated.txt holds a download time from the last 6 hours.

Run:  python3 check_refresh.py
"""
import csv, io, json, os, subprocess, sys
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_DROP = 0.10          # a condition may lose at most 10% of its trials
MAX_AGE_HOURS = 6
PPR_CONDITIONS = ("breast_cancer", "prostate_cancer")


def snapshot(name):
    """The committed version of a file, as CSV rows."""
    text = subprocess.run(["git", "show", "HEAD:" + name], cwd=HERE, check=True,
                          capture_output=True, text=True, encoding="utf-8").stdout
    return list(csv.DictReader(io.StringIO(text, newline="")))


def current(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def is_number(v):
    try:
        float(v)
        return True
    except (TypeError, ValueError):
        return False


def main():
    problems = []
    old, new = snapshot("trials_clean.csv"), current("trials_clean.csv")

    missing = set(old[0]) - set(new[0] if new else [])
    if missing:
        problems.append("trials_clean.csv is missing columns: " + ", ".join(sorted(missing)))

    old_n, new_n = Counter(r["condition"] for r in old), Counter(r.get("condition") for r in new)
    for cond, n in sorted(old_n.items()):
        floor = n * (1 - MAX_DROP)
        status = "ok" if new_n[cond] >= floor else "TOO FEW"
        print(f"  {cond:<18} snapshot {n:>5}   now {new_n[cond]:>5}   {status}")
        if new_n[cond] < floor:
            problems.append(f"{cond} has {new_n[cond]} trials, more than 10% below the snapshot's {n}")

    try:
        lines = open(os.path.join(HERE, "docs", "data.js"), encoding="utf-8").read().splitlines()
        prefix = "window.TRIALS = "
        trials = json.loads(lines[0][len(prefix):].rstrip(";")) if lines and lines[0].startswith(prefix) else []
    except (OSError, ValueError):
        trials = []
    if not trials:
        problems.append("docs/data.js is empty or unreadable")
    elif len(trials) != len(new):
        problems.append(f"docs/data.js has {len(trials)} records but trials_clean.csv has {len(new)} rows")

    now_ppr = {(r["condition"], r["trial_group"]): r["ppr"] for r in current("ppr_by_condition.csv")}
    for r in snapshot("ppr_by_condition.csv"):
        key = (r["condition"], r["trial_group"])
        if r["condition"] in PPR_CONDITIONS and is_number(r["ppr"]) and not is_number(now_ppr.get(key)):
            problems.append(f"PPR is no longer computed for {key[0]}, {key[1]}")
    if not os.path.getsize(os.path.join(HERE, "docs", "ppr.js")):
        problems.append("docs/ppr.js is empty")

    try:
        stamp = open(os.path.join(HERE, "data_updated.txt")).read().strip()
        age = datetime.now(timezone.utc) - datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        if not 0 <= age.total_seconds() <= MAX_AGE_HOURS * 3600:
            problems.append(f"data_updated.txt says {stamp}, which is not within the last {MAX_AGE_HOURS} hours")
    except (OSError, ValueError):
        problems.append("data_updated.txt has no download time, so the download did not run")

    if problems:
        print("\nRefresh checks FAILED. The site was not updated.")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print(f"\nRefresh checks passed: {len(new)} rows, data last updated {stamp}.")


if __name__ == "__main__":
    main()
