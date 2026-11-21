# Site Plan

**Owner:** Sanjana
**Status:** Built 11/21 and waiting for team review. The first plan (11/6) had six pages and a wireframe for each. This version records what was built, the answers to the open questions, and what is still to check.

The goal for the site: a reader should understand the main point at a glance, find everything easily, and always know which data is missing. Our professor asked for two things in particular. Only present complete data, and make clear which data sets are missing variables or information. Also check and improve the site's accessibility.

---

## 1. Site map

```
Home           index.html     The answer at a glance
Explore        explore.html   One condition at a time
Data gaps      gaps.html      What is missing, by condition
Learn          learn.html     Study phases, PPR, limits of the data
Compare        compare.html   How this site differs from FDA Drug Trials Snapshots
About          about.html     Sources, methods, AI use, contact
```

All pages share one header with navigation and one short footer (data date, contact, AI disclosure). The pages are plain HTML in `docs/`, so GitHub Pages and the daily refresh work as before.

| File | What it does |
|---|---|
| `style.css` | Look and layout for every page |
| `common.js` | Condition names, race colors, number formatting, the "data updated" text, and the completeness counts |
| `home.js` | Key numbers, the race chart for all four conditions, condition cards, the reporting bar |
| `explore.js` | Condition buttons, filters, and every chart and table on Explore |
| `gaps.js` | The two tables on Data gaps |
| `data.js`, `ppr.js` | Data from the pipeline (unchanged) |

---

## 2. What each page has

**Home.** A dark header with the question, three big numbers, and a colored race chart for all four conditions straight away. Next come four condition cards, a bar showing how many trials reported race in standard categories, in their own categories, or not at all, and three links to keep going. The chart has a table version.

**Explore.**
1. Condition buttons, and a collapsed "Refine" box for record type and study phase.
2. Four summary numbers.
3. "How complete is this data?": how many trials reported race (standard, own categories, not reported), ethnicity, average age, and all-US sites.
4. Race, patient comparison (PPR), ethnicity, age, and the largest trials.
5. Each chart has a plain headline, a note saying how many trials it uses and what was left out, and a collapsed "About this chart" with the notes and sources.
6. The patient comparison shows only groups that have both a trial share and a patient share. The rest are listed as "Not shown yet" with the reason.

**Data gaps.** A table of how much of each condition's trial data has each piece of information, and a table of which patient comparisons are shown or still waiting.

**Learn.** Sneha's text on study phases, PPR, and limits, moved over unchanged.

**Compare.** A table and four short blocks comparing this site with FDA Drug Trials Snapshots, plus ICER's diversity rating and GSK's study, with sources.

**About.** Sources and methods, how we used AI, and contact and upkeep, moved over unchanged.

---

## 3. Answers to the four open questions

1. **Is six pages too many?** Six pages are what we built, because each one has one job and the nav shows all of them. The first plan had the same six, and the build matched it.
2. **One Explore page with tabs, or a page per condition?** One page with condition buttons. The charts are the same for every condition, and the choice is kept in the address (`explore.html?c=heart_failure`) so a link opens the same view.
3. **Where does PPR go on Explore?** Directly after the race chart, because the patient comparison uses the same race groups.
4. **Should Home show a chart?** Yes. Home shows the race chart for all four conditions, and a bar for how often race is reported. The prototype's single page could not do both a short first view and the full detail, which is why it was split.

---

## 4. Design and accessibility choices

- **Plain language first.** Short intro, one headline per chart, long notes collapsed.
- **Missing data is visible.** Each chart says how many trials it uses and what was left out. Data gaps shows the full picture.
- **No hover-only information.** Counts are always visible. Home and the patient comparison have table versions.
- **Color is never the only signal.** Every bar and segment has a text label and value.
- **Structure for screen readers and keyboards.** A skip link, one main heading per page, labeled regions, a live message when filters change, and visible focus rings.
- **Readable at any size.** Body text is 18 px, tap targets are at least 44 px, and the pages reflow on a phone and when zoomed.
- **Motion.** Bars animate in a little and stop if the reader's device asks for reduced motion.
- **Neutral wording.** No group is labeled as underrepresented. PPR sits next to a reference line at 1.0, as the team decided.

---

## 5. Checks done and still to do

Done on 11/21, with a script that checks contrast (text at least 4.5:1), headings, labels, duplicate IDs, tap target size, and sideways scrolling. It found no problems on the six pages at desktop width or at a phone-sized view (375 px wide). This is not a full audit.

Still to do:
- Run a free checker, such as WAVE or axe, on each page. The Harvard accessibility page lists free ones: https://accessibility.huit.harvard.edu/auto-tools-testing
- Use each page with the keyboard only (Tab, Enter, Space).
- Try a screen reader such as NVDA, which is free on Windows.
- Check the pages again on the live site after the data refreshes, since local testing used older data.
- Look at the site on a real phone.
- Check each claim on the Compare page against the FDA's own reports.
