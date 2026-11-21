// Shared by every page: names, colors, number helpers, and the "data updated" text.
const CONDS = {breast_cancer:"Breast cancer", prostate_cancer:"Prostate cancer", type_2_diabetes:"Type 2 diabetes", heart_failure:"Heart failure"};
const RACES = ["American Indian or Alaska Native","Asian","Native Hawaiian or Other Pacific Islander","Black or African American","White","More than one race","Unknown or Not Reported"];
const UNKNOWN = RACES.indexOf("Unknown or Not Reported");
// Order shown in charts, largest groups first: White, Black, Asian, AI/AN, NHPI, More than one race.
const RACE_ORDER = [4, 3, 1, 0, 2, 5];
const RACE_SHORT = ["American Indian or Alaska Native","Asian","Native Hawaiian or Pacific Islander","Black or African American","White","More than one race"];
// [background, text] pairs. Text colors are chosen for at least 4.5:1 contrast on their background.
const RACE_COLOR = {4:["#1f5fa8","#fff"], 3:["#a84300","#fff"], 1:["#0b7a5a","#fff"], 0:["#8e3b8e","#fff"], 2:["#e0a800","#14202b"], 5:["#5aa9d6","#14202b"]};
const data = window.TRIALS || [];
const PPR = window.PPR || [];
const $ = id => document.getElementById(id);
const fmt = n => Math.round(n).toLocaleString();
const pct = (a, b) => b ? (100 * a / b) : 0;
const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

// Race totals for a set of trials that used the standard race categories.
function raceTotals(rows) {
  const omb = rows.filter(r => r.rf === "omb");
  const tot = RACES.map((_, i) => omb.reduce((s, r) => s + (r.r[i] || 0), 0));
  const known = tot.reduce((a, b) => a + b, 0) - tot[UNKNOWN];
  return {omb, tot, known, unknown: tot[UNKNOWN], all: known + tot[UNKNOWN]};
}

// A bar row. Colors are never the only signal: the label and value are always text.
function bar(label, p, detail, opts = {}) {
  const style = opts.color ? ` style="--c:${opts.color}"` : "";
  return `<li class="bar"><span class="name">${esc(label)}</span>` +
    `<span class="track" aria-hidden="true"><span class="fill ${opts.cls || ""}" style="width:${Math.max(p, 0.6)}%;display:block;${opts.color ? "--c:" + opts.color : ""}"></span></span>` +
    `<span class="pct">${p.toFixed(1)}%</span>` +
    (detail ? `<span class="tag">${esc(detail)}</span>` : "") + `</li>`;
}

// "Data last updated": a full UTC time from the daily refresh, or a date for a manual snapshot.
function updatedText(v) {
  if (!v) return "not recorded";
  const dateOnly = v.length === 10;
  const d = new Date(dateOnly ? v + "T00:00:00Z" : v);
  if (isNaN(d)) return v;
  const day = d.toLocaleDateString("en-US", {year: "numeric", month: "long", day: "numeric", timeZone: "UTC"});
  if (dateOnly) return day;
  return `${day}, ${d.toLocaleTimeString("en-GB", {hour: "2-digit", minute: "2-digit", timeZone: "UTC"})} UTC`;
}
document.querySelectorAll(".data-updated").forEach(e => { e.textContent = updatedText(window.DATA_UPDATED); });

// One row per trial, ignoring which condition it is listed under.
function uniqueTrials() {
  const seen = new Map();
  data.forEach(r => { if (!seen.has(r.id)) seen.set(r.id, r); });
  return [...seen.values()];
}

// How complete the data is for a set of trials. Each charted variable only uses trials that have it.
function completeness(rows) {
  const n = rows.length;
  const count = f => rows.filter(f).length;
  return {
    n,
    race: count(r => r.rf === "omb"), own: count(r => r.rf === "customized"), none: count(r => r.rf === "none"),
    eth: count(r => r.e), age: count(r => r.ag != null && r.ag <= 100),
    us: count(r => r.uo === 1), noLoc: count(r => r.uo == null)
  };
}
