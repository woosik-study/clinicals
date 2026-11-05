const CONDS = {breast_cancer:"Breast cancer", prostate_cancer:"Prostate cancer", type_2_diabetes:"Type 2 diabetes", heart_failure:"Heart failure"};
const RACES = ["American Indian or Alaska Native","Asian","Native Hawaiian or Other Pacific Islander","Black or African American","White","More than one race","Unknown or Not Reported"];
const data = window.TRIALS || [];
let cond = "breast_cancer";
const $ = id => document.getElementById(id);
const fmt = n => Math.round(n).toLocaleString();
const pct = (a, b) => b ? (100 * a / b) : 0;

function bar(label, p, title, cls="") {
  return `<div class="bar" title="${title}"><span>${label}</span><div class="track"><div class="fill ${cls}" style="width:${Math.max(p,0.5)}%"></div></div><span class="pct">${p.toFixed(1)}%</span></div>`;
}

function render() {
  const phase = $("phase").value;
  const rows = data.filter(r => r.c === cond && (!phase || (r.p || "").split("|").includes(phase)));
  document.querySelectorAll("#conds button").forEach(b => b.setAttribute("aria-selected", b.dataset.c === cond));

  if (!rows.length) {
    $("stats").innerHTML = `<div class="stat"><div class="l">No trials match this filter.</div></div>`;
    $("race").innerHTML = $("reporting").innerHTML = `<p class="empty">No data.</p>`;
    $("trials").querySelector("tbody").innerHTML = "";
    return;
  }
  const omb = rows.filter(r => r.rf === "omb");
  const anyRace = rows.filter(r => r.rf !== "none").length;
  const raceTot = RACES.map((_, i) => omb.reduce((s, r) => s + (r.r[i] || 0), 0));
  const allRace = raceTot.reduce((a, b) => a + b, 0);
  const sx = rows.filter(r => r.fe != null || r.ma != null);
  const fe = sx.reduce((s, r) => s + (r.fe || 0), 0), ma = sx.reduce((s, r) => s + (r.ma || 0), 0);
  const people = rows.reduce((s, r) => s + (r.n || 0), 0);

  $("stats").innerHTML = [
    [fmt(rows.length), "trials with posted results"],
    [fmt(people), "participants"],
    [pct(anyRace, rows.length).toFixed(0) + "%", "of trials reported race"],
    [(fe + ma) ? pct(fe, fe + ma).toFixed(0) + "%" : "n/a", "of participants were female"],
  ].map(([v, l]) => `<div class="stat"><div class="v">${v}</div><div class="l">${l}</div></div>`).join("");

  $("race").innerHTML = allRace
    ? RACES.map((name, i) => bar(name, pct(raceTot[i], allRace), `${fmt(raceTot[i])} of ${fmt(allRace)} participants`, name.startsWith("Unknown") ? "gray" : "")).join("")
      + `<p class="note" style="margin-top:12px">Based on ${fmt(omb.length)} trials and ${fmt(allRace)} participants.</p>`
    : `<p class="empty">No trials in this view reported race in the standard categories.</p>`;

  const custom = rows.filter(r => r.rf === "customized").length, none = rows.filter(r => r.rf === "none").length;
  $("reporting").innerHTML =
    bar("Standard race categories", pct(omb.length, rows.length), `${omb.length} trials`) +
    bar("Own race categories", pct(custom, rows.length), `${custom} trials`, "gray") +
    bar("Race not reported", pct(none, rows.length), `${none} trials`, "warn");

  const top = [...rows].sort((a, b) => (b.n || 0) - (a.n || 0)).slice(0, 50);
  const lbl = {omb:"Yes", customized:"Own categories", none:"No"};
  $("trials").querySelector("tbody").innerHTML = top.map(r =>
    `<tr><td><a href="https://clinicaltrials.gov/study/${r.id}" target="_blank" rel="noopener">${r.id}</a><br>${(r.t || "").replace(/</g,"&lt;")}</td>
     <td>${(r.p || "n/a").replaceAll("PHASE","Phase ").replaceAll("|"," / ").replace("EARLY_Phase 1","Early Phase 1").replace("NA","n/a")}</td>
     <td>${r.y || ""}</td><td class="num">${r.n ? fmt(r.n) : ""}</td><td>${lbl[r.rf]}</td></tr>`).join("");
}

$("conds").innerHTML = Object.entries(CONDS).map(([k, v]) => `<button role="tab" data-c="${k}">${v}</button>`).join("");
$("conds").addEventListener("click", e => { if (e.target.dataset.c) { cond = e.target.dataset.c; render(); } });
$("phase").addEventListener("change", render);
render();
