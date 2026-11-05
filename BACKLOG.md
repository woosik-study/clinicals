# Clinicals: Project Backlog and Work Log

**Project:** Who Is in the Trial? Exploring Demographic Representation in Clinical Trials
**Team:** Woosik Kim, Sanjana, Saurabi, Sneha
**Live site:** https://woosik-study.github.io/clinicals
**Repo:** https://github.com/woosik-study/clinicals
**Sources:** [RESEARCH.md](RESEARCH.md)
**Data snapshot:** pulled 11/4/2026. The site does not update itself. New data needs a manual re-run (see section 3).

This file tracks what we have done, how we did it, and what is left. Update it whenever a task moves. It is the source for our final presentation.

---

## 1. Status board

**Roles**
- **Woosik:** trial data and charts
- **Saurabi:** prevalence data and resource list
- **Sanjana:** site structure and existing tools comparison
- **Sneha:** research and explainers

| Task | Owner | Planned | Status | Notes |
|---|---|---|---|---|
| Submit 2 missed progress updates | All | Week 6 | ✅ Done 11/4 | |
| Submit this week's progress update | All | Week 6 | ❌ Not started | Gantt charts are ready (Woosik) |
| Confirm 4 conditions | All | Week 6 | ❌ Not started | Alzheimer's is an optional 5th |
| Tell the group if your research part is done | All | Week 6 | ❌ Not started | |
| Weekly progress update | All | Every week | 🔁 Ongoing | |
| Abstract | All | Week 3 | ✅ Done | Submitted 10/16 |
| Group charter | All | Week 3 to 4 | ✅ Done | |
| Research: ClinicalTrials.gov API and data fields | Woosik | Week 4 to 5 | ✅ Done | Used to build the data pipeline |
| Research: FDA Snapshots and existing tools | Sanjana | Week 4 to 5 | ❓ Confirm | |
| Research: Disease prevalence data (CDC, NCI) | Saurabi | Week 4 to 5 | ❓ Confirm | |
| Research: Trial diversity studies and PPR | Sneha | Finish Week 6 | ❓ Confirm | |
| Pick conditions | All | Week 5 to 6 | ✅ Proposed | Breast cancer, prostate cancer, type 2 diabetes, heart failure. Team to confirm (see above). |
| Pull and clean trial demographic data | Woosik | Week 5 to 6 | ✅ Done 11/4 | 4,494 rows, 4,415 unique trials |
| Count trials that did not report race | Woosik | Week 6 | ✅ Done 11/4 | Breast 304, prostate 169, type 2 diabetes 507, heart failure 170 (1,140 unique trials) |
| Fix "Race and Ethnicity Not Collected" label bug | Woosik | Week 6 | ✅ Done 11/4 | 261 rows moved from own categories to not reported |
| Add trial locations to the data pull | Woosik | Before PPR charts | ✅ Done 11/4 | `us_only` and `any_us_site` flags filled by a full data pull. Other numbers did not change. |
| Decide if there are enough `us_only` trials for PPR | All | Week 6 to 7 | ❌ Not started | Counts are in section 4 |
| Build charts and filters | Woosik | Week 7 to 8 | ✅ First version 11/4 | Ahead of schedule. PPR charts still to do. Age and ethnicity are not on the site yet. |
| Host site on GitHub Pages | Woosik | Week 6 | ✅ Done 11/4 | |
| Site pages and wireframe (rough layout) | Sanjana | Week 6 | ⚠️ Partial | For example Home, condition pages, explainers, sources. Basic structure exists in the prototype. |
| Collect patient demographics per condition | Saurabi | Week 6 | ❌ Not started | **Blocking PPR charts.** NCI SEER for the cancers, CDC for diabetes and heart failure. Match the trial data's race and sex categories. |
| Resource list (10+ sources) | Saurabi | Through Week 9 | ⚠️ Started | Track every source we use in [RESEARCH.md](RESEARCH.md) |
| FDA Snapshots comparison section | Sanjana | Week 7 to 8 | ❌ Not started | |
| Explainer text (phases, PPR, data limits) | Sneha | Week 7 to 8 | ⚠️ Placeholder | Short placeholder text on the site. Sneha to rewrite and expand. |
| PPR charts | Woosik | Week 7 to 8 | ❌ Not started | Needs prevalence data. Follow the rules in section 5. |
| Team review and edits | All | Week 9 | ❌ | |
| Final polish, submission, AI chat logs | All | Week 10 to Finals | ❌ | |

---

## 2. Work log

### Week 3 (10/12 to 10/16)
- Each member pitched a topic idea. Team chose clinical trial representation.
- Checked for existing tools. FDA Drug Trials Snapshots already shows participant demographics for newly approved drugs, so we justified our project under **added depth**: comparing participants with real patient populations (PPR), showing how often demographic data is missing, and covering trials beyond FDA approved drugs.
- Submitted the abstract and group charter.

### Week 4 (10/19 to 10/23)
- Split research into 4 parts (see status board).
- Made the baseline Gantt chart through Finals Week.
- **Missed:** the progress update was not submitted. Each of us thought another member had submitted it.

### Week 5 (10/26 to 10/30)
- Extended the research phase through the end of Week 5.
- **Missed:** the progress update was not submitted for the same reason.

### Week 6 (11/2 to 11/6)
- 11/4: TA (Uliyaah) flagged the missing Week 5 and Week 6 updates. We confirmed it was a miscommunication and are submitting them.
- 11/4: The 2 missed progress updates were handled.
- 11/4: Proposed 4 conditions to focus on.
- 11/4: Built and ran the data pipeline (4,494 trials).
- 11/4: Built the working prototype and published it on GitHub Pages.
- 11/4: Created this backlog.
- 11/4: Checked the backlog numbers against the raw data and found a race label bug. ClinicalTrials.gov lists "Race and Ethnicity Not Collected" as a baseline measure, and the script counted those 261 rows as own categories. Fixed it, rebuilt the data from the saved raw files, and changed the banner from "live" to the snapshot date.
- 11/4: Set roles and this week's tasks for all 4 members, and agreed how to compare trial and patient data (see section 3).
- 11/4: Team decided on overlapping trials, US vs global data, unknown race, and neutral wording (see section 5). Implemented the site and script changes.
- 11/4: Ran a full data pull with trial locations and counted the trials and participants available for PPR (see section 4).

---

## 3. How the data pipeline works

**Step 1: Pull data (`fetch_trials.py`)**
- ClinicalTrials.gov has an **API**, a way for a program to request data from the site automatically.
- Filters: one of the 4 conditions, **interventional** trials (testing a treatment), started 2010 or later, with **posted results**.
- Each trial's location countries are requested too.
- Raw responses are saved in `trials_raw/`, one JSONL file per condition.

**Step 2: Clean data (same script)**
- Each trial reports **baseline characteristics**, a table of who enrolled with a "Total" column.
- From the Total column we take sex, race (standard NIH/OMB categories), ethnicity, and average age.
- Each trial's race reporting is labeled **standard categories**, **own categories** (custom labels the script does not try to combine), or **not reported**.
- Each trial gets two location flags: **`us_only`** (all sites in the US) and **`any_us_site`** (at least one US site). Both are blank if the trial lists no location.
- Output: `trials_clean.csv` (one row per trial per condition) and `summary_by_condition.csv`.

**Step 3: Prepare for the site (`build_site_data.py`)**
- Converts the CSV into `docs/data.js`, which the web page loads.

**Step 4: Website (`docs/`)**
- `index.html` (structure), `style.css` (look), `app.js` (filters and recalculation in the browser).
- The site shows sex and race. Ethnicity and age are in the CSV only.

**Step 5: Publish**
- **GitHub Pages** serves the `docs/` folder as a public site and updates on every push.

**To refresh the data:**
```bash
python3 fetch_trials.py
python3 build_site_data.py
git add . && git commit -m "Refresh data" && git push
```

To change only the cleaning logic, run `python3 fetch_trials.py --from-raw` in place of the first command. It rebuilds the CSVs from `trials_raw/` without downloading anything. The script also prints trial counts per condition for each location flag and saves them in `summary_by_condition.csv`.

**How we compare the data**

For each condition we show two numbers side by side:
1. A group's share of trial participants (Woosik's data)
2. That group's share of actual patients (Saurabi's data)

PPR = (1) divided by (2). A value below 1 is what we mean by underrepresented. The site defines that term once in the explainer and does not label individual groups.

For PPR, (1) uses only `us_only` trials with standard race categories and leaves "Unknown or Not Reported" out of the denominator.

Example with made-up numbers: if a group is 10% of trial participants and 20% of patients, its PPR is 0.5.

---

## 4. Key findings so far

| Condition | Trials | Participants | Reported race at all | Standard categories | Own categories | Not reported | Female participants |
|---|---|---|---|---|---|---|---|
| Breast cancer | 1,534 | 383,508 | 80.2% | 60.1% | 20.1% | 19.8% | 95.9% |
| Prostate cancer | 872 | 121,579 | 80.6% | 64.3% | 16.3% | 19.4% | 6.3% |
| Type 2 diabetes | 1,417 | 698,473 | 64.2% | 43.4% | 20.8% | 35.8% | 42.8% |
| Heart failure | 671 | 419,286 | 74.7% | 53.8% | 20.9% | 25.3% | 41.5% |

Each row counts its own condition, so overlapping trials count in each one. We deduplicate only for totals across conditions. Across all 4 conditions there are 4,415 unique trials and 1,596,387 participants.

Participant race, from trials in any country using standard categories. Race shares are among participants with known race. The unknown column is a share of all participants in those trials. AI/AN means American Indian or Alaska Native. Race shares do not sum to 100% because Native Hawaiian or Other Pacific Islander and More than one race are not shown here.

| Condition | White | Black | Asian | AI/AN | Unknown race |
|---|---|---|---|---|---|
| Breast cancer | 75.0% | 11.5% | 11.5% | 1.1% | 5.7% |
| Prostate cancer | 79.9% | 10.0% | 8.6% | 0.6% | 5.1% |
| Type 2 diabetes | 70.6% | 8.2% | 15.9% | 2.9% | 2.0% |
| Heart failure | 78.4% | 11.0% | 7.4% | 1.2% | 1.8% |

These are trial participant shares only. They become meaningful once compared with patient prevalence through PPR (Participation to Prevalence Ratio: a group's share of trial participants divided by its share of people with the condition).

**Trials and participants available for PPR.** PPR will use `us_only` trials (all sites in the US) with standard race categories. `any_us_site` means at least one US site.

| Condition | All trials | With locations | `us_only` | `any_us_site` | Usable for PPR | Participants with known race | Share of those participants in the 10 largest trials |
|---|---|---|---|---|---|---|---|
| Breast cancer | 1,534 | 1,506 | 965 | 1,275 | 677 | 85,512 | 46.4% |
| Prostate cancer | 872 | 862 | 624 | 772 | 455 | 28,509 | 23.7% |
| Type 2 diabetes | 1,417 | 1,325 | 596 | 947 | 333 | 51,486 | 51.3% |
| Heart failure | 671 | 668 | 397 | 527 | 247 | 39,548 | 43.2% |
| All (unique trials) | 4,415 | 4,285 | 2,535 | 3,450 | 1,679 | | |

Participants in those usable trials, by race. These counts are not PPR values and do not show representation until compared with patient data. NHPI means Native Hawaiian or Other Pacific Islander.

| Condition | White | Black | Asian | AI/AN | NHPI | More than one race |
|---|---|---|---|---|---|---|
| Breast cancer | 65,481 | 14,853 | 3,433 | 864 | 139 | 742 |
| Prostate cancer | 23,131 | 4,242 | 718 | 149 | 69 | 200 |
| Type 2 diabetes | 35,220 | 12,329 | 1,469 | 902 | 493 | 1,073 |
| Heart failure | 27,780 | 9,502 | 927 | 388 | 161 | 790 |

A few large trials carry a lot of weight in these totals. The 10 largest trials hold 50.5% of heart failure participants, 33.6% for breast cancer, 24.9% for type 2 diabetes, and 14.1% for prostate cancer. The median trial is small (44 to 114 participants).

---

## 5. Open issues and decisions

**Decisions made (11/4)**
- **Overlapping trials:** keep trials listed under multiple conditions in each condition's stats. The trial table shows "Also listed under: [condition]", and the data limits explainer says so. Deduplicate only when computing cross-condition totals. For context, 79 trials appear under two conditions (56 of them under both breast and prostate cancer). Those 56 trials hold 5,551 of the 7,587 female participants in prostate cancer. Without them the female share is 1.8%, not 6.3%.
- **US vs global:** participant charts stay global. `fetch_trials.py` adds location countries and the `us_only` and `any_us_site` flags. PPR will use `us_only` trials.
- **Unknown race:** exclude "Unknown or Not Reported" from the denominator for race shares used in PPR. The site shows the unknown share separately, as "X% of participants had unknown race". The site's race chart now uses the same denominator, so its shares match the shares PPR will use.
- **Neutral wording:** "Is demographic data even reported?" is now "How often do trials report participants' race?". Individual groups are not labeled as underrepresented. PPR charts will show each value with a reference line at 1.0, and the explainer defines the term once.

**Next step on these decisions**
- **Are there enough `us_only` trials?** Counts are in section 4. Decide on a rule for small groups before seeing any PPR values. Keeping only `us_only` trials leaves 18.8% of type 2 diabetes participants with known race, 25.6% for heart failure, 45.3% for prostate cancer, and 53.8% for breast cancer, compared with the global totals.
- **Small groups:** the smallest counts are NHPI in prostate cancer (69), breast cancer (139), and heart failure (161), and AI/AN in prostate cancer (149). In some cases one trial supplies most of a group: NCT03270436 holds 76.7% of NHPI participants in type 2 diabetes, and NCT04259762 holds 55.7% of AI/AN participants in breast cancer. Decide whether the site should flag values like these.

**Site wording**
- **Intro text:** the intro says trials "leave out demographic data entirely", but the chart only measures race.

**Decisions for the team**
- **Broad search:** the condition search also returns trials that are not mainly about that condition. Decide whether to narrow it.
- **Own race categories:** about 1 in 5 trials use their own race labels and are excluded from the race chart. Explain this on the site. Many of these labels look close to the standard ones (Asian, White), so decide whether to map the clear matches.
- **PPR inputs (Woosik and Saurabi):** agree on these before Saurabi collects the data:
  - **Shares, not rates:** PPR needs each group's share of patients. A rate such as "cases per 100,000 people" in that group is not a share. Record patient counts where possible.
  - **Patient measure:** choose prevalence (people living with the condition) or incidence (new cases), and use the same one across conditions if possible.
  - **Race categories:** a source may combine groups (Asian/Pacific Islander) or mix race with Hispanic origin (White Non-Hispanic). The trial data keeps race and ethnicity separate, so write down how each category maps.
  - **Diabetes type:** our trials cover type 2. Check whether each CDC figure separates type 2 from all diabetes.
  - **Heart failure source:** confirm that CDC publishes heart failure patients by race and sex. If not, choose another source.
- **Age and ethnicity:** our topic includes both, but neither is on the site. About 1 in 5 unique trials has no usable average age (827 of 4,415), and the "average" mixes means and medians.
- **Condition list:** confirm the 4 conditions as a team, or add Alzheimer's disease.

**Smaller data checks**
- **Phase filter:** 1,243 unique trials (28%) appear only under "All phases" because they have no phase, or are Early Phase 1. Combined phases such as Phase 1/2 count under both phases.
- **Race totals:** in 41 rows the race total differs from the baseline participant count, 9 of them with a race total of 0. Not yet examined. 4 trials have two standard race tables and the script keeps only the last.
- **No Total group:** 3 trials have no group the script can identify as "Total", so their demographics are blank.
- **Unusual labels:** a few standard race tables use variant labels the script does not match, such as "Multiracial or other". Measures titled only "Ethnicity" (16) are skipped.

**Process**
- **Research tasks:** Sanjana, Saurabi, and Sneha to confirm status on the board.

---

## 6. AI tool usage

The course requires us to submit AI conversations with the final deliverables. Log each use here.

| Date | Member | Tool | Used for |
|---|---|---|---|
| 10/15 to 10/16 | Woosik | Claude | Topic brainstorming, checking existing tools, abstract drafting |
| 10/15 | Woosik | Claude | Group charter draft |
| 10/23 to 10/29 | Woosik | Claude | Gantt charts and progress update text |
| 11/4 | Woosik | Claude | Data pipeline scripts, prototype website, this backlog |
| 11/4 | Woosik | Claude | Checking code and backlog numbers against the raw data, plain-language project summary, backlog update |
| 11/4 | Woosik | Claude | README draft, implementing team decisions on overlapping trials, trial locations, unknown race, and wording |
| 11/5 | Woosik | Claude | RESEARCH.md draft and reading the seeded sources for key findings |

---

## 7. Presentation outline (draft)

1. The problem: who is missing from clinical trials and why it matters
2. What already exists (FDA Snapshots) and what we add
3. Our data: source, filters, and how we cleaned it
4. Live demo of the site: condition tabs, phase filter, charts, trial table
5. Key findings: reporting gaps and participant demographics (plus PPR once added), shown without rating any trial
6. Limits of the data: posted results only, excluded race labels, overlapping trials, large trials dominating totals, US categories in global trials
7. What we learned, including the label bug we caught and how AI tools were used and checked
8. How the site stays public after the quarter

Speakers: to be decided as a team.
