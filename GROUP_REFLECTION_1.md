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

[Write here]

## Section 2: What we included, left out, and automated (Woosik)

Target: about 240 words.

Guiding questions:
- What did we leave out, and who disappears from the charts because of it? Think of trials with custom race categories, participants with unknown race, and PPR using only trials with all sites in the US.
- What did we keep that a reader might not expect? Think of trials with no study phase (about 27% of records) and trials the condition search pulls in that are not mainly about that condition.
- What did we automate? The site now refreshes its data every day with no person checking each number, and AI tools helped write the code. What can go wrong without a human in the loop, and what do our safety checks catch or miss?
- Which point in a Week 9 reading about speed, automation, or infrastructure connects to these choices?

[Write here]

## Section 3: Who could be affected by errors or gaps (Saurabi)

Target: about 240 words.

Guiding questions:
- Our patient data counts new cases and treats Hispanic as its own group, while trials record race and ethnicity separately. Who could be misrepresented by that mismatch?
- Some groups and conditions show as pending because we only have rates and not patient counts. What could a reader wrongly conclude from a missing value?
- Some PPR values rest on very few participants or mostly on one trial. Who could be harmed if a reader treats those values as solid?
- Which point in a Week 9 reading about who bears the costs of a technology connects to these gaps?

[Write here]

## Section 4: How we framed it and what oversight we should have (Sneha)

Target: about 240 words.

Guiding questions:
- We show each PPR next to a reference line at 1.0 and define "underrepresented" once instead of labeling groups. What did we gain and what did we give up with that neutral framing?
- What oversight does our project have today? Think of the named contact person, the limitations and maintenance notes, the source list, and the AI use disclosure.
- What oversight should a project like ours have that it does not have yet? Think of who reviews the numbers, who fixes errors after the quarter ends, and what happens if nobody maintains the site.
- Which oversight or accountability idea from a Week 9 reading would fit a project of our size?

[Write here]
