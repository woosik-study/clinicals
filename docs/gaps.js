// Data gaps page: how complete the trial data is, and which patient comparisons are still missing.
const cell = (k, n) => {
  const p = pct(k, n);
  return `<td><div class="cell"><b>${p.toFixed(0)}%</b><span class="mini" aria-hidden="true"><i style="width:${p}%"></i></span></div><span class="muted" style="font-size:.85rem">${fmt(k)} of ${fmt(n)}</span></td>`;
};
const cols = [
  ["Race, standard categories", c => c.race],
  ["Race, own categories", c => c.own],
  ["Race not reported", c => c.none],
  ["Ethnicity reported", c => c.eth],
  ["Average age reported", c => c.age],
  ["All sites in the US", c => c.us],
];
$("matrix").innerHTML = `<caption class="sr">Share of each condition's trials that have each piece of information</caption><thead><tr><th scope="col">Condition</th>` +
  cols.map(([name]) => `<th scope="col">${name}</th>`).join("") + `</tr></thead><tbody>` +
  Object.entries(CONDS).map(([key, name]) => {
    const rows = data.filter(r => r.c === key), c = completeness(rows);
    return `<tr><th scope="row">${name}<div class="muted" style="font-weight:400;font-size:.85rem">${fmt(rows.length)} trials</div></th>${cols.map(([, f]) => cell(f(c), c.n)).join("")}</tr>`;
  }).join("") + `</tbody>`;

const label = {computed: ["Shown", "ok"], pending: ["Waiting for patient data", "wait"], no_patient_group: ["No matching patient group", "none"]};
$("patient").innerHTML = `<caption class="sr">Patient comparison status for each condition and group</caption><thead><tr><th scope="col">Condition</th><th scope="col">Group</th><th scope="col">Status</th></tr></thead><tbody>` +
  Object.entries(CONDS).map(([key, name]) => {
    const rs = PPR.filter(r => r.condition === key);
    return rs.map((r, i) => {
      const [text, cls] = label[r.status] || [r.status, "none"];
      return `<tr>${i === 0 ? `<th scope="row" rowspan="${rs.length}">${name}</th>` : ""}<td>${esc(r.trial_group)}</td><td><span class="status ${cls}">${text}</span></td></tr>`;
    }).join("");
  }).join("") + `</tbody>`;
