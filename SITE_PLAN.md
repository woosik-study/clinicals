# Site Plan and Wireframe

**Owner:** Sanjana
**Status:** Week 6 draft (11/6). Team to review before we split the prototype into pages.

This file plans the pages of the final site and gives a rough layout for each one. The current prototype at https://woosik-study.github.io/clinicals is a single page. This plan shows where each part of it goes and what still needs to be added.

---

## 1. Site map

```
Home
├── Explore the data          (one page, a tab per condition)
├── How we compare            (FDA Drug Trials Snapshots and other tools)
├── How to read this          (study phases, PPR, limits of the data)
├── Sources                   (resource list, 10+ sources)
└── About                     (methods, team, AI use)
```

Every page shares the same header, navigation bar, and footer:

```
┌──────────────────────────────────────────────────────────────────────┐
│ Who Is in the Trial?   Home  Explore  Compare  Learn  Sources  About │
└──────────────────────────────────────────────────────────────────────┘
  ...page content...
┌──────────────────────────────────────────────────────────────────────┐
│ Data: ClinicalTrials.gov (snapshot 11/4/2026), NCI SEER, CDC.        │
│ Built by the Clinicals team, CSE 194, UC San Diego.                  │
└──────────────────────────────────────────────────────────────────────┘
```

On phones the navigation links wrap onto a second line. No menu button is needed for six links.

---

## 2. Pages

| Page | File | Purpose | Main content | Owner of content | Exists in prototype? |
|---|---|---|---|---|---|
| Home | `index.html` | Explain the question in under a minute and send readers to the data | Intro, 3 headline numbers, 4 condition cards, links to the other pages | Sanjana (layout), all (wording) | Partly: the intro text |
| Explore the data | `explore.html` | Let readers look at one condition at a time | Condition tabs, phase filter, summary stats, race chart, race reporting chart, PPR chart, trial table | Woosik | Yes, except PPR |
| How we compare | `compare.html` | Show what already exists and what our site adds | Comparison table, short write-up, links to each tool | Sanjana (Week 7 to 8) | No |
| How to read this | `learn.html` | Explain terms a general reader will not know | Study phases, PPR, limits of the data | Sneha | Placeholder text only |
| Sources | `sources.html` | The required resource list | Sources grouped by topic, each with one line on how we used it | Saurabi | No |
| About | `about.html` | How the data was built and who built it | Data pipeline in plain language, team, AI tool usage | All | No (lives in README) |

### Where the prototype's sections go

| Prototype section | New home |
|---|---|
| Banner and intro | Home (intro), all pages (snapshot date in footer) |
| Condition tabs and phase filter | Explore |
| Summary stats | Explore, plus 3 headline numbers on Home |
| Race of trial participants | Explore |
| How often do trials report participants' race? | Explore |
| Trials table | Explore |
| "How to read this" card | How to read this page, with a short "What does this mean?" link next to each chart on Explore |

---

## 3. Wireframes

Boxes are rough. Sizes and wording are placeholders.

### Home

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  Who Is in the Trial?                                        │
│  One paragraph: why it matters who takes part in trials,     │
│  what this site shows, and that we do not rate trials.       │
│                                                              │
│  [ Explore the data → ]                                      │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌────────────┐  ┌────────────┐              │
│  │  4,415     │  │  1.6M      │  │  X%        │              │
│  │  trials    │  │  people    │  │ reported   │              │
│  │            │  │            │  │ race       │              │
│  └────────────┘  └────────────┘  └────────────┘              │
│  (numbers come from data.js so they update on refresh)       │
├──────────────────────────────────────────────────────────────┤
│  Pick a condition                                            │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  │Breast cancer │ │Prostate      │ │Type 2        │ │Heart failure │
│  │N trials      │ │cancer        │ │diabetes      │ │N trials      │
│  │  [View →]    │ │  [View →]    │ │  [View →]    │ │  [View →]    │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
│  Each card opens explore.html#<condition>                    │
├──────────────────────────────────────────────────────────────┤
│  What makes this different?                                  │
│  2 to 3 sentences, then [ How we compare → ]                 │
│                                                              │
│  New to clinical trials?  [ How to read this → ]             │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

### Explore the data

This is the prototype page with a PPR section added. The selected condition goes in the URL (`explore.html#heart_failure`) so a link opens the same view.

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  Explore the data                                            │
│  ( Breast cancer ) ( Prostate ) ( Type 2 diabetes ) ( HF )   │
│                                      Study phase [All  ▾]    │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐             │
│  │ trials  │ │ people  │ │% race   │ │% female │             │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘             │
├──────────────────────────────────────────────────────────────┤
│  Race of trial participants                 [What is this?]  │
│  White      ████████████████████████  75%                    │
│  Black      ████                      11%                    │
│  Asian      ████                      11%                    │
│  ...                                                         │
│  X% of participants had unknown race. Based on N trials.     │
├──────────────────────────────────────────────────────────────┤
│  Trial participants compared with patients (PPR)  [What is PPR?]
│                      0     0.5    1.0    1.5    2.0          │
│  White               ├──────┼──────●──┼──────┤               │
│  Black               ├──────●──────┼──────┼──────┤           │
│  ...                              ┆ reference line at 1.0    │
│  US-only trials. Patient data from SEER or CDC (year).       │
│  Groups are not labeled. Small groups get a note (rule TBD). │
├──────────────────────────────────────────────────────────────┤
│  How often do trials report participants' race?              │
│  Standard categories  ████████████████  60%                  │
│  Own categories       █████             20%                  │
│  Not reported         █████             20%                  │
├──────────────────────────────────────────────────────────────┤
│  Trials (50 largest)                                         │
│  ┌──────────────┬───────┬───────┬──────────────┬──────────┐  │
│  │ Trial        │ Phase │ Start │ Participants │ Race     │  │
│  ├──────────────┼───────┼───────┼──────────────┼──────────┤  │
│  │ NCT… title   │       │       │              │          │  │
│  └──────────────┴───────┴───────┴──────────────┴──────────┘  │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

Open question: should PPR sit above or below the race reporting chart? Above puts the two race charts together. Below keeps the "what we have" charts before the comparison.

### How we compare

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  How we compare                                              │
│  Short intro: other tools already show trial demographics.   │
│  Here is what each one covers and what this site adds.       │
├──────────────────────────────────────────────────────────────┤
│  ┌───────────────────┬─────────────────┬──────────────────┐  │
│  │                   │ FDA Snapshots   │ This site        │  │
│  ├───────────────────┼─────────────────┼──────────────────┤  │
│  │ Which trials      │                 │                  │  │
│  │ Compared with     │                 │                  │  │
│  │ patients?         │                 │                  │  │
│  │ Missing data shown│                 │                  │  │
│  │ ...               │                 │                  │  │
│  └───────────────────┴─────────────────┴──────────────────┘  │
│  (scrolls sideways on phones)                                │
├──────────────────────────────────────────────────────────────┤
│  What FDA Drug Trials Snapshots does well        (1 para)    │
│  What it does not cover                          (1 para)    │
│  What this site adds                             (1 para)    │
│  What this site does not do                      (1 para)    │
├──────────────────────────────────────────────────────────────┤
│  Other tools (short cards, 1 to 2 lines each)                │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

### How to read this

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  How to read this                                            │
│  On this page: Study phases · PPR · Limits of the data       │
├──────────────────────────────────────────────────────────────┤
│  What is a study phase?        (Sneha's text)                │
├──────────────────────────────────────────────────────────────┤
│  What is PPR?                  (Sneha's text + worked        │
│                                 example with made-up numbers)│
├──────────────────────────────────────────────────────────────┤
│  Limits of the data            (Sneha's text)                │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

Each heading gets an anchor (`learn.html#ppr`) so the "What is this?" links on Explore jump straight to it.

### Sources

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  Sources                                                     │
│  Trial data · Patient data · Trial diversity research ·      │
│  Existing tools                                              │
├──────────────────────────────────────────────────────────────┤
│  • Title (link). Type. One line on how we used it.           │
│  • ...                                                       │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

Content comes from [RESEARCH.md](RESEARCH.md).

### About

```
┌──────────────────────────────────────────────────────────────┐
│ [nav]                                                        │
├──────────────────────────────────────────────────────────────┤
│  About this project                                          │
│  How we built the data   (plain-language version of the      │
│                           README's Data section)             │
│  Data snapshot date and how to refresh it                    │
│  Team                                                        │
│  How we used AI tools                                        │
│  Code on GitHub →                                            │
├──────────────────────────────────────────────────────────────┤
│ [footer]                                                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. How to build it

- Keep it static: plain HTML pages in `docs/` sharing `style.css`. No framework, so GitHub Pages keeps working as it does now.
- Only `explore.html` loads `data.js` and `app.js`. Home loads `data.js` too if we want its headline numbers to update on their own.
- Copy the nav and footer into each page by hand. Six pages is few enough that this is simpler than a build step.
- Keep the wording rules from BACKLOG.md section 5 on every page: no group is labeled as underrepresented, and PPR values sit next to a reference line at 1.0.

Suggested order:

1. Move the prototype to `explore.html` and make `index.html` the new Home page.
2. Add the shared nav and footer.
3. Add empty `compare.html`, `learn.html`, `sources.html`, and `about.html` so each owner has a page to fill.
4. Add the PPR section to Explore once the prevalence data is ready.

---

## 5. Questions for the team

1. Is six pages too many? Sources and About could be one page.
2. One Explore page with tabs, or a separate page per condition? This plan uses one page because the charts are the same for every condition.
3. Where should PPR go on Explore (see the open question above)?
4. Should Home show any chart, or only numbers and links?
