# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Orgen ROI Calculator",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .stApp { background: #0A0A14; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', sans-serif;
    background: #0A0A14;
    color: #E8E8F0;
    min-height: 100vh;
    padding: 0 0 60px 0;
    direction: rtl;
  }
  .hero { text-align: center; padding: 52px 24px 36px; }
  .hero h1 {
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg, #7C6FF7, #00D9C8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 10px;
    letter-spacing: -1px;
  }
  .hero p { color: #7A7A9A; font-size: 17px; }
  .page { max-width: 860px; margin: 0 auto; padding: 0 24px; }
  .section { margin-bottom: 28px; }
  .section-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #7C6FF7;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .section-title::after { content: ''; flex: 1; height: 1px; background: #1E1E32; }
  .card { background: #131320; border: 1px solid #1E1E32; border-radius: 16px; padding: 24px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  label.field-label { display: block; font-size: 12px; font-weight: 500; color: #7A7A9A; margin-bottom: 7px; }
  input[type=text], input[type=number], select {
    width: 100%;
    background: #0E0E1C;
    border: 1px solid #252540;
    border-radius: 10px;
    padding: 10px 14px;
    color: #E8E8F0;
    font-size: 14px;
    font-family: inherit;
    outline: none;
    transition: border-color .2s;
    appearance: none;
    -webkit-appearance: none;
  }
  input:focus, select:focus { border-color: #7C6FF7; }
  select {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%237A7A9A' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: left 12px center;
    padding-left: 34px;
  }
  .toggle-wrap { display: flex; gap: 8px; margin-bottom: 20px; }
  .toggle-btn {
    flex: 1; padding: 10px; border-radius: 10px;
    border: 1px solid #252540; background: transparent;
    color: #7A7A9A; font-size: 13px; font-weight: 500;
    font-family: inherit; cursor: pointer; transition: all .2s;
  }
  .toggle-btn.active { background: #1C1A3A; border-color: #7C6FF7; color: #E8E8F0; }
  .model-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
  .model-pill {
    padding: 9px 10px; border-radius: 10px;
    border: 1px solid #252540; background: transparent;
    color: #7A7A9A; font-size: 12px; font-weight: 500;
    font-family: inherit; cursor: pointer; transition: all .2s; text-align: center;
  }
  .model-pill.active { background: #1C1A3A; border-color: #7C6FF7; color: #C4BFFF; }
  .user-card { display: flex; flex-direction: column; gap: 6px; }
  .user-card-header { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
  .user-icon {
    width: 32px; height: 32px; background: #1C1A3A;
    border-radius: 8px; display: flex; align-items: center;
    justify-content: center; font-size: 15px;
  }
  .user-title { font-size: 14px; font-weight: 600; color: #E8E8F0; }
  .user-desc { font-size: 12px; color: #7A7A9A; margin-bottom: 8px; }
  .counter-wrap { display: flex; align-items: center; gap: 12px; }
  .counter-btn {
    width: 36px; height: 36px; border-radius: 8px;
    border: 1px solid #252540; background: #0E0E1C;
    color: #C4BFFF; font-size: 20px; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: all .15s; flex-shrink: 0;
  }
  .counter-btn:hover { border-color: #7C6FF7; background: #1C1A3A; }
  .counter-input {
    flex: 1; text-align: center; font-size: 22px; font-weight: 700;
    color: #E8E8F0; border: 1px solid #252540; border-radius: 10px; padding: 8px;
  }
  .line-header { display: grid; grid-template-columns: 2fr 90px 110px 36px; gap: 8px; margin-bottom: 8px; }
  .line-header span { font-size: 11px; color: #7A7A9A; font-weight: 500; }
  .line-row { display: grid; grid-template-columns: 2fr 90px 110px 36px; gap: 8px; margin-bottom: 8px; align-items: center; }
  .del-btn {
    width: 36px; height: 36px; border-radius: 8px;
    border: 1px solid #252540; background: transparent;
    color: #7A7A9A; font-size: 16px; cursor: pointer;
    display: flex; align-items: center; justify-content: center; transition: all .15s;
  }
  .del-btn:hover { border-color: #E05C5C; color: #E05C5C; background: #1A0E0E; }
  .add-btn {
    margin-top: 8px; padding: 9px 16px; border-radius: 10px;
    border: 1px dashed #252540; background: transparent;
    color: #7A7A9A; font-size: 13px; font-family: inherit;
    cursor: pointer; transition: all .2s; width: 100%;
  }
  .add-btn:hover { border-color: #7C6FF7; color: #C4BFFF; background: #13132A; }
  .results-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 20px; }
  .result-card {
    background: #13132A; border: 1px solid #1E1E38;
    border-radius: 14px; padding: 20px 16px; text-align: center;
  }
  .result-card.highlight {
    background: linear-gradient(145deg, #0E1F1A, #13132A);
    border-color: #00B894;
  }
  .result-label { font-size: 12px; color: #7A7A9A; margin-bottom: 10px; }
  .result-val { font-size: 28px; font-weight: 700; color: #E8E8F0; }
  .result-val.green { color: #00C896; }
  .result-pct { font-size: 13px; color: #00C896; margin-top: 4px; }
  .annual-box {
    background: #13132A; border: 1px solid #1E1E38;
    border-radius: 16px; padding: 32px 24px; text-align: center;
  }
  .annual-label { font-size: 14px; color: #7A7A9A; margin-bottom: 10px; }
  .annual-val {
    font-size: 52px; font-weight: 800;
    background: linear-gradient(90deg, #7C6FF7, #00D9C8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; letter-spacing: -2px;
  }
  details { margin-top: 16px; }
  details summary {
    font-size: 13px; color: #7A7A9A; cursor: pointer;
    list-style: none; display: flex; align-items: center; gap: 6px; padding: 10px 0;
  }
  details summary::before { content: "\\25B8"; font-size: 10px; transition: transform .15s; }
  details[open] summary::before { transform: rotate(90deg); }
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th { color: #7A7A9A; font-weight: 500; text-align: right; padding: 6px 10px 10px; border-bottom: 1px solid #1E1E32; }
  td { padding: 8px 10px; border-bottom: 1px solid #1E1E32; color: #C8C8E0; }
  tr:last-child td { border-bottom: none; font-weight: 600; color: #E8E8F0; }
</style>
</head>
<body>

<div class="hero">
  <h1>Orgen ROI Calculator</h1>
  <p>&#1490;&#1500;&#1492; &#1499;&#1502;&#1492; &#1514;&#1495;&#1505;&#1493;&#1498; &#1506;&#1501; Orgen</p>
</div>

<div class="page">

  <div class="section">
    <div class="section-title">&#1513;&#1500;&#1489; 1 &mdash; &#1508;&#1512;&#1496;&#1497; &#1492;&#1495;&#1489;&#1512;&#1492;</div>
    <div class="card grid-3">
      <div>
        <label class="field-label">&#1513;&#1501; &#1492;&#1495;&#1489;&#1512;&#1492;</label>
        <input type="text" id="companyName" placeholder="Acme Corp">
      </div>
      <div>
        <label class="field-label">&#1514;&#1506;&#1513;&#1497;&#1497;&#1492;</label>
        <select id="industry">
          <option>&#1496;&#1499;&#1504;&#1493;&#1500;&#1493;&#1490;&#1497;&#1492;</option>
          <option>&#1508;&#1497;&#1504;&#1504;&#1505;&#1497;&#1501;</option>
          <option>&#1489;&#1512;&#1497;&#1488;&#1493;&#1514;</option>
          <option>&#1495;&#1497;&#1504;&#1493;&#1498;</option>
          <option>&#1511;&#1502;&#1506;&#1493;&#1504;&#1488;&#1493;&#1514;</option>
          <option>&#1488;&#1495;&#1512;</option>
        </select>
      </div>
      <div>
        <label class="field-label">&#1490;&#1493;&#1491;&#1500; &#1495;&#1489;&#1512;&#1492;</label>
        <select id="companySize">
          <option>1-50</option><option>51-200</option>
          <option selected>201-500</option>
          <option>501-1000</option><option>1000+</option>
        </select>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">&#1513;&#1500;&#1489; 2 &mdash; &#1502;&#1513;&#1514;&#1502;&#1513;&#1497;&#1501;</div>
    <div class="card grid-2">
      <div class="user-card">
        <div class="user-card-header">
          <div class="user-icon">&#128100;</div>
          <div>
            <div class="user-title">&#1502;&#1513;&#1514;&#1502;&#1513;&#1497;&#1501; &#1512;&#1490;&#1497;&#1500;&#1497;&#1501;</div>
            <div class="user-desc">&#1506;&#1493;&#1489;&#1491;&#1497;&#1501; &#1513;&#1502;&#1513;&#1514;&#1502;&#1513;&#1497;&#1501; &#1489;&#1499;&#1500;&#1497; AI &#1500;&#1497;&#1493;&#1502;&#1497;&#1493;&#1501;</div>
          </div>
        </div>
        <div class="counter-wrap">
          <button class="counter-btn" onclick="change('regular',-1)">&#8722;</button>
          <input class="counter-input" type="number" id="regular" value="30" min="0" oninput="update()">
          <button class="counter-btn" onclick="change('regular',1)">+</button>
        </div>
      </div>
      <div class="user-card">
        <div class="user-card-header">
          <div class="user-icon">&#128187;</div>
          <div>
            <div class="user-title">&#1502;&#1508;&#1514;&#1495;&#1497;&#1501;</div>
            <div class="user-desc">&#1502;&#1508;&#1514;&#1495;&#1497;&#1501; &#1513;&#1502;&#1513;&#1514;&#1502;&#1513;&#1497;&#1501; &#1489;-API</div>
          </div>
        </div>
        <div class="counter-wrap">
          <button class="counter-btn" onclick="change('devs',-1)">&#8722;</button>
          <input class="counter-input" type="number" id="devs" value="10" min="0" oninput="update()">
          <button class="counter-btn" onclick="change('devs',1)">+</button>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">&#1513;&#1500;&#1489; 3 &mdash; &#1492;&#1493;&#1510;&#1488;&#1493;&#1514; &#1504;&#1493;&#1499;&#1495;&#1497;&#1493;&#1514;</div>
    <div class="toggle-wrap">
      <button class="toggle-btn active" id="btnAuto" onclick="setMode('auto')">&#1495;&#1497;&#1513;&#1493;&#1489; &#1488;&#1493;&#1496;&#1493;&#1502;&#1496;&#1497;</button>
      <button class="toggle-btn" id="btnManual" onclick="setMode('manual')">&#1492;&#1494;&#1504;&#1492; &#1497;&#1491;&#1504;&#1497;&#1514;</button>
    </div>
    <div id="autoSection" class="card">
      <label class="field-label" style="margin-bottom:14px">&#1488;&#1497;&#1494;&#1492; &#1502;&#1493;&#1491;&#1500; AI &#1502;&#1513;&#1514;&#1502;&#1513;&#1514; &#1492;&#1495;&#1489;&#1512;&#1492; &#1489;&#1506;&#1497;&#1511;&#1512; &#1492;&#1497;&#1493;&#1501;?</label>
      <div class="model-grid" id="modelGrid"></div>
    </div>
    <div id="manualSection" class="card" style="display:none">
      <div class="line-header">
        <span>&#1514;&#1497;&#1488;&#1493;&#1512;</span>
        <span>&#1505;&#1493;&#1490;</span>
        <span>&#1506;&#1500;&#1493;&#1514; ($)</span>
        <span></span>
      </div>
      <div id="lineItems"></div>
      <button class="add-btn" onclick="addLine()">+ &#1492;&#1493;&#1505;&#1507; &#1513;&#1493;&#1512;&#1492;</button>
    </div>
  </div>

  <div class="section">
    <div class="section-title">&#1492;&#1514;&#1493;&#1510;&#1488;&#1493;&#1514; &#1513;&#1500;&#1498;</div>
    <div class="results-grid">
      <div class="result-card">
        <div class="result-label">&#1506;&#1500;&#1493;&#1514; &#1504;&#1493;&#1499;&#1495;&#1497;&#1514;</div>
        <div class="result-val" id="rBefore">&mdash;</div>
      </div>
      <div class="result-card highlight">
        <div class="result-label">&#1495;&#1497;&#1505;&#1499;&#1493;&#1503; &#1506;&#1501; Orgen</div>
        <div class="result-val green" id="rSavings">&mdash;</div>
        <div class="result-pct" id="rPct"></div>
      </div>
      <div class="result-card">
        <div class="result-label">&#1506;&#1500;&#1493;&#1514; &#1506;&#1501; Orgen</div>
        <div class="result-val" id="rAfter">&mdash;</div>
      </div>
    </div>
    <div class="annual-box">
      <div class="annual-label">&#1495;&#1497;&#1505;&#1499;&#1493;&#1503; &#1513;&#1504;&#1514;&#1497; &#1502;&#1513;&#1493;&#1506;&#1512;</div>
      <div class="annual-val" id="rAnnual">&mdash;</div>
    </div>
    <details id="breakdownDetails" style="display:none">
      <summary>&#1508;&#1497;&#1512;&#1493;&#1496; &#1502;&#1500;&#1488;</summary>
      <div id="breakdownContent"></div>
    </details>
  </div>

</div>

<script>
const MODEL_PRICES = {
  "Claude Opus":   {input:15.00, output:75.00},
  "Claude Sonnet": {input:3.00,  output:15.00},
  "Claude Haiku":  {input:0.25,  output:1.25},
  "GPT-4o":        {input:2.50,  output:10.00},
  "GPT-4o mini":   {input:0.15,  output:0.60},
  "Gemini Flash":  {input:0.075, output:0.30},
};
const ROUTING = {
  regular: [{model:"Gemini Flash",share:.50},{model:"Claude Haiku",share:.40},{model:"Claude Sonnet",share:.10}],
  dev:     [{model:"Claude Haiku",share:.60},{model:"Claude Sonnet",share:.30},{model:"Claude Opus",share:.10}],
};
const PLATFORM_FEE = 2000;

let currentModel = "Claude Sonnet";
let mode = "auto";
let lines = [{desc:"",type:"API",cost:0}];

function fmt(v) {
  if (v <= 0) return "$0";
  if (v >= 1e6) return "$" + (v/1e6).toFixed(1) + "M";
  if (v >= 1000) return "$" + Math.round(v).toLocaleString();
  return "$" + Math.round(v);
}

function change(id, delta) {
  const el = document.getElementById(id);
  el.value = Math.max(0, (parseInt(el.value)||0) + delta);
  update();
}

function calcRouting(tokens, routing, ratio) {
  return routing.reduce((s,r) => {
    const p = MODEL_PRICES[r.model], t = tokens * r.share;
    return s + (t*ratio.input/1e6)*p.input + (t*ratio.output/1e6)*p.output;
  }, 0);
}

function update() {
  const reg = Math.max(0, parseInt(document.getElementById("regular").value)||0);
  const dev = Math.max(0, parseInt(document.getElementById("devs").value)||0);
  let before, after, savings, pct;

  if (mode === "auto") {
    const p = MODEL_PRICES[currentModel];
    const tokReg = reg * 18500 * 22;
    const tokDev = dev * 121000 * 22;
    const bReg = reg > 0 ? (tokReg*.40/1e6)*p.input + (tokReg*.60/1e6)*p.output : 0;
    const bDev = dev > 0 ? (tokDev*.50/1e6)*p.input + (tokDev*.50/1e6)*p.output : 0;
    const aReg = reg > 0 ? calcRouting(tokReg, ROUTING.regular, {input:.40,output:.60}) : 0;
    const aDev = dev > 0 ? calcRouting(tokDev, ROUTING.dev,     {input:.50,output:.50}) : 0;
    before = bReg + bDev;
    after  = aReg + aDev + PLATFORM_FEE;
    savings = before - after;
    pct = before > 0 ? savings/before : 0;
    if (before > 0) {
      buildTable(
        ["\u05E7\u05D8\u05D2\u05D5\u05E8\u05D9\u05D4","\u05DC\u05E4\u05E0\u05D9 Orgen","\u05D0\u05D7\u05E8\u05D9 Orgen","\u05D7\u05D9\u05E1\u05DB\u05D5\u05DF"],
        [
          ["\u05DE\u05E9\u05EA\u05DE\u05E9\u05D9\u05DD \u05E8\u05D2\u05D9\u05DC\u05D9\u05DD", fmt(bReg), fmt(aReg), fmt(bReg-aReg)],
          ["\u05DE\u05E4\u05EA\u05D7\u05D9\u05DD", fmt(bDev), fmt(aDev), fmt(bDev-aDev)],
          ["Platform Fee", "&mdash;", fmt(PLATFORM_FEE), "&mdash;"],
          ["\u05E1\u05D4\"\u05DB", fmt(before), fmt(after), fmt(before-after)],
        ]
      );
    }
  } else {
    const valid = lines.filter(l => l.cost > 0);
    let tot = 0, sav = 0;
    const bd = valid.map(l => {
      const sp = l.type === "API" ? .45 : .20;
      const sa = l.cost * sp;
      tot += l.cost; sav += sa;
      return {...l, sp, sa, costAfter: l.cost - sa};
    });
    before = tot; savings = sav; after = tot - sav;
    pct = tot > 0 ? sav/tot : 0;
    if (before > 0 && bd.length) {
      const rows = bd.map(i => [i.desc||"\u05DC\u05DC\u05D0 \u05E9\u05DD", i.type, fmt(i.cost), Math.round(i.sp*100)+"%", fmt(i.costAfter)]);
      rows.push(["\u05E1\u05D4\"\u05DB","",fmt(tot),"",fmt(after)]);
      buildTable(["\u05EA\u05D9\u05D0\u05D5\u05E8","\u05E1\u05D5\u05D2","\u05DC\u05E4\u05E0\u05D9","\u05D7\u05D9\u05E1\u05DB\u05D5\u05DF","\u05D0\u05D7\u05E8\u05D9"], rows);
    }
  }

  document.getElementById("rBefore").innerHTML  = before > 0 ? fmt(before) : "&mdash;";
  document.getElementById("rAfter").innerHTML   = before > 0 ? fmt(after)  : "&mdash;";
  document.getElementById("rSavings").innerHTML = before > 0 ? fmt(savings): "&mdash;";
  document.getElementById("rPct").textContent   = before > 0 ? Math.round(pct*100) + "% \u05D7\u05D9\u05E1\u05DB\u05D5\u05DF" : "";
  document.getElementById("rAnnual").innerHTML  = before > 0 ? fmt(savings * 12) : "&mdash;";
  document.getElementById("breakdownDetails").style.display = before > 0 ? "block" : "none";
}

function buildTable(headers, rows) {
  let h = "<table><thead><tr>" + headers.map(x=>`<th>${x}</th>`).join("") + "</tr></thead><tbody>";
  rows.forEach(r => { h += "<tr>" + r.map(c=>`<td>${c}</td>`).join("") + "</tr>"; });
  document.getElementById("breakdownContent").innerHTML = h + "</tbody></table>";
}

function setMode(m) {
  mode = m;
  document.getElementById("autoSection").style.display  = m==="auto"   ? "block" : "none";
  document.getElementById("manualSection").style.display = m==="manual" ? "block" : "none";
  document.getElementById("btnAuto").classList.toggle("active",   m==="auto");
  document.getElementById("btnManual").classList.toggle("active", m==="manual");
  update();
}

function buildModels() {
  document.getElementById("modelGrid").innerHTML = Object.keys(MODEL_PRICES).map(name =>
    `<button class="model-pill ${name===currentModel?"active":""}" onclick="selectModel('${name}')">${name}</button>`
  ).join("");
}

function selectModel(name) { currentModel = name; buildModels(); update(); }

function renderLines() {
  document.getElementById("lineItems").innerHTML = lines.map((l,i) => `
    <div class="line-row">
      <input type="text" value="${l.desc}" placeholder="\u05DC\u05D3\u05D5\u05D2\u05DE\u05D0: Claude API"
        oninput="lines[${i}].desc=this.value">
      <select onchange="lines[${i}].type=this.value;update()">
        <option value="API" ${l.type==="API"?"selected":""}>API</option>
        <option value="mnuy" ${l.type==="mnuy"?"selected":""}>\u05DE\u05E0\u05D5\u05D9</option>
      </select>
      <input type="number" value="${l.cost||''}" min="0" step="100" placeholder="0"
        oninput="lines[${i}].cost=parseFloat(this.value)||0;update()">
      <button class="del-btn" onclick="delLine(${i})">&#10005;</button>
    </div>
  `).join("");
}

function addLine()  { lines.push({desc:"",type:"API",cost:0}); renderLines(); }
function delLine(i) { lines.splice(i,1); if(!lines.length) lines=[{desc:"",type:"API",cost:0}]; renderLines(); update(); }

buildModels();
renderLines();
update();
</script>
</body>
</html>
""", height=1450, scrolling=True)
