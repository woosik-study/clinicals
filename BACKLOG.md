# Clinicals: Project Backlog and Work Log

**Project:** Who Is in the Trial? Exploring Demographic Representation in Clinical Trials
**Team:** Woosik Kim, Sanjana, Saurabi, Sneha
**Live site:** https://woosik-study.github.io/clinicals
**Repo:** https://github.com/woosik-study/clinicals

This file tracks what we have done, how we did it, and what is left. Update it whenever a task moves. It is the source for our final presentation.

---

## 1. Status board

| Task | Owner | Planned | Status | Notes |
|---|---|---|---|---|
| Abstract | All | Week 3 | ✅ Done | Submitted 10/16 |
| Group charter | All | Week 3 to 4 | ✅ Done | |
| Research: ClinicalTrials.gov API and data fields | Woosik | Week 4 to 5 | ✅ Done | Used to build the data pipeline |
| Research: FDA Snapshots and existing tools | Sanjana | Week 4 to 5 | ❓ Confirm | |
| Research: Disease prevalence data (CDC, NCI) | Saurabi | Week 4 to 5 | ❓ Confirm | |
| Research: Trial diversity studies and PPR | Sneha | Week 4 to 5 | ❓ Confirm | |
| Pick conditions | All | Week 5 to 6 | ✅ Proposed | Breast cancer, prostate cancer, type 2 diabetes, heart failure. Team to confirm. |
| Pull and clean trial demographic data | Woosik | Week 5 to 6 | ✅ Done 11/4 | 4,494 trials |
| Build charts and filters | Woosik | Week 7 to 8 | ✅ First version 11/4 | Ahead of schedule. PPR charts still to do. |
| Host site on GitHub Pages | Woosik | Week 6 | ✅ Done 11/4 | |
| Site structure and wireframe | Sanjana | Week 5 to 6 | ⚠️ Partial | Basic structure exists in the prototype. Sanjana to review and refine. |
| Collect prevalence data per condition | Saurabi | Week 5 to 6 | ❌ Not started | **Blocking PPR charts** |
| Resource list (10+ sources) | Saurabi | Week 5 to 9 | ❌ Not started | |
| FDA Snapshots comparison section | Sanjana | Week 7 to 8 | ❌ Not started | |
| Explainer text (phases, PPR, data limits) | Sneha | Week 7 to 8 | ⚠️ Placeholder | Short placeholder text on the site. Sneha to rewrite and expand. |
| PPR charts | Woosik | Week 7 to 8 | ❌ Not started | Needs prevalence data |
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
- 11/4: Proposed 4 conditions to focus on.
- 11/4: Built and ran the data pipeline (4,494 trials).
- 11/4: Built the working prototype and published it on GitHub Pages.
- 11/4: Created this backlog.

---

## 3. How the data pipeline works

**Step 1: Pull data (`fetch_trials.py`)**
- ClinicalTrials.gov has an **API**, a way for a program to request data from the site automatically.
- Filters: one of the 4 conditions, **interventional** trials (testing a treatment), started 2010 or later, with **posted results**.
- Raw responses are saved in `trials_raw/`, one JSONL file per condition.

**Step 2: Clean data (same script)**
- Each trial reports **baseline characteristics**, a table of who enrolled with a "Total" column.
- From the Total column we take sex, race (standard NIH/OMB categories), ethnicity, and average age.
- Each trial's race reporting is labeled **standard categories**, **own categories** (custom labels that cannot be combined), or **not reported**.
- Output: `trials_clean.csv` (one row per trial) and `summary_by_condition.csv`.

**Step 3: Prepare for the site (`build_site_data.py`)**
- Converts the CSV into `docs/data.js`, which the web page loads.

**Step 4: Website (`docs/`)**
- `index.html` (structure), `style.css` (look), `app.js` (filters and recalculation in the browser).

**Step 5: Publish**
- **GitHub Pages** serves the `docs/` folder as a public site and updates on every push.

**To refresh the data:**
```bash
python3 fetch_trials.py
python3 build_site_data.py
git add . && git commit -m "Refresh data" && git push
```

---

## 4. Key findings so far

| Condition | Trials | Reported race at all | Standard race categories | Female participants |
|---|---|---|---|---|
| Breast cancer | 1,534 | 86.0% | 60.1% | 95.9% |
| Prostate cancer | 872 | 86.4% | 64.3% | 6.3% |
| Type 2 diabetes | 1,417 | 69.6% | 43.4% | 42.8% |
| Heart failure | 671 | 81.5% | 53.8% | 41.5% |

Participant race (trials using standard categories):

| Condition | White | Black | Asian | AI/AN | Unknown |
|---|---|---|---|---|---|
| Breast cancer | 70.7% | 10.8% | 10.9% | 1.0% | 5.7% |
| Prostate cancer | 75.8% | 9.5% | 8.2% | 0.6% | 5.1% |
| Type 2 diabetes | 69.1% | 8.0% | 15.6% | 2.9% | 2.0% |
| Heart failure | 77.0% | 10.8% | 7.3% | 1.2% | 1.8% |

These are trial participant shares only. They become meaningful once compared with patient prevalence (PPR).

---

## 5. Open issues and decisions

- **Overlapping trials:** 79 trials appear under two conditions (for example, trials that study breast and prostate cancer together). This explains the 6% female share in prostate cancer. Decide whether to keep, remove, or flag them.
- **Custom race categories:** about a quarter of trials use their own race labels and are excluded from the race chart. Explain this on the site.
- **Progress updates:** confirm with the TA whether one member or every member submits each week.
- **Condition list:** confirm the 4 conditions as a team, or add Alzheimer's disease.

---

## 6. AI tool usage

The course requires us to submit AI conversations with the final deliverables. Log each use here.

| Date | Member | Tool | Used for |
|---|---|---|---|
| 10/15 to 10/16 | Woosik | Claude | Topic brainstorming, checking existing tools, abstract drafting |
| 10/15 | Woosik | Claude | Group charter draft |
| 10/23 to 10/29 | Woosik | Claude | Gantt charts and progress update text |
| 11/4 | Woosik | Claude | Data pipeline scripts, prototype website, this backlog |

---

## 7. Presentation outline (draft)

1. The problem: who is missing from clinical trials and why it matters
2. What already exists (FDA Snapshots) and what we add
3. Our data: source, filters, and how we cleaned it
4. Live demo of the site
5. Key findings: reporting gaps and participant demographics (plus PPR once added)
6. Limits of the data
7. What we learned, and how the site stays public after the quarter
