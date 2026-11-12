const CONDS = {breast_cancer:"Breast cancer", prostate_cancer:"Prostate cancer", type_2_diabetes:"Type 2 diabetes", heart_failure:"Heart failure"};
const RACES = ["American Indian or Alaska Native","Asian","Native Hawaiian or Other Pacific Islander","Black or African American","White","More than one race","Unknown or Not Reported"];
const data = window.TRIALS || [];
const PPR = window.PPR || [];
const AGE_BINS = [["Under 18", 0, 18], ["18 to 39", 18, 40], ["40 to 49", 40, 50], ["50 to 59", 50, 60], ["60 to 69", 60, 70], ["70 to 100", 70, 100.0001]];
let cond = "breast_cancer";
const $ = id => document.getElementById(id);
const fmt = n => Math.round(n).toLocaleString();
const pct = (a, b) => b ? (100 * a / b) : 0;
const UNKNOWN = RACES.indexOf("Unknown or Not Reported");
const condsByTrial = {};
data.forEach(r => (condsByTrial[r.id] = condsByTrial[r.id] || []).push(r.c));

function bar(label, p, title, cls="") {
  return `<div class="bar" title="${title}"><span>${label}</span><div class="track"><div class="fill ${cls}" style="width:${Math.max(p,0.5)}%"></div></div><span class="pct">${p.toFixed(1)}%</span></div>`;
}

function render() {
  const phase = $("phase").value;
  const rows = data.filter(r => r.c === cond && (!phase || (r.p || "").split("|").includes(phase)));
  document.querySelectorAll("#conds button").forEach(b => b.setAttribute("aria-selected", b.dataset.c === cond));

  if (!rows.length) {
    $("stats").innerHTML = `<div class="stat"><div class="l">No trials match this filter.</div></div>`;
    $("race").innerHTML = $("reporting").innerHTML = $("ethnicity").innerHTML = $("age").innerHTML = `<p class="empty">No data.</p>`;
    renderPPR();
    $("trials").querySelector("tbody").innerHTML = "";
    return;
  }
  const omb = rows.filter(r => r.rf === "omb");
  const anyRace = rows.filter(r => r.rf !== "none").length;
  const raceTot = RACES.map((_, i) => omb.reduce((s, r) => s + (r.r[i] || 0), 0));
  const allRace = raceTot.reduce((a, b) => a + b, 0);
  const unknownRace = raceTot[UNKNOWN], knownRace = allRace - unknownRace;
  const sx = rows.filter(r => r.fe != null || r.ma != null);
  const fe = sx.reduce((s, r) => s + (r.fe || 0), 0), ma = sx.reduce((s, r) => s + (r.ma || 0), 0);
  const people = rows.reduce((s, r) => s + (r.n || 0), 0);

  $("stats").innerHTML = [
    [fmt(rows.length), "trials with posted results"],
    [fmt(people), "participants"],
    [pct(anyRace, rows.length).toFixed(0) + "%", "of trials reported race"],
    [(fe + ma) ? pct(fe, fe + ma).toFixed(0) + "%" : "n/a", "of participants were female"],
  ].map(([v, l]) => `<div class="stat"><div class="v">${v}</div><div class="l">${l}</div></div>`).join("");

  const raceBars = knownRace
    ? RACES.map((name, i) => i === UNKNOWN ? "" : bar(name, pct(raceTot[i], knownRace), `${fmt(raceTot[i])} of ${fmt(knownRace)} participants with known race`)).join("")
    : "";
  $("race").innerHTML = allRace
    ? raceBars + `<p class="note" style="margin-top:12px">${pct(unknownRace, allRace).toFixed(1)}% of participants had unknown race (${fmt(unknownRace)} of ${fmt(allRace)}). Based on ${fmt(omb.length)} trials.</p>`
    : `<p class="empty">No trials in this view reported race in the standard categories.</p>`;

  const eth = rows.filter(r => r.e);
  const ethTot = [0, 1, 2].map(i => eth.reduce((s, r) => s + (r.e[i] || 0), 0));
  const ethKnown = ethTot[0] + ethTot[1], ethAll = ethKnown + ethTot[2];
  $("ethnicity").innerHTML = ethKnown
    ? bar("Hispanic or Latino", pct(ethTot[0], ethKnown), `${fmt(ethTot[0])} of ${fmt(ethKnown)} participants with known ethnicity`) +
      bar("Not Hispanic or Latino", pct(ethTot[1], ethKnown), `${fmt(ethTot[1])} of ${fmt(ethKnown)} participants with known ethnicity`) +
      `<p class="note" style="margin-top:12px">${pct(ethTot[2], ethAll).toFixed(1)}% of participants had unknown ethnicity (${fmt(ethTot[2])} of ${fmt(ethAll)}). Based on ${fmt(eth.length)} of ${fmt(rows.length)} trials, the ones that reported ethnicity.</p>`
    : `<p class="empty">No trials in this view reported ethnicity in the standard categories.</p>`;

  const aged = rows.filter(r => r.ag != null && r.ag <= 100);
  const odd = rows.filter(r => r.ag != null && r.ag > 100).length;
  $("age").innerHTML = aged.length
    ? AGE_BINS.map(([name, lo, hi]) => {
        const k = aged.filter(r => r.ag >= lo && r.ag < hi).length;
        return bar(name, pct(k, aged.length), `${k} trials`, "gray");
      }).join("") +
      `<p class="note" style="margin-top:12px">Share of trials by their average age. Based on ${fmt(aged.length)} of ${fmt(rows.length)} trials. ${fmt(rows.length - aged.length - odd)} did not report an average age${odd ? `, and ${odd} reported an average over 100, which is likely an entry error and is not shown` : ""}.</p>`
    : `<p class="empty">No trials in this view reported an average age.</p>`;

  renderPPR();

  const custom = rows.filter(r => r.rf === "customized").length, none = rows.filter(r => r.rf === "none").length;
  $("reporting").innerHTML =
    bar("Standard race categories", pct(omb.length, rows.length), `${omb.length} trials`) +
    bar("Own race categories", pct(custom, rows.length), `${custom} trials`, "gray") +
    bar("Race not reported", pct(none, rows.length), `${none} trials`, "warn");

  const top = [...rows].sort((a, b) => (b.n || 0) - (a.n || 0)).slice(0, 50);
  const lbl = {omb:"Yes", customized:"Own categories", none:"No"};
  const alsoListed = r => {
    const others = condsByTrial[r.id].filter(c => c !== r.c).map(c => CONDS[c]);
    return others.length ? `<div class="also">Also listed under: ${others.join(", ")}</div>` : "";
  };
  $("trials").querySelector("tbody").innerHTML = top.map(r =>
    `<tr><td><a href="https://clinicaltrials.gov/study/${r.id}" target="_blank" rel="noopener">${r.id}</a><br>${(r.t || "").replace(/</g,"&lt;")}${alsoListed(r)}</td>
     <td>${(r.p || "n/a").replaceAll("PHASE","Phase ").replaceAll("|"," / ").replace("EARLY_Phase 1","Early Phase 1").replace("NA","n/a")}</td>
     <td>${r.y || ""}</td><td class="num">${r.n ? fmt(r.n) : ""}</td><td>${lbl[r.rf]}</td></tr>`).join("");
}

function renderPPR() {
  const rs = PPR.filter(r => r.condition === cond);
  if (!rs.length) {
    $("ppr").innerHTML = `<p class="empty">Patient data for ${CONDS[cond].toLowerCase()} has not been added yet.</p>`;
    return;
  }
  const vals = rs.map(r => +r.ppr).filter(v => v > 0);
  const max = Math.max(2, Math.ceil(Math.max(...vals) * 2) / 2);
  const x = v => (100 * v / max).toFixed(2) + "%";
  const ticks = [];
  for (let t = 0; t <= max + 1e-9; t += 0.5) ticks.push(`<span style="left:${x(t)}">${t.toFixed(1)}</span>`);
  const rowHtml = rs.map(r => {
    const has = r.ppr !== "";
    const detail = `${fmt(r.trial_participants)} participants in ${fmt(r.trials_used)} trials. ` +
      (r.largest_trial_share_pct !== "" ? `${r.largest_trial_share_pct}% are from the largest single trial.` : "");
    const plot = has
      ? `<div class="dot" style="left:${x(+r.ppr)}" title="Trial share ${r.trial_share_pct}%, patient share ${r.seer_share_pct}%"></div>`
      : "";
    const value = has ? (+r.ppr).toFixed(2) : (r.seer_group ? "Patient data pending" : "No matching patient group");
    const p1 = v => (+v).toFixed(1);
    const shares = has ? `Trials ${p1(r.trial_share_pct)}%, patients ${p1(r.seer_share_pct)}%. ` : `Trials ${p1(r.trial_share_pct)}%. `;
    return `<div class="ppr-row"><div class="ppr-label">${r.trial_group}</div>
      <div class="ppr-track"><div class="ref" style="left:${x(1)}"></div>${plot}</div>
      <div class="ppr-val">${value}</div>
      <div class="ppr-detail">${shares}${detail}</div></div>`;
  }).join("");
  $("ppr").innerHTML = `<div class="ppr-axis"><div></div><div class="ticks">${ticks.join("")}</div><div></div></div>` + rowHtml +
    `<p class="note" style="margin-top:12px">Patient data: NCI SEER new cases, 2019 to 2023. ${cond === "prostate_cancer" ? "Trials also listed under breast cancer are left out. " : ""}Hispanic or Latino uses the trials' ethnicity data. See "How to read this" for how groups are matched.</p>`;
}

$("conds").innerHTML = Object.entries(CONDS).map(([k, v]) => `<button role="tab" data-c="${k}">${v}</button>`).join("");
$("conds").addEventListener("click", e => { if (e.target.dataset.c) { cond = e.target.dataset.c; render(); } });
$("phase").addEventListener("change", render);
render();
