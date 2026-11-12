# Who Is in the Trial?

Clinical trials produce much of the evidence behind which treatments reach the public and how doctors use them. When the people in a trial do not reflect the people who have the condition, it is harder to know how well the results apply to everyone. Many trials also leave out participant demographics or report them in ways that are hard to compare. This project makes that information easier to see by showing who took part in clinical trials for four common conditions, and how those trials reported race. The site does not rate trials or push a conclusion. It lets readers explore the data and interpret it themselves.

**Live site:** https://woosik-study.github.io/clinicals

Current numbers are on the site. This file explains the project and does not repeat them, because they change when the data is refreshed.

## What the site shows now

The site is a prototype. It covers breast cancer, prostate cancer, type 2 diabetes, and heart failure.

- **Filters:** a tab for each condition and a study phase filter. A study phase is a stage of testing a treatment, from small safety tests to large comparisons with existing care.
- **Summary stats:** number of trials, number of participants, share of trials that reported race, and share of participants who were female.
- **Race of participants:** a bar chart of race shares among participants with known race, using only trials that reported race in the standard categories. The share with unknown race is shown separately.
- **Ethnicity of participants:** Hispanic or Latino share among participants with known ethnicity, in trials that reported ethnicity.
- **Average age:** how trials are spread across average age ranges. Averages mix means and medians.
- **PPR:** for breast and prostate cancer, each group's share of trial participants compared with its share of patients, next to a reference line at 1.0. Uses only trials with all sites in the US.
- **Race reporting:** a bar chart of how many trials used standard categories, used their own categories, or did not report race.
- **Trial table:** the 50 largest trials in the current view, each linked to its ClinicalTrials.gov page. A trial listed under another condition says so.
- **Explainers:** short notes on study phases, PPR, and the limits of the data.

## PPR comparison

The site compares trial participants with real patient populations using the **Participation to Prevalence Ratio (PPR)**. Breast and prostate cancer are on the site now. White and Black PPR are waiting on two SEER counts, and type 2 diabetes and heart failure are waiting on patient data. For each group, the site shows two numbers side by side:

1. The group's share of trial participants, from ClinicalTrials.gov
2. The group's share of people who have the condition, from NCI SEER for the cancers (CDC planned for diabetes and heart failure)

PPR is (1) divided by (2). A value below 1 means the group makes up a smaller share of trial participants than of patients. PPR uses only trials with all sites in the US and leaves participants with unknown race or ethnicity out of the shares. Each value appears next to a reference line at 1.0, and individual groups are not labeled. The participant charts stay global.

How trial groups are matched to SEER groups:

| Trial group | SEER group |
|---|---|
| White | White (includes Hispanic) |
| Black or African American | Black (includes Hispanic) |
| Asian plus Native Hawaiian or Other Pacific Islander | Non-Hispanic Asian / Pacific Islander |
| American Indian or Alaska Native | Non-Hispanic American Indian / Alaska Native |
| Hispanic or Latino (ethnicity) | Hispanic (any race) |
| More than one race | None, so no PPR |

The two Non-Hispanic SEER groups leave out Hispanic patients while the trial groups include them, so those two comparisons are approximate. For prostate cancer, trials also listed under breast cancer are left out.

## Data

**Source:** the [ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api), a way for programs to request trial records directly from ClinicalTrials.gov.

**Filters:**

- Condition search for one of the four conditions
- Interventional trials, meaning trials that test a treatment
- Start date in 2010 or later
- Posted results

**Fields requested:** trial ID, title, phase, start date, enrollment count, study type, location countries, and the baseline characteristics module. Baseline characteristics are a trial's table of who enrolled.

**Fields extracted:** values come from the "Total" group in the baseline table.

- Sex: female and male counts
- Race: NIH/OMB categories, which are the standard US federal categories
- Ethnicity: NIH/OMB categories
- Average age: the reported value and whether it is a mean or a median
- Locations: the countries where a trial has sites, plus two flags, `us_only` (all sites in the US) and `any_us_site` (at least one US site). Both flags are blank when a trial lists no location.

Each trial's race reporting is labeled `omb` (standard categories), `customized` (the trial's own categories), or `none` (not reported). The site shows sex, race, ethnicity, and average age.

**Limits:** see [Limitations](#limitations) below, and the open issues in [BACKLOG.md](BACKLOG.md).

## Repo layout

| Path | What it is |
|---|---|
| `fetch_trials.py` | Downloads trial records, then writes the raw files and both CSVs |
| `build_site_data.py` | Converts `trials_clean.csv` into `docs/data.js` |
| `prevalence.csv` | Patient counts from SEER, matched to the trial race and ethnicity groups |
| `build_ppr.py` | Computes PPR from `trials_clean.csv` and `prevalence.csv`, and writes `ppr_by_condition.csv` and `docs/ppr.js` |
| `ppr_by_condition.csv` | PPR, trial share, patient share, and participant counts for each condition and group |
| `docs/` | The website, published by GitHub Pages: `index.html`, `style.css`, `app.js`, `data.js`, `ppr.js` |
| `trials_raw/` | Raw API records, one JSONL file per condition (JSONL has one JSON record per line) |
| `trials_clean.csv` | One row per trial per condition |
| `summary_by_condition.csv` | Race reporting rates, participant race shares, unknown race share, female share, and location counts for each condition |
| `BACKLOG.md` | Task board, work log, findings, open issues, AI usage log, and presentation outline |
| [`SITE_PLAN.md`](SITE_PLAN.md) | Plan for the final site's pages, with a rough layout of each |
| [`RESEARCH.md`](RESEARCH.md) | Shared list of sources and key findings for the site's resource list |

## Refresh the data

You need Python 3. The scripts use only the standard library, so there is nothing to install.

```bash
python3 fetch_trials.py
python3 build_site_data.py
python3 build_ppr.py
git add . && git commit -m "Refresh data" && git push
```

GitHub Pages updates the site after the push. When new patient counts are added to `prevalence.csv`, run only `python3 build_ppr.py`.

Other options for `fetch_trials.py`:

| Command | When to use it |
|---|---|
| `python3 fetch_trials.py --from-raw` | Rebuild the CSVs from `trials_raw/` without downloading, for example after changing the cleaning logic |
| `python3 fetch_trials.py --test` | Pull 5 trials per condition as a quick check |

`--test` overwrites `trials_raw/` and both CSVs with the small sample. To restore the full data afterward, run:

```bash
git checkout -- trials_raw trials_clean.csv summary_by_condition.csv
```

## Limitations

What the data and the site cannot tell you:

- The data covers only trials with posted results on ClinicalTrials.gov.
- Trials that report race in their own custom categories are left out of the race charts.
- About 27% of records have no study phase. ClinicalTrials.gov uses "Not Applicable" for trials without FDA defined phases, such as device or behavioral studies.
- SEER counts new cases, not people living with a condition.
- SEER treats Hispanic as a separate group, while trials record Hispanic origin as ethnicity, separately from race. Trial and SEER race groups therefore do not match exactly.
- Trials listed under two conditions count in each condition.

## Sources

The full resource list is in [RESEARCH.md](RESEARCH.md).

## AI use

We used AI tools (Claude) to help write code and edit text. The team reviewed all of the work. Our AI conversations are included in our final submission.

## Maintenance

- **Last updated:** data snapshot 2026-11-04
- **Ongoing updates:** [TBD by team]
- **Contact:** see Contact below

## Contact

[name], [email]

We reply within 24 hours through Friday of finals week.

## Team

Woosik Kim, Sanjana, Saurabi, and Sneha

CSE 194, UC San Diego, Fall 2026
