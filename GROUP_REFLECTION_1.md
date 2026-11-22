# Group Reflection #1: Accountability and Governance

**Due:** Sunday 11/22 at 11:59pm, on Canvas under "Week 9 | Progress Report (PDF)"
**Format:** one PDF for the group, about 1,000 words at most, worth 8 points
**Exact prompt and grading:** https://canvas.ucsd.edu/courses/77863/assignments/1203380

## The prompt

This is a summary. Read the exact wording on Canvas before you write.

1. Who is accountable for the impacts of what we built? That covers both the problem our site addresses and the technology itself.
2. Drawing on the Week 9 readings on AI governance, ethics, and infrastructure, what ethical trade-offs did our team make while building the project?
3. What oversight or accountability measures, if any, should a project like ours have?

**How it is graded:** real engagement with the Week 9 readings, specifics from our actual project and the trade-offs we really made, and evidence that the whole group contributed.

## How we write it

- Each member writes one section below, about 240 words, so the total stays under 1,000 words.
- Name the reading you draw on and connect it to a concrete decision in our project.
- Use our real decisions. They are recorded in [BACKLOG.md](BACKLOG.md) section 5 and in the Limitations section of [README.md](README.md).
- Sections are due **Friday 11/20**. We merge, trim to the word limit, and export the PDF by **Sunday 11/22**.
- Submitted by: [name]

## Readings to cite

Both links were checked on 11/16/2026.

| Title | Author or organization | Published | Link |
|---|---|---|---|
| America's AI Action Plan | The White House | 2025-07 | https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf |
| US Data Center Map: AI Data Centers Being Built and Planned | Cleanview | Updated daily, viewed 2026-11-16 | https://cleanview.co/data-centers/us |

---

## Section 1: Who is accountable (Sanjana)

Target: about 240 words.

Guiding questions:
- Who is accountable for the problem itself, meaning who decides who gets enrolled in a trial and what gets reported on ClinicalTrials.gov?
- Who is accountable for our site? We chose not to rate trials or label groups, so what are we still responsible for when someone reads our numbers?
- FDA Drug Trials Snapshots is run by a federal agency and ours is run by four students. How does that change who answers for mistakes?
- Which point in a Week 9 reading about who governs a technology applies to a small public tool like ours?

Our site exists because of a gap that no one clearly owns: many clinical trials don't report who took part in them. Sponsors and researchers decide who gets enrolled, and ClinicalTrials.gov lets them report race in standard categories, in their own categories, or not at all. In our data, about one in five trials used their own categories, and about a third of type 2 diabetes trials reported no race. The FDA's Drug Trials Snapshots has a clear owner, since a federal agency publishes it within 30 days of each approval.

For our site, the responsibility is ours. Four students maintain it, and no outside group reviews it. We chose not to rate trials, but we still show participation-to-prevalence ratios (PPR), so we are responsible for how people read them. To reduce the risk of misreading, we added a Data gaps page, show each PPR next to a version with the largest trial removed, and mark values as "pending" when we don't have enough patient data.

The readings helped us see what accountability looks like without a regulator. America's AI Action Plan aims to speed up AI by reducing regulatory requirements, so checking AI-assisted work is up to the people using it. Cleanview shows one way to handle that. It says there is no government database of data centers, so it builds one from public records and saves the source for each campus so anyone can check it. We followed the same approach. Every chart has a source line, our code is public, and we say where AI helped write it. That means readers can catch our mistakes, but it doesn't guarantee anyone will fix them.

## Section 2: What we included, left out, and automated (Woosik)

Target: about 240 words.

Guiding questions:
- What did we leave out, and who disappears from the charts because of it? Think of trials with custom race categories, participants with unknown race, and PPR using only trials with all sites in the US.
- What did we keep that a reader might not expect? Think of trials with no study phase (about 27% of records) and trials the condition search pulls in that are not mainly about that condition.
- What did we automate? The site now refreshes its data every day with no person checking each number, and AI tools helped write the code. What can go wrong without a human in the loop, and what do our safety checks catch or miss?
- Which point in a Week 9 reading about speed, automation, or infrastructure connects to these choices?

The data choice that mattered most was leaving out trials that reported race in their own categories. About one in five trials did this. We could not combine their labels with the standard categories, so we left them out of the race charts. Those trials did collect race data, but their participants disappear from our picture. It was the only honest way to keep the categories comparable, but our charts now describe only part of the trials.

We also automated the data refresh, so the site updates every day with no person checking. Our safety checks only catch obvious failures, such as trial counts dropping more than 10% or a missing column. They would not catch a small change in how ClinicalTrials.gov formats its data that makes our code quietly mislabel trials. The site would still look fine, and wrong numbers would go public with nobody noticing.

We have already seen code run with no errors and still be wrong. The first version of our script, written with AI help, undercounted the trials that reported no race. The corrected count was 1,140 unique trials. It was caught by reviewing the results again, not because anything crashed.

America's AI Action Plan, in its section Build an AI Evaluations Ecosystem, says evaluations are how the industry assesses the "performance and reliability" of AI systems. We learned the same thing at a small scale. We cannot treat code written with AI help or automated output as correct just because it works. Someone has to check the numbers.

## Section 3: Who could be affected by errors or gaps (Saurabi)

The patient counts I collected and the trial data we use do not describe people the same way. SEER and CDC treat Hispanic as its own group, but trials record race and ethnicity separately, so a Hispanic participant also appears in a race group. I think this mostly misrepresents Hispanic patients who are also Black or Asian, who disappear into one group in the patient data, and it can make White PPR look higher than it is. We lined the groups up for breast and prostate cancer, but our diabetes comparisons stay approximate.

Missing values can mislead readers too. Heart failure has no patient counts by group yet, and American Indian or Alaska Native has no patient group for diabetes or heart failure. We mark these as pending, but a reader could still take a blank to mean nothing is wrong, when these are among the smallest groups in the trials.

Small groups are also the easiest to over-read. Only 902 American Indian or Alaska Native participants appear in our diabetes trials, and the Asian or Pacific Islander PPR of 0.62 falls to 0.51 without the largest trial. One study can swing these values, so readers could feel falsely reassured about a group that is missing, or alarmed by noise.

This connects to Cleanview, which exists because no government database tracks data centers. When no official record exists, the people with the most at stake rely on someone else's compilation. In our project, the groups with the least data bear the same cost, because errors about them are hardest to notice.

[Write here]

## Section 4: How we framed it and what oversight we should have (Sneha)

One decision we made was to keep the site descriptive instead of telling readers which trials were “good” or which populations were underrepresented. We show each participation-to-prevalence ratio (PPR) next to a 1.0 reference line and define “underrepresented” in the explainer, but do not label individual groups. This avoids suggesting that one number can fully judge a trial’s fairness, especially when demographic categories do not match perfectly or a result depends heavily on one study. At the same time, our neutral framing could make a real disparity seem less urgent. Asking users to draw their own conclusions does not remove our responsibility for how we present the data.

Our current oversight is mostly transparency. We link to sources and methods, explain limitations and maintenance in the README, and disclose that AI helped write code and text. We also name Woosik as a contact and promise replies through finals week. These steps make our decisions visible, but they do not guarantee that someone will catch or fix an error after the quarter ends.

In America’s AI Action Plan, the section “Promote Mature Federal Capacity for AI Incident Response” argues for planning how to respond when technology fails. We can apply that idea without needing a formal regulator: assign a maintainer, periodically review PPR values, record corrections publicly, and clearly mark the site as archived if nobody can keep checking it. Publishing information creates a responsibility that lasts beyond the assignment.
