"""Independent count reconciliation and isolated regression of the PPR pipeline."""
import ast
import csv
from decimal import Decimal
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    audit = list(csv.DictReader((HERE / "patient_count_audit.csv").open()))
    # Read raw NHIS CSV records with stdlib and sum Decimal weights, without
    # using reproduce.py, pandas masks, or floating point aggregation.
    sums = {}
    for year in (22, 23, 24):
        with zipfile.ZipFile(HERE / "sources" / f"adult{year}csv.zip") as z:
            for r in csv.DictReader(io.TextIOWrapper(z.open(f"adult{year}.csv"))):
                if r["DIBEV_A"] != "1":
                    continue
                if r["DIBTYPE_A"] != "2" and not (r["DIBTYPE_A"] == "1" and r["DIBINS_A"] == "2"):
                    continue
                race, sex = int(r["RACEALLP_A"]), int(r["SEX_A"])
                labels = ["All", {
                    1: "White (includes Hispanic)", 2: "Black (includes Hispanic)",
                    3: "Asian only (includes Hispanic; excludes NHPI)",
                    4: "American Indian / Alaska Native only (includes Hispanic)",
                    5: "AIAN and any other group (includes Hispanic)",
                    6: "Other single and multiple races",
                }.get(race, "Unknown race")]
                if r["HISPALLP_A"] == "01" or r["HISPALLP_A"] == "1":
                    labels.append("Hispanic (any race)")
                for label in labels:
                    for sx in ("all", {1: "male", 2: "female"}[sex]):
                        key = ("type_2_diabetes", sx, label)
                        sums[key] = sums.get(key, Decimal(0)) + Decimal(r["WTFA_A"]) / 3
    # XPT parsing uses pandas, but the separate record join and count summation
    # below do not use the production analysis's merge, masks, or group logic.
    demos = pd.read_sas(HERE / "sources" / "DEMO_L.xpt").to_dict("records")
    answers = {r["SEQN"]: r["MCQ160B"] for r in pd.read_sas(HERE / "sources" / "MCQ_L.xpt").to_dict("records")}
    for r in demos:
        if answers.get(r["SEQN"]) != 1 or r["RIDAGEYR"] < 20:
            continue
        race = int(r["RIDRETH3"])
        label = {1: "Hispanic (any race)", 2: "Hispanic (any race)",
                 3: "Non-Hispanic White", 4: "Non-Hispanic Black",
                 6: "Non-Hispanic Asian (excludes NHPI)",
                 7: "Other non-Hispanic races (includes multiracial)"}[race]
        for group in ("All", label):
            for sx in ("all", {1: "male", 2: "female"}[int(r["RIAGENDR"])]):
                key = ("heart_failure", sx, group)
                sums[key] = sums.get(key, Decimal(0)) + Decimal(str(r["WTINT2YR"]))
    assert len(sums) == len(audit) == 45
    max_error = 0
    for a in audit:
        key = tuple(a[k] for k in ("condition", "sex", "race_ethnicity"))
        error = abs(sums[key] - Decimal(a["estimated_case_count"]))
        max_error = max(max_error, float(error))
        assert error < Decimal("0.00001"), (key, error)
        assert int(a["case_count_rounded"]) == round(sums[key])
    baseline = subprocess.check_output(["git", "show", "HEAD:prevalence.csv"], cwd=ROOT, text=True)
    old = list(csv.DictReader(io.StringIO(baseline)))
    with (ROOT / "prevalence.csv").open() as f:
        new = list(csv.DictReader(f))
    old_cancer = [r for r in old if r["condition"].endswith("cancer")]
    assert old_cancer == [r for r in new if r["condition"].endswith("cancer")]
    index = {tuple(a[k] for k in ("condition", "sex", "race_ethnicity")): a for a in audit}
    for r in new:
        assert None not in r, "Malformed CSV row"
        if r["condition"].endswith("cancer"):
            continue
        assert not r["prevalence_pct"] and not r["incidence_per_100000"]
        assert r["years"] and "https://" in r["source"]
        key = tuple(r[k] for k in ("condition", "sex", "race_ethnicity"))
        if key in index and index[key]["count_screen"] == "pass":
            assert r["case_count"] == index[key]["case_count_rounded"]
            assert r["status"] == "derived_estimate"
        else:
            assert r["status"] == "verify_source" and not r["case_count"]
    assert sum(r["condition"] == "type_2_diabetes" and r["sex"] in ("male", "female")
               and r["race_ethnicity"] in {"White (includes Hispanic)", "Black (includes Hispanic)",
               "Asian only (includes Hispanic; excludes NHPI)",
               "American Indian / Alaska Native only (includes Hispanic)", "Hispanic (any race)"}
               and bool(r["case_count"]) for r in new) == 10
    # Run old and new inputs against the same current builder in temporary
    # directories; committed outputs may predate the latest cancer additions.
    generated = []
    for content in (baseline, (ROOT / "prevalence.csv").read_text()):
        with tempfile.TemporaryDirectory() as folder:
            temp = Path(folder)
            (temp / "docs").mkdir()
            for name in ("build_ppr.py", "trials_clean.csv"):
                shutil.copy2(ROOT / name, temp / name)
            (temp / "prevalence.csv").write_text(content)
            run = subprocess.run([sys.executable, str(temp / "build_ppr.py")], capture_output=True, text=True)
            assert run.returncode == 0, run.stderr
            generated.append(((temp / "ppr_by_condition.csv").read_bytes(), (temp / "docs/ppr.js").read_bytes()))
    assert generated[0] == generated[1], "PPR changed despite data-only scope"
    for name in ("build_ppr.py", "ppr_by_condition.csv", "docs/ppr.js", "trials_clean.csv"):
        assert (ROOT / name).read_bytes() == subprocess.check_output(["git", "show", "HEAD:" + name], cwd=ROOT)
    for path in HERE.glob("*.py"):
        ast.parse(path.read_text())
    report = {"independent_raw_count_checks": len(audit), "maximum_absolute_count_difference": max_error,
              "original_cancer_rows_unchanged": len(old_cancer), "requested_diabetes_sex_cells_populated": 10,
              "source_urls_and_years_present": True, "unsupported_counts_withheld": True,
              "old_vs_new_ppr_outputs_identical": True, "production_scripts_and_chart_files_unchanged": True,
              "python_syntax_valid": True}
    (HERE / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
