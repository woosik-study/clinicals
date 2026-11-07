# Research Sources

This is our shared list of every source used for the project and the final site's resource list, which needs at least 10 sources.

Each team member adds their own research to their own section.

## How to add a source

1. Open `RESEARCH.md` on GitHub and click the pencil icon.
2. Go to your section and add a row to the Sources table. Add a line under Key findings if you found something we should use. Write TBD if you are not sure yet.
3. Click **Commit changes**.

## Woosik

### Sources

#### Existing tools

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| FDA Drug Trials Snapshots | https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots | official data | The existing tool we extend | Woosik | 2026-11-05 |
| FDA 2024 Drug Trials Snapshots Summary Report | https://www.americanpharmaceuticalreview.com/1315-News/620108-FDA-Releases-2024-Drug-Trials-Snapshots-Summary-Report/ | news | What Snapshots reports each year | Woosik | 2026-11-05 |

#### Trial diversity research

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| More than half of clinical trials do not report race/ethnicity data (ScienceDaily) | https://ScienceDaily.com/releases/2022/04/220410205932.htm | news | Evidence for our missing data feature | Woosik | 2026-11-05 |
| Participation of Older Adults in Clinical Trials for New Drug Applications and Biologics License Applications From 2010 Through 2019 (JAMA Network Open) | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2797323 | research | Background for PPR | Woosik | 2026-11-05 |
| Racial and Ethnic Diversity in Clinical Studies Reported to ClinicalTrials.gov, 2009 to 2024 (medRxiv) | https://www.medrxiv.org/content/10.1101/2025.07.21.25331865.full.pdf | research (preprint) | Broader context for trial diversity | Woosik | 2026-11-05 |

#### ClinicalTrials.gov data structure

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| Results data element definitions | https://prsinfo.clinicaltrials.gov/results_definitions.html | official guidance | How baseline characteristics are defined | Woosik | 2026-11-05 |
| Race and ethnicity results table format | https://cdn.clinicaltrials.gov/documents/results_table_layout/DataEntryTable_BaselineRegionRaceEthnicityForm.pdf | official guidance | The NIH/OMB race categories our pipeline uses | Woosik | 2026-11-05 |

#### Prevalence data

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| SEER Cancer Statistics Review 1975 to 2017, Table 23.11: Cancer of the Prostate (Invasive) | https://seer.cancer.gov/archive/csr/1975_2017/results_single/sect_23_table.11.pdf | official data | Checking how SEER reports cancer data by race | Woosik | 2026-11-05 |
| CDC National Diabetes Statistics Report | https://www.cdc.gov/diabetes/php/data-research/index.html | official data | Checking how CDC reports diabetes data by race and sex | Woosik | 2026-11-05 |

### Key findings

#### Existing tools

- Snapshots give concise information about who took part in the key clinical trials that supported the original FDA approval of new drugs. Source: FDA Drug Trials Snapshots
- The 2024 report covers 50 novel drugs and about 31,000 patients, broken down by sex, race, ethnicity, age group, and US participation. Source: FDA 2024 Drug Trials Snapshots Summary Report

#### Trial diversity research

- Across more than 20,000 trials from March 2000 to March 2020, fewer than 44 percent reported any race or ethnicity data. Source: ScienceDaily
- Among the 8,871 trials in that study that reported race or ethnicity, White enrollment was 79.7 percent, compared with 72.4 percent of the US population. Source: ScienceDaily
- In 2024, 54.6 percent of studies reported both race and ethnicity, up from 7.4 percent in 2013, and 17.2 percent reported neither. Source: medRxiv preprint
- Observational studies were consistently less likely than interventional trials to report race, ethnicity, or both. Source: medRxiv preprint

#### ClinicalTrials.gov data structure

- Race and ethnicity can be reported as Race (NIH/OMB), Ethnicity (NIH/OMB), Race/Ethnicity Customized, or Race and Ethnicity Not Collected. Source: Results data element definitions
- Required baseline measures include age, sex or gender, race, and ethnicity if it was collected under the protocol. Source: Results data element definitions
- The April 2017 template lists "Native Hawaiian or Pacific Islander", but our pipeline matches "Native Hawaiian or Other Pacific Islander". Source: Race and ethnicity results table format

#### Prevalence data

- The SEER table gives age adjusted incidence and mortality rates per 100,000 people, not counts or shares of patients. Source: SEER Table 23.11
- The SEER table uses White, White Hispanic, White Non Hispanic, Black, Asian/Pacific Islander, American Indian/Alaska Native, and Hispanic, which do not match our race categories one to one. Source: SEER Table 23.11
- The SEER table comes from an archived 1975 to 2017 edition and covers prostate cancer only. Source: SEER Table 23.11
- The CDC page gives totals with no breakdown by race, ethnicity, or sex, and no separate figure for type 2 diabetes. It links to a full report that we have not checked yet. Source: CDC National Diabetes Statistics Report

#### PPR method

- PPR is a group's percentage among trial participants divided by its percentage in the US population with the condition. This paper applies it to age groups, not race. Source: JAMA Network Open
- The paper says a PPR between 0.8 and 1.2 has been suggested as a benchmark for adequate representativeness. Source: JAMA Network Open
- The paper reports a PPR of 0.20 for type 2 diabetes and 0.19 for heart failure in the oldest age group studied. Source: JAMA Network Open

## Sanjana

### Sources

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|

### Key findings

## Saurabi

### Sources

#### Prevalence data

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| SEER Incidence Data, Breast Cancer, 2019 to 2023 (SEER*Explorer) | https://seer.cancer.gov/statistics-network/explorer/ | official data | Breast cancer cases by sex and race for PPR | Saurabi | 2026-11-06 |
| SEER Incidence Data, Prostate Cancer, 2019 to 2023 (SEER*Explorer) | https://seer.cancer.gov/statistics-network/explorer/ | official data | Prostate cancer cases by race for PPR | Saurabi | 2026-11-06 |

### Key findings

#### Prevalence data

- SEER reports 603,016 breast cancer cases from 2019 to 2023. Source: SEER Incidence Data, Breast Cancer
- By share of breast cancer cases: White women 63.0 percent (379,654 cases, 141.3 per 100,000), Hispanic women 15.5 percent (93,516, 107.9 per 100,000), Black women 11.7 percent (70,327, 132.4 per 100,000), Asian women 8.6 percent (51,954, 116.5 per 100,000), and American Indian/Alaska Native women 0.3 percent (1,966, 199.4 per 100,000). Source: SEER Incidence Data, Breast Cancer
- Men make up under 1 percent of breast cancer cases: White men 0.6 percent (3,481 cases, 1.3 per 100,000), Black men 0.1 percent (804, 2.0 per 100,000), Hispanic men 0.1 percent (480, 0.7 per 100,000), and Asian men under 0.1 percent (251, 0.7 per 100,000). Source: SEER Incidence Data, Breast Cancer
- American Indian/Alaska Native women have the highest breast cancer rate in this data at 199.4 per 100,000, even though they are only 0.3 percent of cases. Source: SEER Incidence Data, Breast Cancer
- SEER reports 553,816 prostate cancer cases from 2019 to 2023. Source: SEER Incidence Data, Prostate Cancer
- By share of prostate cancer cases: White 64.1 percent (354,834 cases, 122.2 per 100,000), Black 16.3 percent (90,538, 200.1 per 100,000), Hispanic 11.8 percent (65,222, 92.6 per 100,000), Asian 4.7 percent (25,900, 66.6 per 100,000), and American Indian/Alaska Native 0.2 percent (1,241, 86.7 per 100,000). Source: SEER Incidence Data, Prostate Cancer
- Black men have the highest prostate cancer rate at 200.1 per 100,000, well above White men at 122.2. Source: SEER Incidence Data, Prostate Cancer
- The race groups listed cover about 99.9 percent of breast cancer cases and about 97.1 percent of prostate cancer cases, so the rest are other or unknown races. Source: SEER Incidence Data
- Type 2 diabetes and heart failure: TBD


## Sneha

### Sources

#### Trial diversity research

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| Racial and Ethnic Inequities in US Oncology Clinical Trial Participation From 2017 to 2022 (JAMA Network Open) | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2807488 | research | Evidence of racial disparities in cancer trial participation | Sneha | 2026-11-06 |
| Examining the Representation of Minority Race and Ethnicity Groups in Breast Cancer Clinical Trials in the USA Published 2012–2022 | https://link.springer.com/article/10.1245/s10434-026-19214-y | research | Breast cancer representation and PPR comparisons | Sneha | 2026-11-06 |
| Improving Representation in Clinical Trials and Research (National Academies, 2022) | https://www.nationalacademies.org/projects/PGA-POLICY-20-19/publication/26479 | research report | Barriers to participation and importance of diversity | Sneha | 2026-11-06 |
| FDASIA Section 907: Inclusion of Demographic Subgroups in Clinical Trials (FDA) | https://www.fda.gov/regulatory-information/food-and-drug-administration-safety-and-innovation-act-fdasia/fdasia-section-907-inclusion-demographic-subgroups-clinical-trials | official guidance | Why demographic representation matters | Sneha | 2026-11-06 |

#### PPR method

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| Who Are We Missing? Reporting of Ethnicity, Race, and Sex-Specific Populations in Clinical Trials | https://pubmed.ncbi.nlm.nih.gov/39719416/ | research | PPR methodology and demographic underrepresentation | Sneha | 2026-11-06 |

#### Trial phases and data limitations

| Title | Link | Type | Used for | Added by | Date |
|---|---|---|---|---|---|
| Race and Ethnicity Reporting for Clinical Trials in ClinicalTrials.gov and Publications | https://pubmed.ncbi.nlm.nih.gov/33290865/ | research | Missing demographic data and reporting differences | Sneha | 2026-11-06 |
| Step 3: Clinical Research (FDA) | https://www.fda.gov/patients/drug-development-process/step-3-clinical-research | official guidance | Explaining clinical trial phases | Sneha | 2026-11-06 |
| ClinicalTrials.gov Glossary | https://clinicaltrials.gov/study-basics/glossary | official guidance | Phase definitions and terminology | Sneha | 2026-11-06 |
| How to Read Study Results (ClinicalTrials.gov) | https://clinicaltrials.gov/study-basics/how-to-read-study-results | official guidance | Results availability and baseline data limitations | Sneha | 2026-11-06 |

### Key findings

#### Trial diversity research

- Clinical trials should include participants who reflect the populations likely to use the treatments being studied. Representation matters because researchers need to understand treatment safety and effectiveness across different patient groups. Source: FDA Section 907.
- A 2023 JAMA Network Open study examined 50,411 patients across five cancer types. Trial participation was lower among Black patients (4.4%) and Latinx patients (4.2%) than White patients (7.2%). Source: JAMA Network Open, 2023.
- A study of 1,068 US breast cancer trials published from 2012 to 2022 found that 73.5% reported race or ethnicity. Among trials reporting these data, only 5.7% achieved a PPR above 0.8 simultaneously for Asian, Black, and Hispanic participants. Source: Breast Cancer Clinical Trials study, 2026.
- Barriers to diverse participation include restrictive eligibility requirements, limited research site accessibility, transportation costs, financial burdens, and recruitment practices. Source: National Academies, 2022.
- Comparing trial enrollment to disease prevalence provides more meaningful context than displaying raw demographic percentages alone. Source: Who Are We Missing?, 2025.

#### PPR method

- PPR stands for Participation-to-Prevalence Ratio. It measures how closely a demographic group's representation in clinical trials matches its representation among people who have the condition being studied. Source: Who Are We Missing?, 2025.
- PPR = (% of trial participants in a demographic group) / (% of people with the condition in that demographic group).
- A PPR of 1.0 indicates proportional representation. Below 1.0 indicates underrepresentation, while above 1.0 indicates overrepresentation.
- Researchers commonly use a PPR range of 0.8 to 1.2 as a suggested benchmark for approximately proportional representation. Source: Who Are We Missing?, 2025.
- Example: If Black patients make up 20% of trial participants but 40% of people with the disease, the PPR is 0.20 / 0.40 = 0.50, suggesting underrepresentation.
- A 2025 cardiovascular trial analysis calculated 22 PPR values across demographic groups and conditions. Nineteen were below 0.8, suggesting underrepresentation in those comparisons. Source: Who Are We Missing?, 2025.
- PPR is more informative than comparing trial enrollment to the entire US population because diseases affect demographic groups at different rates.

#### Clinical trial phases

- Phase 1 primarily evaluates safety, dosage, and how a treatment interacts with the body, generally in smaller groups. Source: FDA Step 3.
- Phase 2 investigates whether a treatment appears effective for a particular condition while continuing to evaluate safety. Source: FDA Step 3.
- Phase 3 studies safety and effectiveness in larger populations and provides stronger evidence about treatment benefits and risks. Source: FDA Step 3.
- Phase 4 takes place after approval and examines additional information about a treatment's safety, effectiveness, or optimal use. Source: FDA Step 3.
- Some studies are classified as "Not Applicable" because FDA-defined drug trial phases do not apply to them, such as certain behavioral or device studies. Source: ClinicalTrials.gov Glossary.

#### Data limitations

- Not all registered trials have posted results, and not every trial reports complete race, ethnicity, sex, or age information. Source: ClinicalTrials.gov, How to Read Study Results.
- Missing demographic data does not necessarily indicate that a demographic group was excluded. Data may not have been collected or may not have been reported. Source: Race and Ethnicity Reporting for Clinical Trials.
- Race and ethnicity categories are not always consistent between trial datasets and disease prevalence datasets, making some comparisons difficult.
- PPR calculations require comparable disease prevalence data for the same demographic categories and geographic population. Missing information may prevent reliable calculations.
- A low PPR indicates underrepresentation relative to disease prevalence, but it does not independently establish whether a trial is safe, effective, or fair.
- Our dashboard should distinguish between underrepresentation and missing information by displaying "Insufficient data" when reliable comparisons cannot be calculated.
- Transparent reporting of missing demographic information is important so users do not mistake incomplete data for complete representation.

### Draft website explainer text

#### What are clinical trial phases?

Clinical trials evaluate medical treatments in people to understand their safety and effectiveness.

- **Phase 1:** Tests safety and dosage.
- **Phase 2:** Evaluates preliminary effectiveness and continues safety testing.
- **Phase 3:** Studies safety and effectiveness in larger patient populations.
- **Phase 4:** Monitors treatments after approval.

Each phase serves a different purpose, and demographic representation can vary across phases.

Source: FDA Step 3: Clinical Research.

#### What is PPR?

The Participation-to-Prevalence Ratio (PPR) measures whether a demographic group's participation in clinical trials is proportional to its share of the population affected by a disease.

- **Below 0.8:** Suggests underrepresentation.
- **0.8–1.2:** Approximately proportional representation.
- **Above 1.2:** Suggests overrepresentation.

For example, if a group represents 10% of trial participants but 20% of people living with the disease, its PPR is 0.5.

PPR helps identify possible representation gaps but is not a complete measure of trial quality.

Source: Who Are We Missing?, 2025.

#### Understanding data limitations

Our dashboard uses publicly available clinical trial information to examine demographic representation across medical conditions.

However, not every trial reports complete demographic information. Differences in how studies collect and report race, ethnicity, age, and sex can make comparisons difficult.

We aim to make these limitations visible and distinguish missing information from actual underrepresentation. When reliable comparisons are unavailable, the dashboard will indicate insufficient data rather than present potentially misleading results.

Source: ClinicalTrials.gov, How to Read Study Results.
