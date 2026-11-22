// Explore page: one condition at a time. Every chart only uses trials that have the information it shows,
// and says how many trials that is.
const AGE_BINS = [["Under 18", 0, 18], ["18 to 39", 18, 40], ["40 to 49", 40, 50], ["50 to 59", 50, 60], ["60 to 69", 60, 70], ["70 to 100", 70, 100.0001]];
const condsByTrial = {};
data.forEach(r => (condsByTrial[r.id] = condsByTrial[r.id] || []).push(r.c));
let cond = "breast_cancer", showAll = false;
const fromUrl = new URLSearchParams(location.search).get("c");
if (CONDS[fromUrl]) cond = fromUrl;

const coverLine = (used, total, extra) =>
  `<span class="chip">Uses ${fmt(used)} of ${fmt(total)} trials (${pct(used, total).toFixed(0)}%)</span> ${extra || ""} <a href="gaps.html">What is missing?</a>`;

function render() {
  // Record type: "phased" has a study phase, "nophase" lists none (blank or "NA" on ClinicalTrials.gov).
  const kind = $("kind").value;
  $("phase").disabled = kind === "nophase";
  const phase = kind === "nophase" ? "" : $("phase").value;
  const hasPhase = r => (r.p || "").includes("PHASE");
  const rows = data.filter(r => r.c === cond &&
    (!kind || (kind === "phased") === hasPhase(r)) &&
    (!phase || (r.p || "").split("|").includes(phase)));
  document.querySelectorAll("#conds button").forEach(b => b.setAttribute("aria-pressed", b.dataset.c === cond));
  $("refine-now").textContent = kind || phase ? "(on)" : "";
  try { history.replaceState(null, "", `?c=${cond}${location.hash}`); } catch (e) { /* opened from a file, no URL to update */ }
  renderPPR();

  if (!rows.length) {
    $("live").textContent = `${CONDS[cond]}: no trials match this filter.`;
    $("stats").innerHTML = `<div class="stat"><div class="l">No trials match this filter.</div></div>`;
    ["cover-race", "cover-other", "race-chart", "eth-chart", "age-chart"].forEach(id => $(id).innerHTML = "");
    ["race-head", "eth-head", "age-head", "race-cover", "eth-cover", "age-cover", "trials-head"].forEach(id => $(id).textContent = "");
    $("trials-table").querySelector("tbody").innerHTML = "";
    $("more-trials").hidden = true;
    return;
  }

  const c = completeness(rows);
  const rt = raceTotals(rows);
  const sx = rows.filter(r => r.fe != null || r.ma != null);
  const fe = sx.reduce((s, r) => s + (r.fe || 0), 0), ma = sx.reduce((s, r) => s + (r.ma || 0), 0);
  const people = rows.reduce((s, r) => s + (r.n || 0), 0);
  $("live").textContent = `Showing ${CONDS[cond]}: ${fmt(rows.length)} trials and ${fmt(people)} participants.`;

  $("stats").innerHTML = [
    [fmt(rows.length), "trials with posted results"],
    [fmt(people), "participants"],
    [pct(c.race + c.own, rows.length).toFixed(0) + "%", "of trials reported race"],
    [(fe + ma) ? pct(fe, fe + ma).toFixed(0) + "%" : "n/a", "of participants were female"],
  ].map(([v, l]) => `<div class="stat"><div class="v">${v}</div><div class="l">${l}</div></div>`).join("");

  // How complete is the data.
  $("cover-race").innerHTML =
    bar("Standard race categories", pct(c.race, c.n), `${fmt(c.race)} of ${fmt(c.n)} trials. Shown in the race chart.`) +
    bar("Their own race categories", pct(c.own, c.n), `${fmt(c.own)} trials. Not shown, because these labels cannot be combined with the standard ones.`, {cls: "gray"}) +
    bar("Race not reported", pct(c.none, c.n), `${fmt(c.none)} trials. Not shown.`, {cls: "warn"});
  $("cover-other").innerHTML =
    bar("Ethnicity reported", pct(c.eth, c.n), `${fmt(c.eth)} of ${fmt(c.n)} trials. Shown in the ethnicity chart.`) +
    bar("Average age reported", pct(c.age, c.n), `${fmt(c.age)} of ${fmt(c.n)} trials. Shown in the age chart.`) +
    bar("All sites in the US", pct(c.us, c.n), `${fmt(c.us)} of ${fmt(c.n)} trials. Needed for the patient comparison.`);

  // Race.
  if (rt.known) {
    const top = RACE_ORDER.reduce((a, b) => rt.tot[b] > rt.tot[a] ? b : a);
    $("race-head").textContent = `${RACE_SHORT[top]} participants were ${pct(rt.tot[top], rt.known).toFixed(0)}% of those with known race.`;
    $("race-chart").innerHTML = RACE_ORDER.map(i =>
      bar(RACES[i], pct(rt.tot[i], rt.known), `${fmt(rt.tot[i])} of ${fmt(rt.known)} participants with known race`, {color: RACE_COLOR[i][0]})).join("");
    $("race-cover").innerHTML = coverLine(rt.omb.length, c.n,
      `Left out: ${fmt(c.own)} used their own categories and ${fmt(c.none)} did not report race. ${pct(rt.unknown, rt.all).toFixed(1)}% of participants in the trials used had unknown race (${fmt(rt.unknown)} of ${fmt(rt.all)}).`);
  } else {
    $("race-head").textContent = "";
    $("race-chart").innerHTML = `<li class="empty">No trials in this view reported race in the standard categories.</li>`;
    $("race-cover").textContent = "";
  }

  // Ethnicity.
  const eth = rows.filter(r => r.e);
  const ethTot = [0, 1, 2].map(i => eth.reduce((s, r) => s + (r.e[i] || 0), 0));
  const ethKnown = ethTot[0] + ethTot[1], ethAll = ethKnown + ethTot[2];
  if (ethKnown) {
    $("eth-head").textContent = `${pct(ethTot[0], ethKnown).toFixed(0)}% of participants with known ethnicity were Hispanic or Latino.`;
    $("eth-chart").innerHTML =
      bar("Hispanic or Latino", pct(ethTot[0], ethKnown), `${fmt(ethTot[0])} of ${fmt(ethKnown)} participants with known ethnicity`) +
      bar("Not Hispanic or Latino", pct(ethTot[1], ethKnown), `${fmt(ethTot[1])} of ${fmt(ethKnown)} participants with known ethnicity`);
    $("eth-cover").innerHTML = coverLine(eth.length, c.n,
      `${fmt(c.n - eth.length)} did not report ethnicity. ${pct(ethTot[2], ethAll).toFixed(1)}% of participants in the trials used had unknown ethnicity.`);
  } else {
    $("eth-head").textContent = "";
    $("eth-chart").innerHTML = `<li class="empty">No trials in this view reported ethnicity in the standard categories.</li>`;
    $("eth-cover").textContent = "";
  }

  // Age.
  const aged = rows.filter(r => r.ag != null && r.ag <= 100);
  const odd = rows.filter(r => r.ag != null && r.ag > 100).length;
  if (aged.length) {
    const bins = AGE_BINS.map(([name, lo, hi]) => [name, aged.filter(r => r.ag >= lo && r.ag < hi).length]);
    const best = bins.reduce((a, b) => b[1] > a[1] ? b : a);
    $("age-head").textContent = `The most common average age was ${best[0]}, for ${pct(best[1], aged.length).toFixed(0)}% of trials that reported one.`;
    $("age-chart").innerHTML = bins.map(([name, k]) => bar(name, pct(k, aged.length), `${fmt(k)} trials`, {cls: "gray"})).join("");
    $("age-cover").innerHTML = coverLine(aged.length, c.n,
      `${fmt(c.n - aged.length - odd)} did not report an average age${odd ? `, and ${odd} reported one over 100, which is likely an entry error and is not shown` : ""}.`);
  } else {
    $("age-head").textContent = "";
    $("age-chart").innerHTML = `<li class="empty">No trials in this view reported an average age.</li>`;
    $("age-cover").textContent = "";
  }

  // Largest trials.
  const sorted = [...rows].sort((a, b) => (b.n || 0) - (a.n || 0));
  const shown = sorted.slice(0, showAll ? 50 : 10);
  const lbl = {omb: "Yes", customized: "Own categories", none: "No"};
  const alsoListed = r => {
    const others = condsByTrial[r.id].filter(x => x !== r.c).map(x => CONDS[x]);
    return others.length ? `<div class="also">Also listed under: ${others.join(", ")}</div>` : "";
  };
  $("trials-head").textContent = `Showing the ${shown.length} largest of ${fmt(rows.length)} trials in this view.`;
  $("more-trials").hidden = rows.length <= 10;
  $("more-trials").textContent = showAll ? "Show fewer" : "Show the 50 largest";
  $("trials-table").querySelector("tbody").innerHTML = shown.map(r =>
    `<tr><td><a href="https://clinicaltrials.gov/study/${esc(r.id)}" target="_blank" rel="noopener">${esc(r.id)}<span class="sr"> (opens ClinicalTrials.gov in a new tab)</span></a><br>${esc(r.t)}${alsoListed(r)}</td>
     <td>${(r.p || "n/a").replaceAll("PHASE", "Phase ").replaceAll("|", " / ").replace("EARLY_Phase 1", "Early Phase 1").replace("NA", "n/a")}</td>
     <td>${esc(r.y)}</td><td class="num">${r.n ? fmt(r.n) : ""}</td><td>${lbl[r.rf]}</td></tr>`).join("");
}

// PPR: draw only the groups that have both a trial share and a patient share. List the rest as not shown yet.
function renderPPR() {
  const rs = PPR.filter(r => r.condition === cond);
  const done = rs.filter(r => r.ppr !== "");
  const waiting = rs.filter(r => r.ppr === "" && r.seer_group).map(r => r.trial_group);
  const nomatch = rs.filter(r => r.ppr === "" && !r.seer_group).map(r => r.trial_group);
  const notShown = (waiting.length ? `<p><strong>Not shown yet:</strong> ${waiting.join(", ")}. Patient counts for ${waiting.length > 1 ? "these groups are" : "this group is"} still being added.</p>` : "") +
    (nomatch.length ? `<p><strong>No comparison possible:</strong> ${nomatch.join(", ")}. The patient data has no matching group.</p>` : "");

  if (!done.length) {
    $("ppr-chart").innerHTML = `<div class="pending"><p><strong>Not shown yet for ${CONDS[cond].toLowerCase()}.</strong> We have the trial data, but not the patient counts we need to compare it with. We only show a comparison when both sides are complete.</p>${notShown}</div>`;
    $("ppr-cover").innerHTML = `<a href="gaps.html">See what is missing</a>`;
    $("ppr-numbers").hidden = true;
    return;
  }
  const vals = done.flatMap(r => [+r.ppr, +r.ppr_without_largest]).filter(v => v > 0);
  const max = Math.max(2, Math.ceil(Math.max(...vals) * 2) / 2);
  const x = v => (100 * v / max).toFixed(2) + "%";
  const ticks = [];
  for (let t = 0; t <= max + 1e-9; t += 0.5) ticks.push(`<span style="left:${x(t)}">${t.toFixed(1)}</span>`);
  const p1 = v => (+v).toFixed(1);
  const rowHtml = done.map(r => {
    const hasWo = r.ppr_without_largest !== "";
    const without = hasWo ? `<span class="wo">${(+r.ppr_without_largest).toFixed(2)} without largest trial</span>` : "";
    return `<div class="ppr-row"><div class="ppr-label">${esc(r.trial_group)}</div>
      <div class="ppr-track" aria-hidden="true"><div class="ref" style="left:${x(1)}"></div>${hasWo ? `<div class="dot hollow" style="left:${x(+r.ppr_without_largest)}"></div>` : ""}<div class="dot" style="left:${x(+r.ppr)}"></div></div>
      <div class="ppr-val">${(+r.ppr).toFixed(2)}${without}</div>
      <div class="ppr-detail">Trials ${p1(r.trial_share_pct)}%${r.trial_share_without_largest_pct !== "" ? ` (${p1(r.trial_share_without_largest_pct)}% without the largest trial)` : ""}, patients ${p1(r.seer_share_pct)}%</div></div>`;
  }).join("");
  $("ppr-chart").innerHTML = `<div class="ppr-axis" aria-hidden="true"><div></div><div class="ticks">${ticks.join("")}</div><div></div></div>${rowHtml}` +
    `<ul class="key"><li><span class="dot-key"></span>All trials</li><li><span class="dot-key hollow"></span>Without the largest trial</li><li><span class="ref-key"></span>1.0, equal shares</li></ul>` +
    (notShown ? `<div class="pending" style="margin-top:1rem">${notShown}</div>` : "");
  $("ppr-cover").innerHTML = `<span class="chip">Uses ${fmt(done[0].trials_used)} trials with all sites in the US</span> ${cond === "type_2_diabetes" ? "Patient data: CDC estimated counts of adults with diagnosed diabetes, 2021. Diagnosed diabetes of any type stands in for type 2. " : "Patient data: NCI SEER new cases, 2019 to 2023. "}${cond === "prostate_cancer" ? "Trials also listed under breast cancer are left out. " : ""}Hispanic or Latino uses the trials' ethnicity data. <a href="gaps.html">What is missing?</a>`;
  $("ppr-numbers").hidden = false;
  $("ppr-table").innerHTML = `<caption>Numbers behind the patient comparison for ${CONDS[cond].toLowerCase()}.</caption><thead><tr><th scope="col">Group</th><th scope="col" class="num">PPR</th><th scope="col" class="num">PPR without largest trial</th><th scope="col" class="num">Trial share</th><th scope="col" class="num">Trial share without largest trial</th><th scope="col" class="num">Patient share</th><th scope="col" class="num">Participants</th><th scope="col" class="num">Share from largest trial</th></tr></thead><tbody>` +
    done.map(r => `<tr><th scope="row">${esc(r.trial_group)}</th><td class="num">${(+r.ppr).toFixed(2)}</td><td class="num">${r.ppr_without_largest !== "" ? (+r.ppr_without_largest).toFixed(2) : ""}</td><td class="num">${p1(r.trial_share_pct)}%</td><td class="num">${r.trial_share_without_largest_pct !== "" ? p1(r.trial_share_without_largest_pct) + "%" : ""}</td><td class="num">${p1(r.seer_share_pct)}%</td><td class="num">${fmt(r.trial_participants)} in ${fmt(r.trials_used)} trials</td><td class="num">${r.largest_trial_share_pct !== "" ? r.largest_trial_share_pct + "%" : ""}</td></tr>`).join("") + `</tbody>`;
}

$("conds").innerHTML = Object.entries(CONDS).map(([k, v]) => `<button type="button" data-c="${k}" aria-pressed="false">${v}</button>`).join("");
$("conds").addEventListener("click", e => { if (e.target.dataset.c) { cond = e.target.dataset.c; render(); } });
$("phase").addEventListener("change", render);
$("kind").addEventListener("change", render);
$("more-trials").addEventListener("click", () => { showAll = !showAll; render(); });
render();
