// Home page: key numbers, the race chart for all four conditions, condition cards, and the reporting split.
const trialsOnce = uniqueTrials();
const people = trialsOnce.reduce((s, r) => s + (r.n || 0), 0);
const noRace = trialsOnce.filter(r => r.rf === "none").length;

$("bigstats").innerHTML = [
  [fmt(trialsOnce.length), "clinical trials with posted results"],
  [(people / 1e6).toFixed(1) + " million", "participants across those trials"],
  [pct(noRace, trialsOnce.length).toFixed(0) + "%", "of trials did not report participants' race"],
].map(([v, l]) => `<div class="bigstat"><div class="v">${v}</div><div class="l">${l}</div></div>`).join("");

// Stacked bar for each condition: shares of participants with known race, in trials that used the standard categories.
const used = [];
let usedTrials = 0, allTrials = 0;
const rowsHtml = Object.entries(CONDS).map(([key, name]) => {
  const rows = data.filter(r => r.c === key);
  const t = raceTotals(rows);
  allTrials += rows.length; usedTrials += t.omb.length;
  if (!t.known) return "";
  const parts = RACE_ORDER.map(i => ({i, p: pct(t.tot[i], t.known)}));
  used.push({name, parts, t, n: t.omb.length, total: rows.length});
  const label = `${name}: ` + parts.map(x => `${RACE_SHORT[x.i]} ${x.p.toFixed(1)}%`).join(", ");
  const segs = parts.map(x => `<span class="seg" style="width:${x.p}%;background:${RACE_COLOR[x.i][0]};color:${RACE_COLOR[x.i][1]}">${x.p >= 6 ? Math.round(x.p) + "%" : ""}</span>`).join("");
  return `<div class="stack"><div class="rowlabel"><span>${name}</span><small>${fmt(t.omb.length)} of ${fmt(rows.length)} trials used</small></div>` +
    `<div class="stackbar" role="img" aria-label="${esc(label)}">${segs}</div></div>`;
}).join("");
$("herochart").innerHTML = rowsHtml;
$("herokey").innerHTML = RACE_ORDER.map(i => `<li><span class="sw" style="background:${RACE_COLOR[i][0]}"></span>${RACE_SHORT[i]}</li>`).join("");
$("herocover").innerHTML = `<span class="chip">Uses ${fmt(usedTrials)} of ${fmt(allTrials)} trial entries</span> Only trials that reported race in the standard categories are included, and a trial listed under two conditions appears in both. Participants with unknown race are left out of the bars.`;
$("herotable").innerHTML = `<caption>Share of participants with known race, in trials that used the standard categories.</caption><thead><tr><th scope="col">Condition</th>` +
  RACE_ORDER.map(i => `<th scope="col" class="num">${RACE_SHORT[i]}</th>`).join("") + `<th scope="col" class="num">Trials used</th></tr></thead><tbody>` +
  used.map(u => `<tr><th scope="row">${u.name}</th>` + u.parts.map(x => `<td class="num">${x.p.toFixed(1)}%</td>`).join("") + `<td class="num">${fmt(u.n)} of ${fmt(u.total)}</td></tr>`).join("") + `</tbody>`;

// Condition cards.
$("condcards").innerHTML = Object.entries(CONDS).map(([key, name]) => {
  const rows = data.filter(r => r.c === key);
  const c = completeness(rows);
  return `<a class="tile" href="explore.html?c=${key}"><h3>${name}</h3><span class="num">${fmt(rows.length)}</span><p>trials with posted results. ${pct(c.race, rows.length).toFixed(0)}% reported race in the standard categories.</p><span class="go">Explore ${name.toLowerCase()}</span></a>`;
}).join("");

// Reporting split across all unique trials.
const all = completeness(trialsOnce);
const split = [
  {k: "Standard race categories", n: all.race, bg: "#1f5fa8", fg: "#fff"},
  {k: "Their own race categories", n: all.own, bg: "#59646e", fg: "#fff"},
  {k: "Race not reported", n: all.none, bg: "#b85c00", fg: "#fff"},
];
$("gap-sub").textContent = `Of ${fmt(all.n)} trials, ${pct(all.none, all.n).toFixed(0)}% did not report participants' race at all, and another ${pct(all.own, all.n).toFixed(0)}% used their own categories that cannot be combined with the rest.`;
const gapLabel = split.map(s => `${s.k}: ${fmt(s.n)} trials, ${pct(s.n, all.n).toFixed(1)}%`).join("; ");
$("gapchart").innerHTML = `<div class="stackbar" role="img" aria-label="${esc(gapLabel)}">` +
  split.map(s => `<span class="seg" style="width:${pct(s.n, all.n)}%;background:${s.bg};color:${s.fg}">${Math.round(pct(s.n, all.n))}%</span>`).join("") + `</div>`;
$("gapkey").innerHTML = split.map(s => `<li><span class="sw" style="background:${s.bg}"></span>${s.k} (${fmt(s.n)} trials)</li>`).join("");
