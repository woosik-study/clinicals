"""Reproduce research counts; does not modify prevalence.csv or chart outputs.

Requires pandas, numpy, scipy. Run from any directory with Python 3.
Source files are official public-use data, downloaded separately into sources/.
"""
from pathlib import Path
import hashlib
import json
import math
import zipfile

import numpy as np
import pandas as pd
from scipy.stats import t

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "sources"
FILES = {
    **{f"adult{y}csv.zip": f"https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/20{y}/adult{y}csv.zip" for y in (22, 23, 24)},
    **{f"{name}_L.xpt": f"https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/{name}_L.xpt" for name in ("DEMO", "MCQ")},
}


def variance(frame, values):
    """With-replacement stratified ultimate-cluster variance; retain zero domains.

    The CDC pooling example retains the existing PSTRAT/PPSU across years.
    Do not independently renumber the NHIS design variables by year.
    """
    work = frame[["stratum", "psu"]].assign(value=np.asarray(values))
    clusters = work.groupby(["stratum", "psu"]).value.sum()
    v = 0.0
    df = 0
    for _, group in clusters.groupby(level=0):
        m = len(group)
        assert m > 1, "Lonely PSU requires an explicit variance policy"
        v += m / (m - 1) * ((group - group.mean()) ** 2).sum()
        df += m - 1
    return float(v), df


def summarize(frame, group, sex, label, condition, years, source_url):
    domain = group & (frame.sex.eq(sex) if sex else True)
    cases = domain & frame.case
    weight = frame.weight
    estimate = float(weight[cases].sum())
    se2, df = variance(frame, weight * cases)
    se = math.sqrt(se2)
    rse = se / estimate if estimate else float("inf")
    # Descriptive log-t intervals; not a CDC-published or CDC-cleared estimate.
    multiplier = float(t.ppf(.975, df))
    low = estimate * math.exp(-multiplier * rse) if estimate else 0
    high = estimate * math.exp(multiplier * rse) if estimate else 0
    n = int(cases.sum())
    kish = estimate ** 2 / float((weight[cases] ** 2).sum()) if n else 0
    total = float(weight[frame.case].sum())
    share = estimate / total
    share_var, _ = variance(frame, weight * (cases.astype(float) - share * frame.case) / total)
    # Transparent conservative project screen, not a claim to implement all
    # NCHS effective-sample-size/CI standards. Count precision != PPR suitability.
    supported = n >= 10 and kish >= 10 and rse <= .30 and df >= 8
    return {
        "condition": condition, "sex": {0: "all", 1: "male", 2: "female"}[sex],
        "race_ethnicity": label, "years": years,
        "estimated_case_count": round(estimate, 6),
        "case_count_rounded": round(estimate), "unweighted_cases": n,
        "kish_effective_cases": round(kish, 3), "count_se": round(se, 3),
        "count_rse_pct": round(100 * rse, 3),
        "descriptive_count_ci95_low": round(low), "descriptive_count_ci95_high": round(high),
        "design_df": df, "patient_share_pct": round(100 * share, 6),
        "patient_share_se_pct": round(100 * math.sqrt(share_var), 6),
        "count_screen": "pass" if supported else "hold_low_precision",
        "source_url": source_url,
    }


def main():
    manifest = []
    for name, url in FILES.items():
        path = SOURCE / name
        assert path.is_file(), f"Download {url} to {path}"
        manifest.append({"file": name, "url": url, "bytes": path.stat().st_size,
                         "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    (HERE / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    adults = []
    annual = []
    for year in (22, 23, 24):
        with zipfile.ZipFile(SOURCE / f"adult{year}csv.zip") as z:
            d = pd.read_csv(z.open(f"adult{year}.csv"), usecols=[
                "DIBEV_A", "DIBTYPE_A", "DIBINS_A", "WTFA_A", "SEX_A",
                "PSTRAT", "PPSU", "RACEALLP_A", "HISPALLP_A"], low_memory=False)
        assert len(d) == {22: 27651, 23: 29522, 24: 32629}[year]
        # CDC's current surveillance algorithm: diagnosed and type 2, or
        # diagnosed and self-reported type 1 without current insulin use.
        d["case"] = d.DIBEV_A.eq(1) & (d.DIBTYPE_A.eq(2) | (d.DIBTYPE_A.eq(1) & d.DIBINS_A.eq(2)))
        d["weight"] = d.WTFA_A / 3
        d["sex"] = d.SEX_A
        d["stratum"], d["psu"] = d.PSTRAT, d.PPSU
        annual.append({"year": 2000 + year, "sample_adults": len(d),
                       "type2_sample_cases": int(d.case.sum()),
                       "type2_weighted_count": float(d.loc[d.case, "WTFA_A"].sum()),
                       "type2_unknown_race_weighted_count": float(d.loc[d.case & d.RACEALLP_A.isin([7, 8, 9]), "WTFA_A"].sum())})
        adults.append(d)
    d = pd.concat(adults, ignore_index=True)
    assert d.weight.gt(0).all()
    result = []
    nhis_groups = {
        "All": d.case.notna(),
        "White (includes Hispanic)": d.RACEALLP_A.eq(1),
        "Black (includes Hispanic)": d.RACEALLP_A.eq(2),
        "Asian only (includes Hispanic; excludes NHPI)": d.RACEALLP_A.eq(3),
        "American Indian / Alaska Native only (includes Hispanic)": d.RACEALLP_A.eq(4),
        "Hispanic (any race)": d.HISPALLP_A.eq(1),
        "AIAN and any other group (includes Hispanic)": d.RACEALLP_A.eq(5),
        "Other single and multiple races": d.RACEALLP_A.eq(6),
        "Unknown race": d.RACEALLP_A.isin([7, 8, 9]),
    }
    for label, mask in nhis_groups.items():
        for sex in (0, 1, 2):
            result.append(summarize(d, mask, sex, label, "type_2_diabetes", "2022-2024",
                                    "https://www.cdc.gov/nchs/nhis/documentation/2024-nhis.html"))
    # Race is independent of Hispanic origin: Hispanic is overlapping, not an
    # additional mutually-exclusive race. Unknown race stays in total patients.
    race_masks = [v for k, v in nhis_groups.items() if k not in ("All", "Hispanic (any race)")]
    assert np.all(np.sum(race_masks, axis=0) == 1)

    demo = pd.read_sas(SOURCE / "DEMO_L.xpt")
    medical = pd.read_sas(SOURCE / "MCQ_L.xpt")
    assert len(demo) == 11933 and len(medical) == 11744
    h = demo.merge(medical[["SEQN", "MCQ160B"]], on="SEQN", how="left", validate="one_to_one")
    assert int(h.MCQ160B.eq(1).sum()) == 343  # official codebook frequency
    assert h.loc[h.MCQ160B.eq(1), "RIDAGEYR"].ge(20).all()
    h["case"] = h.RIDAGEYR.ge(20) & h.MCQ160B.eq(1)
    h["sex"], h["weight"] = h.RIAGENDR, h.WTINT2YR
    h["stratum"], h["psu"] = h.SDMVSTRA, h.SDMVPSU
    hf_groups = {
        "All": h.SEQN.notna(),
        "Non-Hispanic White": h.RIDRETH3.eq(3),
        "Non-Hispanic Black": h.RIDRETH3.eq(4),
        "Non-Hispanic Asian (excludes NHPI)": h.RIDRETH3.eq(6),
        "Hispanic (any race)": h.RIDRETH3.isin([1, 2]),
        "Other non-Hispanic races (includes multiracial)": h.RIDRETH3.eq(7),
    }
    assert np.all(np.sum([v for k, v in hf_groups.items() if k != "All"], axis=0) == 1)
    for label, mask in hf_groups.items():
        for sex in (0, 1, 2):
            result.append(summarize(h, mask, sex, label, "heart_failure", "2021-2023",
                                    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.htm"))
    out = pd.DataFrame(result)
    out.to_csv(HERE / "patient_count_audit.csv", index=False)
    (HERE / "annual_nhis_checks.json").write_text(json.dumps(annual, indent=2) + "\n")
    for condition in out.condition.unique():
        subset = out[out.condition.eq(condition)]
        for label in subset.race_ethnicity.unique():
            vals = subset[subset.race_ethnicity.eq(label)].set_index("sex").estimated_case_count
            assert abs(vals["all"] - vals["male"] - vals["female"]) < .00001
    print(out[["condition", "sex", "race_ethnicity", "case_count_rounded", "unweighted_cases", "count_rse_pct", "count_screen"]].to_string(index=False))
    print("PASS: source frequencies, joins, race partitions, and sex totals reconciled")


if __name__ == "__main__":
    main()
