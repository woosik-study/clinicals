# Research Sources

This is our shared list of every source used for the project and the final site's resource list, which needs at least 10 sources.

Each team member adds their own research to their own section.

## How to add a source

1. Open `RESEARCH.md` on GitHub and click the pencil icon.
2. Go to your section and add a row to the Sources table. Add a line under Key findings if you found something we should use. Write TBD if you are not sure yet. For Published, use the date on the source. For a web page with no publication date, use its last updated date, or n.d. if it shows none.
3. Click **Commit changes**.

## Woosik

### Sources

#### Existing tools

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Drug Trials Snapshots | U.S. Food and Drug Administration | 2026-08-11 | https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots | official data | The existing tool we extend | Woosik | 2026-11-05 |
| FDA Releases 2024 Drug Trials Snapshots Summary Report | American Pharmaceutical Review | n.d. | https://www.americanpharmaceuticalreview.com/1315-News/620108-FDA-Releases-2024-Drug-Trials-Snapshots-Summary-Report/ | news | What Snapshots reports each year | Woosik | 2026-11-05 |

#### Trial diversity research

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| More than half of clinical trials do not report race/ethnicity data | ScienceDaily, from a Brigham and Women's Hospital release | 2022-04-10 | https://ScienceDaily.com/releases/2022/04/220410205932.htm | news | Evidence for our missing data feature | Woosik | 2026-11-05 |
| Participation of Older Adults in Clinical Trials for New Drug Applications and Biologics License Applications From 2010 Through 2019 | Lau SWJ, Huang Y, Hsieh J, et al. JAMA Network Open | 2022-10-14 | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2797323 | research | Background for PPR | Woosik | 2026-11-05 |
| Racial and Ethnic Diversity in Clinical Studies Reported to ClinicalTrials.gov, 2009-2024 | Aziz M, O'Brien EC, Lusk JB, et al. medRxiv | 2025-07-21 | https://www.medrxiv.org/content/10.1101/2025.07.21.25331865.full.pdf | research (preprint) | Broader context for trial diversity | Woosik | 2026-11-05 |

#### ClinicalTrials.gov data structure

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Results Data Element Definitions for Interventional and Observational Studies | ClinicalTrials.gov | 2024-12-31 | https://clinicaltrials.gov/policy/results-definitions | official guidance | How baseline characteristics are defined | Woosik | 2026-11-05 |
| Baseline Characteristics Template | ClinicalTrials.gov | 2017-04 | https://cdn.clinicaltrials.gov/documents/results_table_layout/DataEntryTable_BaselineRegionRaceEthnicityForm.pdf | official guidance | The NIH/OMB race categories our pipeline uses | Woosik | 2026-11-05 |

#### Prevalence data

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| SEER Cancer Statistics Review, 1975-2017, Table 23.11: Cancer of the Prostate (Invasive) | Howlader N, Noone AM, Krapcho M, et al. (eds). National Cancer Institute | 2020-04-15 | https://seer.cancer.gov/archive/csr/1975_2017/results_single/sect_23_table.11.pdf | official data | Checking how SEER reports cancer data by race | Woosik | 2026-11-05 |
| National Diabetes Statistics Report | Centers for Disease Control and Prevention | 2024-05-15, updated 2026-09-16 | https://www.cdc.gov/diabetes/php/data-research/index.html | official data | Checking how CDC reports diabetes data by race and sex | Woosik | 2026-11-05 |

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

#### Existing tools

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Drug Trials Snapshots | U.S. Food and Drug Administration | 2026-08-11 | https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots | official data | What Snapshots cover and how they are published | Sanjana | 2026-11-06 |
| Drug Trials Snapshots Summary Report (2015 and 2016) | U.S. Food and Drug Administration, Center for Drug Evaluation and Research | 2017-02-13 | https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots-summary-report-2015-and-2016 | official data | When Snapshots started and what they were for | Sanjana | 2026-11-06 |
| FDA report highlights need to improve diversity in clinical trials | Abigail Beaney, Clinical Trials Arena | 2024-05-16 | https://www.clinicaltrialsarena.com/news/fda-report-highlights-need-to-improve-diversity-in-clinical-trials/ | news | What the 2023 Snapshots summary report found | Sanjana | 2026-11-06 |
| ICER Clinical Trial Diversity Rating | Institute for Clinical and Economic Review (ICER) | n.d. | https://icer.org/our-approach/methods-process/icer-clinical-trial-diversity-rating/ | tool | Another tool that measures trial diversity | Sanjana | 2026-11-06 |
| A framework for evaluating the diversity of clinical trials | Agboola F, Wright AC. Journal of Clinical Epidemiology | 2024-05 | https://doi.org/10.1016/j.jclinepi.2024.111299 | research | How the CDR was designed | Sanjana | 2026-11-06 |
| GSK announces results from 17-year retrospective study on US clinical trial diversity | GSK | 2023-02-06 | https://us.gsk.com/en-us/media/press-releases/gsk-announces-results-from-17-year-retrospective-study-on-us-clinical-trial-diversity/ | press release | A drug company comparing its own trials with patient populations | Sanjana | 2026-11-06 |

#### Research that uses Snapshots data

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Longitudinal clinical trial enrollment trends across 341 US FDA-approved drugs and their guiding role in precision medicine strategies | Zaaijer S, Groen SC. Communications Medicine | 2025-12-05 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12680696/ | research | What Snapshots data can and cannot show | Sanjana | 2026-11-06 |

### Key findings

#### FDA Drug Trials Snapshots

- Snapshots cover only new molecular entities and original biologics approved by CDER, the FDA's drug center. They describe the key trials behind each drug's original approval. Source: FDA Drug Trials Snapshots
- CDER started publishing Snapshots in January 2015. Source: Drug Trials Snapshots Summary Report (2015 and 2016)
- Each Snapshot reports sex, race, ethnicity, and age, where the trials were run, and whether benefits or side effects differed between groups. Source: FDA Drug Trials Snapshots
- Snapshots come out within 30 days of approval and are not updated afterward. Source: FDA Drug Trials Snapshots
- Each Snapshot is a separate web page for one drug, and the FDA also publishes a yearly summary report as a PDF. The main page does not mention a downloadable dataset. Source: FDA Drug Trials Snapshots
- The main page does not compare participants with the people who have each disease. Source: FDA Drug Trials Snapshots
- The 2023 summary report covered 55 drugs and about 44,000 patients. Nine drug programs enrolled less than 10% Black patients, and 18 enrolled less than 10% Hispanic or Latino patients. Source: Clinical Trials Arena
- The article on the 2023 report says enrollment by race and ethnicity should be read alongside how common the disease is in each group. Source: Clinical Trials Arena

#### What researchers found when using Snapshots data

- A 2025 study used Snapshots for 341 Phase 3 trials behind drugs approved from 2017 to 2023. It excluded 12 Snapshot reports because they had no demographic data. Source: Communications Medicine
- The study compared participants with the US Census, not with the people who have each disease, and its authors say the Census is not always the right benchmark. Source: Communications Medicine
- Snapshots give only overall demographics, not the demographics of US sites. The median share of US participants fell from 47% in 2020 to 25% in 2023. Source: Communications Medicine
- Snapshot data reflect only what was known at approval and cover only approved drugs, so trials for drugs that were not approved are missing. Source: Communications Medicine

#### Other existing tools

- ICER's Clinical trial Diversity Rating is a framework that gives a trial an overall diversity rating. Users download a template after filling out a form. It rates trials, which our site does not do. Source: ICER CDR
- ICER's scoping review found that only 48% of the studies it reviewed used disease prevalence as the benchmark for diversity. Source: A framework for evaluating the diversity of clinical trials (ICER)
- GSK compared 495 of its own US trials (108,261 participants, 2002 to 2019) with both Census and disease data. In HIV trials, Black participants were 35.1% of enrollment, compared with 13.4% of the Census and 55.3% of people with HIV. The result depends on which benchmark is used. Source: GSK press release
- GSK's study covers only GSK's own trials and was published once, in 2023. It is not an ongoing tool. Source: GSK press release

#### How this compares with our site (draft for the Week 7 to 8 section)

| | FDA Snapshots | ICER CDR | GSK study | This site |
|---|---|---|---|---|
| Which trials | Key trials behind new drug approvals since 2015 | Any trial a user enters | GSK's own US trials, 2002 to 2019 | Interventional trials since 2010 with posted results on ClinicalTrials.gov, for 4 conditions |
| Unit | One drug | One trial | One company | One condition, filterable by phase |
| Compared with patients | No | Not stated on ICER's page (to check in the paper) | Yes, Census and disease data | Planned, with PPR |
| Shows missing race data | Not stated | Not stated | Not stated | Yes, share of trials that did not report race |
| Rates trials | No | Yes | No | No |
| Updated | Once, within 30 days of approval | Not applicable | Once | Manual data refresh |

"Not stated" means the source we read did not say. Check the full reports before putting these cells on the site.

## Saurabi

### Population Demographics

| Conditions | Time Range | Total Cases | Sources |
|---|---|---|---|
| Breast Cancer | 2019-2023 | 603016 | SEER Incidence Data |
| Prostate Cancer | 2019-2023 | 553816 | SEER Incidence Data |
| Type II Diabetes | | | |
| Heart Failure | | | |

| Conditions | Sex | Race/Ethnicity | Patient Percentage | Patient Count | Rate per 100,000 |
|---|---|---|---|---|---|
| Breast Cancer | F | White | 62.9591918 | 379654 | 141.3 |
| Breast Cancer | F | Black | 11.66254295 | 70327 | 132.4 |
| Breast Cancer | M | Black | 0.1333297956 | 804 | 2 |
| Breast Cancer | M | White | 0.5772649482 | 3481 | 1.3 |
| Breast Cancer | F | Hispanic | 15.50804622 | 93516 | 107.9 |
| Breast Cancer | M | Hispanic | 0.07959987795 | 480 | 0.7 |
| Breast Cancer | F | Asian | 8.615691789 | 51954 | 116.5 |
| Breast Cancer | M | Asian | 0.04162410284 | 251 | 0.7 |
| Breast Cancer | F | American Indian / Alaska Native | 0.3260278334 | 1966 | 199.4 |
| Prostate Cancer | M | White | 64.0707383 | 354834 | 122.2 |
| Prostate Cancer | M | Black | 16.34802895 | 90538 | 200.1 |
| Prostate Cancer | M | Hispanic | 11.77683563 | 65222 | 92.6 |
| Prostate Cancer | M | Asian | 4.676643506 | 25900 | 66.6 |
| Prostate Cancer | M | American Indian / Alaska Native | 0.2240816444 | 1241 | 86.7 |

### Sources

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| SEER Incidence Data, Breast Cancer, 2019 to 2023 (SEER*Explorer) | National Cancer Institute, Surveillance Research Program | [data release date] | https://seer.cancer.gov/statistics-network/explorer/ | official data | Breast cancer cases by sex and race for PPR | Saurabi | 2026-11-06 |
| SEER Incidence Data, Prostate Cancer, 2019 to 2023 (SEER*Explorer) | National Cancer Institute, Surveillance Research Program | [data release date] | https://seer.cancer.gov/statistics-network/explorer/ | official data | Prostate cancer cases by race for PPR | Saurabi | 2026-11-06 |

### Key findings

#### Prevalence data

- White patients make up the most cases of both cancers: 63.5 percent of breast cancer cases and 64.1 percent of prostate cancer cases. Source: SEER Incidence Data
- Black men are the most affected by prostate cancer, with a rate of 200.1 per 100,000. That is about 1.6 times the White rate (122.2) and 3 times the Asian rate (66.6). Source: SEER Incidence Data, Prostate Cancer
- American Indian/Alaska Native women have the highest breast cancer rate at 199.4 per 100,000, ahead of White (141.3) and Black (132.4) women, even though they are only 0.3 percent of cases. Source: SEER Incidence Data, Breast Cancer
- Hispanic and Asian women have the lowest breast cancer rates (107.9 and 116.5 per 100,000), but together they are still about 24 percent of cases. Source: SEER Incidence Data, Breast Cancer
- Men are 0.8 percent of breast cancer cases (5,016 of 603,016). Black men have the highest male rate at 2.0 per 100,000. Source: SEER Incidence Data, Breast Cancer

#### Trial representation compared with SEER

These compare our ClinicalTrials.gov data (`trials_clean.csv`, trials that report NIH/OMB race and only have US sites) with the SEER share of cases. Trial share divided by SEER share is a rough PPR.

- Asian patients are underrepresented in both cancers. They are 4.0 percent of US breast cancer trial participants against 8.7 percent of cases (PPR about 0.46), and 2.5 percent of US prostate cancer trial participants against 4.7 percent of cases (PPR about 0.53). Source: SEER Incidence Data; trials_clean.csv
- Black men are 14.9 percent of US prostate cancer trial participants against 16.3 percent of cases (PPR about 0.91). Across all trials, including non-US sites, they are only 10.0 percent (PPR about 0.61), so the group most affected by prostate cancer is underrepresented worldwide. Source: SEER Incidence Data; trials_clean.csv
- Black women are 17.4 percent of US breast cancer trial participants against 11.8 percent of cases (PPR about 1.47). Source: SEER Incidence Data; trials_clean.csv
- White patients are overrepresented in both: 76.6 percent of US breast cancer trial participants (PPR about 1.21) and 81.1 percent of US prostate cancer trial participants (PPR about 1.27). Source: SEER Incidence Data; trials_clean.csv
- These PPRs are rough. SEER counts Hispanic as its own group, while trials report Hispanic ethnicity separately from race, so trial White and Black shares include Hispanic patients and are inflated against SEER. Source: SEER Incidence Data; Race and ethnicity results table format

## Sneha

### Sources

#### Trial diversity research

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Racial and Ethnic Inequities in US Oncology Clinical Trial Participation From 2017 to 2022 | Pittell H, Calip GS, Pierre A, et al. JAMA Network Open | 2023-07-03 | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2807488 | research | Evidence of racial disparities in cancer trial participation | Sneha | 2026-11-06 |
| Examining the Representation of Minority Race and Ethnicity Groups in Breast Cancer Clinical Trials in the USA Published 2012-2022 | Dimaano K, Castillo O Jr, Moazzez A, et al. Annals of Surgical Oncology | 2026-02-23 | https://link.springer.com/article/10.1245/s10434-026-19214-y | research | Breast cancer representation and PPR comparisons | Sneha | 2026-11-06 |
| Improving Representation in Clinical Trials and Research: Building Research Equity for Women and Underrepresented Groups | National Academies of Sciences, Engineering, and Medicine | 2022 | https://www.nationalacademies.org/projects/PGA-POLICY-20-19/publication/26479 | research report | Barriers to participation and importance of diversity | Sneha | 2026-11-06 |
| FDASIA Section 907: Inclusion of Demographic Subgroups in Clinical Trials | U.S. Food and Drug Administration | 2018-03-28 | https://www.fda.gov/regulatory-information/food-and-drug-administration-safety-and-innovation-act-fdasia/fdasia-section-907-inclusion-demographic-subgroups-clinical-trials | official guidance | Why demographic representation matters | Sneha | 2026-11-06 |

#### PPR method

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Who Are We Missing? Reporting of Ethnicity, Race, and Sex-Specific Populations in Clinical Trials | Kohn R, Sheu D, Britez Ferrante E, et al. Journal of the American Heart Association | 2024-12-24 | https://pubmed.ncbi.nlm.nih.gov/39719416/ | research | PPR methodology and demographic underrepresentation | Sneha | 2026-11-06 |

#### Trial phases and data limitations

| Title | Author or organization | Published | Link | Type | Used for | Added by | Date added |
|---|---|---|---|---|---|---|---|
| Race and ethnicity reporting for clinical trials in ClinicalTrials.gov and publications | Fain KM, Nelson JT, Tse T, Williams RJ. Contemporary Clinical Trials | 2020-12-05 | https://pubmed.ncbi.nlm.nih.gov/33290865/ | research | Missing demographic data and reporting differences | Sneha | 2026-11-06 |
| Step 3: Clinical Research | U.S. Food and Drug Administration | 2018-01-04 | https://www.fda.gov/patients/drug-development-process/step-3-clinical-research | official guidance | Explaining clinical trial phases | Sneha | 2026-11-06 |
| ClinicalTrials.gov Glossary Terms | ClinicalTrials.gov | 2026-09-10 | https://clinicaltrials.gov/study-basics/glossary | official guidance | Phase definitions and terminology | Sneha | 2026-11-06 |
| How to Read Study Results | ClinicalTrials.gov | 2026-09-24 | https://clinicaltrials.gov/study-basics/how-to-read-study-results | official guidance | Results availability and baseline data limitations | Sneha | 2026-11-06 |

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
