# Type 2 diabetes and heart failure patient-count handoff

Research date: 2026-11-21. Cancer inputs and PPR integration are unchanged.

## What changed

The ten undated all-diabetes percentages have been replaced with weighted estimates of adults with diagnosed type 2 diabetes from NHIS public-use data. These calculations estimate average annual patient populations for **2022–2024**.

The eight heart failure rates have been replaced with counts where supported by **NHANES August 2021–August 2023**. All eight estimates are in the audit; four sex-specific counts are withheld from `prevalence.csv` for low precision. AI/AN rows remain blank because the public data do not identify that group separately.

The previous 23 noncancer input rows (including their unmatched totals) are preserved in `original_diabetes_heart_failure_rows.csv`. The cancer rows are unchanged. The two generic all-diabetes rows are archived, not reused as type 2 denominators.

## Ten diabetes replacements

Population: US civilian noninstitutionalized adults age **18+**; diagnosed disease only. Weighted counts rounded to the nearest person for reproducibility, not a claim of person-level precision. Prefer rounded thousands in narrative.

| Source group | Male estimated patients | Female estimated patients | Both sexes |
|---|---:|---:|---:|
| White only, includes Hispanic | 7,762,572 | 6,812,279 | 14,574,851 |
| Black/African American only, includes Hispanic | 1,481,753 | 2,011,313 | 3,493,066 |
| Asian only, includes Hispanic; excludes NHPI | 742,120 | 750,890 | 1,493,010 |
| AI/AN only, includes Hispanic; excludes multiracial | 86,952 | 188,150 | 275,102 |
| Hispanic, any race | 1,976,054 | 2,089,453 | 4,065,507 |
| All patients, including other/multiple/unknown races | 10,999,847 | 10,858,393 | 21,858,239 |

Independent rounding can produce a difference of one patient between components and totals. Hispanic ethnicity overlaps the race rows; **do not sum those five groups**. Supporting other/multiple/unknown race counts are also included so the denominator is auditable.

The AI/AN male estimate has 46 sample cases and a count RSE of 21.45%; the female estimate has 79 cases and RSE 26.96%. These are estimates with considerable uncertainty, even after pooling, not precise enumerations. Their descriptive 95% intervals are in the audit.

### Disease definition and calculation

Following [CDC's current surveillance definitions](https://usdss.cdc.gov/diabetes/data/socrata/National_Burden_Magnitude_methods.html), select `DIBEV_A=1` and either `DIBTYPE_A=2`, or `DIBTYPE_A=1` with `DIBINS_A=2`. This is an algorithmic classification from self-report; it includes the latter respondents even though they self-report type 1. It excludes gestational-only diabetes, prediabetes, other types, unknown/refused type, and undiagnosed diabetes. Unknown type is not assigned to type 2 and a blanket 90–95% multiplier is not used. This follows the current CDC method rather than broadening the definition used in the older 2016 MMWR analysis.

For each selected group, sum `WTFA_A / 3` over the 2022, 2023, and 2024 Sample Adult files. This equals the arithmetic mean of the three independently weighted annual counts. The [NHIS survey description, pp. 47–49](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2024/srvydesc-508.pdf) gives the pooling rule. Keep the standard `PSTRAT` and `PPSU` across the pooled years for variance estimation; do not independently renumber them by year.

Race uses `RACEALLP_A`: 1 White only; 2 Black/African American only; 3 Asian only; 4 AIAN only. Ethnicity uses `HISPALLP_A=1`. The separate `RACEALLP_A=5` AIAN-and-other group is retained as supporting data and is not silently merged into AIAN-only. Other single/multiple races use 6, and unknown race uses 7/8/9. Hispanic respondents may have unascertained race; those patients remain in the total and are not redistributed into White or other races.

## Eight heart failure cells

Population: US civilian noninstitutionalized adults age **20+**, self-report of ever being told by a health professional they had congestive heart failure, `MCQ160B=1`. This is diagnosed-ever prevalence among living respondents, not admissions, visits, deaths, current ejection-fraction diagnoses, or all cardiovascular disease.

| Exact available group | Male estimate | Female estimate | Both-sex estimate | Input decision |
|---|---:|---:|---:|---|
| Non-Hispanic White | 2,818,885 | 2,193,771 | 5,012,657 | Counts retained |
| Non-Hispanic Black | 463,384† | 486,703 | 950,087 | Male held; both-sex count retained |
| Hispanic, any race | 397,640† | 430,342 | 827,982 | Male held; both-sex count retained |
| Non-Hispanic Asian, excludes NHPI | 119,113† | 55,780† | 174,893† | All three held |
| AI/AN | Unavailable | Unavailable | Unavailable | Not separable in public data |
| All patients, including other races | 4,191,695 | 3,363,035 | 7,554,730 | Matching derived denominator |

† **Audit estimates only**: these values are not put into usable `case_count` cells. NH Black men have 21 sample cases and count RSE 35.23%; Hispanic men 22 cases and RSE 39.36%; NH Asian men 8 cases and RSE 53.07%; NH Asian women 4 cases and RSE 47.10%. Even the both-sex Asian estimate has 12 cases and RSE 41.52%. A real weighted result does not make a small cell dependable.

Join DEMO_L and MCQ_L one-to-one on `SEQN` and sum **interview weight `WTINT2YR`**, not examination weight `WTMEC2YR`. The medical condition and demographic fields are collected at the interview; exam participation is not required. Keep the full survey design when calculating domain variances, including zero contributions outside a subgroup. The matching total is **7.555 million** from this analysis; do not divide these derived counts by the prior 7.7 million published total, which comes from a separate tabulation.

NHANES `RIDRETH3=1,2` combines Mexican American and Other Hispanic; 3 is NH White, 4 NH Black, 6 NH Asian, and 7 other NH races including multiracial. It cannot identify AI/AN separately, nor White/Black patients of Hispanic origin. [AHA's sex/race fact sheet](https://professional.heart.org/en/-/media/phd-files-2/science-news/2/2025-heart-and-stroke-stat-update/factsheets/2025-stats-update-fact-sheet-sex-and-race-and-cvd.pdf) independently confirms that NHANES prevalence data are unavailable separately for AI/AN and NHPI. AI/AN mortality statistics and Strong Heart Study regional cohorts cannot replace nationwide living-patient counts.

[CDC's weighting guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx) generally advises against combining August 2021–August 2023 with prior cycles because of the pandemic gap. All HF counts here use the same latest cycle.

## Precision and status conventions

`derived_estimate` means a source-derived count passed this research's explicit **conservative screening rule**: at least 10 observed cases, Kish weight-effective cases at least 10, count RSE no greater than 30%, and overall design degrees of freedom at least 8. It does **not** mean CDC published or certified this estimate, or that its group matches a trial group.

The screen is not a full implementation of [NCHS's rates/counts presentation standards](https://www.cdc.gov/nchs/data/series/sr_02/sr02-200.pdf). Kish effective cases describe unequal weights rather than the full sampling design effect. Audit confidence intervals use descriptive log-t intervals and overall design degrees of freedom; subgroup-specific degrees of freedom have not been established. Review the intervals before publishing comparisons.

`verify_source` is retained for held cells because that is the existing builder's exclusion flag. Their sources have been investigated; the unresolved issue is low precision or unavailable group detail. Those cells have blank counts and rates. The reasons appear in the source field and audit, rather than treating an unverified old percentage as corrected data.

## PPR integration requirements for Woosik

`build_ppr.py` still enables only cancers. Diabetes and heart failure PPR remain pending until the group and denominator choices below are resolved.

Before enabling these conditions:

1. Use `type_2_diabetes` / `diagnosed_prevalence` for NHIS and `heart_failure` / `diagnosed_prevalence` for NHANES. Use the **same source, period, age universe, disease algorithm, and denominator** for each group.
2. Make group mappings condition-specific. NHIS White/Black include Hispanic; NHANES White/Black **exclude** Hispanic. NHIS Asian excludes NHPI, whereas current trial PPR combines Asian and NHPI. Do not silently map an exact label to a broader trial category. Either change the trial grouping where supported, disclose an explicitly approximate comparison, or keep it pending. Public aggregate trial tables generally cannot recover NH White/Black race-by-ethnicity intersections.
3. For race comparisons, decide and disclose how to handle unknown patient race consistently with the known-race trial denominator. The NHIS all-patient total includes an estimated **1,624,512** patients with unknown race (7.432%); the known-race total rounds to **20,233,727**. Both denominators are computable from the audit. `patient_share_pct` in the audit always divides by **all** condition patients; it is not a within-race prevalence percentage. Hispanic ethnicity uses all patients and overlaps race.
4. Prefer the both-sex group rows where provided. **Never construct Black or Hispanic heart failure totals from just the passing female row** when the male cell is held. The directly computed both-sex counts pass the screen and avoid that truncation.
5. Match the adult age target or disclose the difference. The existing cleaned trial table does not provide participant-level adult counts. Neither source estimates institutionalized adults, military populations, undiagnosed disease, or pediatric patients.
6. Preserve Asian and AI/AN HF as pending under the latest-cycle evidence. Do not treat missing as zero or substitute mortality, hospitalizations, all-heart-disease, or a regional cohort.
7. Do not derive disease prevalence by multiplying age-adjusted within-group rates by Census totals. That would mix standardization weights, populations, and disease definitions.

## Sources and reproducibility

- [NHIS 2022 data and documentation](https://www.cdc.gov/nchs/nhis/documentation/2022-nhis.html)
- [NHIS 2023 data and documentation](https://www.cdc.gov/nchs/nhis/documentation/2023-nhis.html)
- [NHIS 2024 data and documentation](https://www.cdc.gov/nchs/nhis/documentation/2024-nhis.html), including the public codebook pp. 24–25 and 113–122.
- [Current CDC diabetes definitions](https://usdss.cdc.gov/diabetes/data/socrata/National_Burden_Magnitude_methods.html)
- [NHANES DEMO_L dictionary](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm)
- [NHANES MCQ_L dictionary](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.htm)
- [NHANES weights and cycle-combination guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx)
- [AHA 2025 sex/race/CVD fact sheet](https://professional.heart.org/en/-/media/phd-files-2/science-news/2/2025-heart-and-stroke-stat-update/factsheets/2025-stats-update-fact-sheet-sex-and-race-and-cvd.pdf)

Download the five public files listed in `source_manifest.json` into this directory's `sources/` folder. The manifest records their URLs and SHA-256 hashes. Source downloads are excluded from Git. Run `python3 research/prevalence_2026-11-21/reproduce.py` to regenerate the audit and annual checks; run `apply_counts.py` to apply the CSV inputs. Research dependencies are pandas, numpy, and scipy; the production refresh retains its existing standard-library dependencies.

`patient_count_audit.csv` records unrounded/rounded counts, sample cases, Kish effective cases, count standard errors/RSE, descriptive intervals, patient shares, and share standard errors. `annual_nhis_checks.json` records the independently weighted annual totals. `verification.json` records separate raw-file calculations and pipeline regression checks.
