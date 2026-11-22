"""Apply researched inputs locally, preserving baseline cancer rows and old inputs.

Run reproduce.py first. Chart integration is deliberately outside this script.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    path = ROOT / "prevalence.csv"
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        current = list(reader)
    archive = HERE / "original_diabetes_heart_failure_rows.csv"
    if not archive.exists():
        assert sum(r["condition"] == "diabetes" for r in current) == 12
        assert sum(r["condition"] == "heart_failure" for r in current) == 11
        with archive.open("w", newline="") as f:
            w = csv.DictWriter(f, fields, lineterminator="\n")
            w.writeheader()
            w.writerows(r for r in current if r["condition"] in ("diabetes", "heart_failure"))
    cancer = [r for r in current if r["condition"] not in ("diabetes", "type_2_diabetes", "heart_failure")]
    with (HERE / "patient_count_audit.csv").open(newline="") as f:
        audit = list(csv.DictReader(f))
    result = []
    for r in audit:
        condition = r["condition"]
        row = dict.fromkeys(fields, "")
        row.update(condition=condition, sex=r["sex"], race_ethnicity=r["race_ethnicity"],
                   measure="diagnosed_prevalence", years=r["years"],
                   source=("CDC/NCHS NHIS 2022-2024; author calculation; " if condition == "type_2_diabetes"
                           else "CDC/NCHS NHANES Aug 2021-Aug 2023; author calculation; ") + r["source_url"],
                   status="derived_estimate" if r["count_screen"] == "pass" else "verify_source")
        if r["count_screen"] == "pass":
            row["case_count"] = r["case_count_rounded"]
        else:
            row["source"] += "; HOLD: low precision; see patient_count_audit.csv"
        # Unsupported estimates remain in audit only, not usable patient inputs.
        result.append(row)
    for sex in ("all", "male", "female"):
        row = dict.fromkeys(fields, "")
        row.update(condition="heart_failure", sex=sex,
                   race_ethnicity="American Indian / Alaska Native", measure="diagnosed_prevalence",
                   years="2021-2023", status="verify_source",
                   source="Not separately identifiable in public NHANES RIDRETH3; https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm")
        result.append(row)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, lineterminator="\n")
        w.writeheader()
        w.writerows(cancer + result)
    assert len(cancer) == 16
    print(f"Saved {len(result)} researched rows; preserved {len(cancer)} cancer rows")


if __name__ == "__main__":
    main()
