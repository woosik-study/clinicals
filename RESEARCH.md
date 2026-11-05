# Research Sources

This is our shared list of every source used for the project and the final site's resource list, which needs at least 10 sources.

Each team member has a section for the topics in their role. The Added by column shows who added each source.

## How to add a source

1. Open `RESEARCH.md` on GitHub and click the pencil icon.
2. Go to your section and add a row to the table for your topic. Add a line under Key findings if you found something we should use. Write TBD if you are not sure yet.
3. Click **Commit changes**.

## Woosik: ClinicalTrials.gov data structure

### Sources

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| Results data element definitions | https://prsinfo.clinicaltrials.gov/results_definitions.html | official guidance | How baseline characteristics are defined | Woosik | 2026-11-05 |
| Race and ethnicity results table format | https://cdn.clinicaltrials.gov/documents/results_table_layout/DataEntryTable_BaselineRegionRaceEthnicityForm.pdf | official guidance | The NIH/OMB race categories our pipeline uses | Woosik | 2026-11-05 |

### Key findings

- Race and ethnicity can be reported as Race (NIH/OMB), Ethnicity (NIH/OMB), Race/Ethnicity Customized, or Race and Ethnicity Not Collected. Source: Results data element definitions
- Required baseline measures include age, sex or gender, race, and ethnicity if it was collected under the protocol. Source: Results data element definitions
- The April 2017 template lists "Native Hawaiian or Pacific Islander", but our pipeline matches "Native Hawaiian or Other Pacific Islander". Source: Race and ethnicity results table format

## Sanjana: Existing tools

### Sources

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| FDA Drug Trials Snapshots | https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots | official data | The existing tool we extend | Woosik | 2026-11-05 |
| FDA 2024 Drug Trials Snapshots Summary Report | https://www.americanpharmaceuticalreview.com/1315-News/620108-FDA-Releases-2024-Drug-Trials-Snapshots-Summary-Report/ | news | What Snapshots reports each year | Woosik | 2026-11-05 |

### Key findings

- Snapshots give concise information about who took part in the key clinical trials that supported the original FDA approval of new drugs. Source: FDA Drug Trials Snapshots
- The 2024 report covers 50 novel drugs and about 31,000 patients, broken down by sex, race, ethnicity, age group, and US participation. Source: FDA 2024 Drug Trials Snapshots Summary Report

## Saurabi: Prevalence data

### Sources

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| SEER Cancer Statistics Review 1975 to 2017, Table 23.11: Cancer of the Prostate (Invasive) | https://seer.cancer.gov/archive/csr/1975_2017/results_single/sect_23_table.11.pdf | official data | Checking how SEER reports cancer data by race | Woosik | 2026-11-05 |
| CDC National Diabetes Statistics Report | https://www.cdc.gov/diabetes/php/data-research/index.html | official data | Checking how CDC reports diabetes data by race and sex | Woosik | 2026-11-05 |

### Key findings

- The SEER table gives age adjusted incidence and mortality rates per 100,000 people, not counts or shares of patients. Source: SEER Table 23.11
- The SEER table uses White, White Hispanic, White Non Hispanic, Black, Asian/Pacific Islander, American Indian/Alaska Native, and Hispanic, which do not match our race categories one to one. Source: SEER Table 23.11
- The SEER table comes from an archived 1975 to 2017 edition and covers prostate cancer only, so the current edition and breast cancer still need checking. Source: SEER Table 23.11
- The CDC page gives totals with no breakdown by race, ethnicity, or sex, and no separate figure for type 2 diabetes. It links to a full report that we have not checked yet. Source: CDC National Diabetes Statistics Report
- Heart failure patient data: TBD. We have no confirmed source yet.

## Sneha: Trial diversity research and PPR method

### Trial diversity research sources

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| More than half of clinical trials do not report race/ethnicity data (ScienceDaily) | https://ScienceDaily.com/releases/2022/04/220410205932.htm | news | Evidence for our missing data feature | Woosik | 2026-11-05 |
| Participation of Older Adults in Clinical Trials for New Drug Applications and Biologics License Applications From 2010 Through 2019 (JAMA Network Open) | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2797323 | research | Background for PPR | Woosik | 2026-11-05 |
| Racial and Ethnic Diversity in Clinical Studies Reported to ClinicalTrials.gov, 2009 to 2024 (medRxiv) | https://www.medrxiv.org/content/10.1101/2025.07.21.25331865.full.pdf | research (preprint) | Broader context for trial diversity | Woosik | 2026-11-05 |

### PPR method sources

The JAMA Network Open paper listed under Trial diversity research sources defines PPR. See Key findings below.

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|

### Key findings: Trial diversity research

- Across more than 20,000 trials from March 2000 to March 2020, fewer than 44 percent reported any race or ethnicity data. Source: ScienceDaily
- Among the 8,871 trials in that study that reported race or ethnicity, White enrollment was 79.7 percent, compared with 72.4 percent of the US population. Source: ScienceDaily
- In 2024, 54.6 percent of studies reported both race and ethnicity, up from 7.4 percent in 2013, and 17.2 percent reported neither. Source: medRxiv preprint
- Observational studies were consistently less likely than interventional trials to report race, ethnicity, or both. Source: medRxiv preprint

### Key findings: PPR method

- PPR is a group's percentage among trial participants divided by its percentage in the US population with the condition. This paper applies it to age groups, not race. Source: JAMA Network Open
- The paper says a PPR between 0.8 and 1.2 has been suggested as a benchmark for adequate representativeness. Source: JAMA Network Open
- The paper reports a PPR of 0.20 for type 2 diabetes and 0.19 for heart failure in the oldest age group studied. Source: JAMA Network Open
