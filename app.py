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
<html lang="en">
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
}

/* ── RESULTS PAGE ── */
.results-page {
  max-width: 860px;
  margin: 0 auto;
  padding: 40px 24px 80px;
  opacity: 0;
  transition: opacity .5s ease;
}
.results-page.visible { opacity: 1; }

.hero { text-align: center; margin-bottom: 40px; }
.hero h1 {
  font-size: 40px; font-weight: 800;
  background: linear-gradient(90deg, #7C6FF7, #00D9C8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; letter-spacing: -1px; margin-bottom: 8px;
}
.hero p { color: #7A7A9A; font-size: 16px; }

.company-badge {
  display: inline-flex; align-items: center; gap: 8px;
  background: #1C1A3A; border: 1px solid #7C6FF7;
  border-radius: 20px; padding: 6px 18px;
  font-size: 13px; color: #C4BFFF; margin-bottom: 32px;
}

.section-title {
  font-size: 11px; font-weight: 600; letter-spacing: .1em;
  text-transform: uppercase; color: #7C6FF7; margin-bottom: 14px;
  display: flex; align-items: center; gap: 8px;
}
.section-title::after { content: ''; flex: 1; height: 1px; background: #1E1E32; }

.results-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 20px; }
.result-card {
  background: #131320; border: 1px solid #1E1E32;
  border-radius: 14px; padding: 24px 16px; text-align: center;
}
.result-card.highlight {
  background: linear-gradient(145deg, #0E1F1A, #131320);
  border-color: #00B894;
}
.result-label { font-size: 12px; color: #7A7A9A; margin-bottom: 10px; }
.result-val { font-size: 30px; font-weight: 700; color: #E8E8F0; }
.result-val.green { color: #00C896; }
.result-pct { font-size: 13px; color: #00C896; margin-top: 5px; }

.annual-box {
  background: #131320; border: 1px solid #1E1E32;
  border-radius: 16px; padding: 36px 24px; text-align: center; margin-bottom: 20px;
}
.annual-label { font-size: 14px; color: #7A7A9A; margin-bottom: 10px; }
.annual-val {
  font-size: 56px; font-weight: 800;
  background: linear-gradient(90deg, #7C6FF7, #00D9C8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; letter-spacing: -2px;
}

.summary-grid {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 10px; margin-bottom: 20px;
}
.summary-item {
  background: #131320; border: 1px solid #1E1E32;
  border-radius: 12px; padding: 14px 16px;
}
.summary-key { font-size: 11px; color: #7A7A9A; margin-bottom: 4px; }
.summary-val { font-size: 14px; font-weight: 600; color: #E8E8F0; }

details { margin-top: 4px; }
details summary {
  font-size: 13px; color: #7A7A9A; cursor: pointer;
  list-style: none; display: flex; align-items: center; gap: 6px; padding: 10px 0;
}
details summary::before { content: "\25B8"; font-size: 10px; transition: transform .15s; }
details[open] summary::before { transform: rotate(90deg); }
table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
th { color: #7A7A9A; font-weight: 500; text-align: left; padding: 6px 10px 10px; border-bottom: 1px solid #1E1E32; }
td { padding: 8px 10px; border-bottom: 1px solid #1E1E32; color: #C8C8E0; }
tr:last-child td { border-bottom: none; font-weight: 600; color: #E8E8F0; }

.restart-btn {
  display: block; width: 100%; margin-top: 20px;
  padding: 13px; border-radius: 12px;
  border: 1px solid #252540; background: transparent;
  color: #7A7A9A; font-size: 14px; font-family: inherit;
  cursor: pointer; transition: all .2s;
}
.restart-btn:hover { border-color: #7C6FF7; color: #C4BFFF; background: #13132A; }

/* ══ MODAL OVERLAY ══ */
.overlay {
  position: fixed; inset: 0;
  background: rgba(5,5,15,.85);
  backdrop-filter: blur(6px);
  display: flex; align-items: center; justify-content: center;
  z-index: 1000;
  transition: opacity .4s ease;
}
.overlay.hidden { opacity: 0; pointer-events: none; }

/* ══ MODAL BOX ══ */
.modal {
  background: #111120;
  border: 1px solid #1E1E38;
  border-radius: 20px;
  width: 520px;
  max-width: calc(100vw - 32px);
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 32px 80px rgba(0,0,0,.6);
  animation: slideUp .35s ease;
}
@keyframes slideUp {
  from { transform: translateY(24px); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}

/* ── PROGRESS ── */
.progress-wrap { padding: 24px 28px 0; }
.step-labels { display: flex; justify-content: space-between; margin-bottom: 8px; }
.step-label { font-size: 11px; color: #7A7A9A; text-align: center; flex: 1; }
.step-label.active { color: #C4BFFF; font-weight: 600; }
.progress-steps { display: flex; align-items: center; gap: 0; margin-bottom: 4px; }
.step-dot {
  width: 28px; height: 28px; border-radius: 50%;
  border: 2px solid #252540; background: #0E0E1C;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 600; color: #7A7A9A;
  flex-shrink: 0; transition: all .3s; z-index: 1;
}
.step-dot.active { border-color: #7C6FF7; background: #7C6FF7; color: #fff; }
.step-dot.done   { border-color: #00C896; background: #00C896; color: #fff; }
.step-line { flex: 1; height: 2px; background: #1E1E32; transition: background .3s; }
.step-line.done { background: #00C896; }

/* ── MODAL BODY ── */
.modal-body { padding: 20px 28px 28px; }
.modal-title { font-size: 20px; font-weight: 700; color: #E8E8F0; margin-bottom: 6px; }
.modal-sub   { font-size: 13px; color: #7A7A9A; margin-bottom: 24px; }

/* ── FORM ── */
.field { margin-bottom: 16px; }
label.fl { display: block; font-size: 12px; font-weight: 500; color: #7A7A9A; margin-bottom: 7px; }
input[type=text], input[type=number], select {
  width: 100%; background: #0E0E1C;
  border: 1px solid #252540; border-radius: 10px;
  padding: 11px 14px; color: #E8E8F0;
  font-size: 14px; font-family: inherit; outline: none;
  transition: border-color .2s;
  appearance: none; -webkit-appearance: none;
}
input:focus, select:focus { border-color: #7C6FF7; }
select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%237A7A9A' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 34px;
}
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

/* ── USER BLOCKS ── */
.user-block {
  background: #0E0E1C; border: 1px solid #1E1E32;
  border-radius: 12px; padding: 16px; margin-bottom: 12px;
}
.user-block-header { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.user-icon { font-size: 20px; }
.user-info-title { font-size: 14px; font-weight: 600; color: #E8E8F0; }
.user-info-desc  { font-size: 12px; color: #7A7A9A; }
.counter-wrap { display: flex; align-items: center; gap: 12px; }
.cbtn {
  width: 36px; height: 36px; border-radius: 8px;
  border: 1px solid #252540; background: #131320;
  color: #C4BFFF; font-size: 20px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all .15s; flex-shrink: 0;
}
.cbtn:hover { border-color: #7C6FF7; background: #1C1A3A; }
.cinput {
  flex: 1; text-align: center; font-size: 24px; font-weight: 700;
  color: #E8E8F0; border: 1px solid #252540;
  border-radius: 10px; padding: 8px; background: #0A0A14;
}

/* ── TOGGLE ── */
.toggle-wrap { display: flex; gap: 8px; margin-bottom: 16px; }
.tbtn {
  flex: 1; padding: 10px; border-radius: 10px;
  border: 1px solid #252540; background: transparent;
  color: #7A7A9A; font-size: 13px; font-weight: 500;
  font-family: inherit; cursor: pointer; transition: all .2s;
}
.tbtn.active { background: #1C1A3A; border-color: #7C6FF7; color: #E8E8F0; }

/* ── MODEL PILLS ── */
.model-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 4px; }
.mpill {
  padding: 9px 6px; border-radius: 10px;
  border: 1px solid #252540; background: transparent;
  color: #7A7A9A; font-size: 12px; font-weight: 500;
  font-family: inherit; cursor: pointer; transition: all .2s; text-align: center;
}
.mpill.active { background: #1C1A3A; border-color: #7C6FF7; color: #C4BFFF; }

/* ── LINE ITEMS ── */
.line-header { display: grid; grid-template-columns: 1fr 80px 90px 32px; gap: 8px; margin-bottom: 6px; }
.line-header span { font-size: 11px; color: #7A7A9A; }
.line-row { display: grid; grid-template-columns: 1fr 80px 90px 32px; gap: 8px; margin-bottom: 8px; align-items: center; }
.dbtn {
  width: 32px; height: 36px; border-radius: 8px;
  border: 1px solid #252540; background: transparent;
  color: #7A7A9A; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all .15s;
}
.dbtn:hover { border-color: #E05C5C; color: #E05C5C; }
.abtn {
  width: 100%; margin-top: 6px; padding: 9px;
  border-radius: 10px; border: 1px dashed #252540;
  background: transparent; color: #7A7A9A;
  font-size: 13px; font-family: inherit; cursor: pointer; transition: all .2s;
}
.abtn:hover { border-color: #7C6FF7; color: #C4BFFF; }

/* ── BUTTONS ── */
.next-btn {
  width: 100%; margin-top: 24px; padding: 14px;
  border-radius: 12px; border: none;
  background: linear-gradient(90deg, #7C6FF7, #5B9CF6);
  color: #fff; font-size: 15px; font-weight: 600;
  font-family: inherit; cursor: pointer;
  transition: opacity .2s; letter-spacing: .01em;
}
.next-btn:hover { opacity: .9; }
.next-btn:disabled { opacity: .35; cursor: not-allowed; }
.back-link {
  display: block; text-align: center; margin-top: 12px;
  font-size: 13px; color: #7A7A9A; cursor: pointer; transition: color .2s;
}
.back-link:hover { color: #C4BFFF; }
</style>
</head>
<body>

<!-- ══ RESULTS PAGE ══ -->
<div class="results-page" id="resultsPage">
  <div class="hero">
    <h1>Orgen ROI Calculator</h1>
    <p>Your estimated savings with Orgen</p>
  </div>
  <div style="text-align:center;margin-bottom:28px">
    <span class="company-badge" id="companyBadge"></span>
  </div>

  <div class="section-title">Company Summary</div>
  <div class="summary-grid" id="summaryGrid"></div>

  <div class="section-title">Monthly Results</div>
  <div class="results-grid">
    <div class="result-card">
      <div class="result-label">Current Monthly Cost</div>
      <div class="result-val" id="rBefore">&mdash;</div>
    </div>
    <div class="result-card highlight">
      <div class="result-label">Monthly Savings with Orgen</div>
      <div class="result-val green" id="rSavings">&mdash;</div>
      <div class="result-pct" id="rPct"></div>
    </div>
    <div class="result-card">
      <div class="result-label">Monthly Cost with Orgen</div>
      <div class="result-val" id="rAfter">&mdash;</div>
    </div>
  </div>

  <div class="section-title">Annual Projection</div>
  <div class="annual-box">
    <div class="annual-label">Estimated Annual Savings</div>
    <div class="annual-val" id="rAnnual">&mdash;</div>
  </div>

  <details>
    <summary>View full breakdown</summary>
    <div id="breakdownContent"></div>
  </details>

  <button class="restart-btn" onclick="restart()">&#8635; &nbsp; Recalculate</button>
</div>

<!-- ══ MODAL ══ -->
<div class="overlay" id="overlay">
  <div class="modal">

    <div class="progress-wrap">
      <div class="step-labels">
        <span class="step-label active" id="lbl1">Company</span>
        <span class="step-label" id="lbl2">Users</span>
        <span class="step-label" id="lbl3">Costs</span>
      </div>
      <div class="progress-steps">
        <div class="step-dot active" id="dot1">1</div>
        <div class="step-line" id="line1"></div>
        <div class="step-dot" id="dot2">2</div>
        <div class="step-line" id="line2"></div>
        <div class="step-dot" id="dot3">3</div>
      </div>
    </div>

    <!-- STEP 1 -->
    <div class="modal-body" id="step1">
      <div class="modal-title">Tell us about your company</div>
      <div class="modal-sub">We'll use this to personalize your ROI estimate</div>
      <div class="field">
        <label class="fl">Company name *</label>
        <input type="text" id="companyName" placeholder="Acme Corp" oninput="validateStep1()">
      </div>
      <div class="grid-2">
        <div class="field">
          <label class="fl">Industry</label>
          <select id="industry">
            <option>Technology</option>
            <option>Finance</option>
            <option>Healthcare</option>
            <option>Education</option>
            <option>Retail</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field">
          <label class="fl">Company size</label>
          <select id="companySize">
            <option>1–50</option>
            <option>51–200</option>
            <option>201–500</option>
            <option>501–1,000</option>
            <option>1,000+</option>
          </select>
        </div>
      </div>
      <button class="next-btn" id="nextBtn1" onclick="goTo(2)" disabled>
        Continue &rarr;
      </button>
    </div>

    <!-- STEP 2 -->
    <div class="modal-body" id="step2" style="display:none">
      <div class="modal-title">How many users?</div>
      <div class="modal-sub">Set the number of users per category</div>

      <div class="user-block">
        <div class="user-block-header">
          <span class="user-icon">&#128100;</span>
          <div>
            <div class="user-info-title">Regular Users</div>
            <div class="user-info-desc">Employees using AI tools for everyday tasks</div>
          </div>
        </div>
        <div class="counter-wrap">
          <button class="cbtn" onclick="chg('regular',-1)">&#8722;</button>
          <input class="cinput" type="number" id="regular" value="30" min="0" oninput="validateStep2()">
          <button class="cbtn" onclick="chg('regular',1)">+</button>
        </div>
      </div>

      <div class="user-block">
        <div class="user-block-header">
          <span class="user-icon">&#128187;</span>
          <div>
            <div class="user-info-title">Developers</div>
            <div class="user-info-desc">Engineers consuming AI via API</div>
          </div>
        </div>
        <div class="counter-wrap">
          <button class="cbtn" onclick="chg('devs',-1)">&#8722;</button>
          <input class="cinput" type="number" id="devs" value="10" min="0" oninput="validateStep2()">
          <button class="cbtn" onclick="chg('devs',1)">+</button>
        </div>
      </div>

      <button class="next-btn" id="nextBtn2" onclick="goTo(3)">
        Continue &rarr;
      </button>
      <span class="back-link" onclick="goTo(1)">&larr; Back</span>
    </div>

    <!-- STEP 3 -->
    <div class="modal-body" id="step3" style="display:none">
      <div class="modal-title">Current AI spending</div>
      <div class="modal-sub">Choose how to estimate your current costs</div>

      <div class="toggle-wrap">
        <button class="tbtn active" id="tbAuto" onclick="setMode('auto')">Auto-calculate</button>
        <button class="tbtn" id="tbManual" onclick="setMode('manual')">Enter manually</button>
      </div>

      <div id="autoSection">
        <label class="fl" style="margin-bottom:12px">Which AI model does your company primarily use today?</label>
        <div class="model-grid" id="modelGrid"></div>
      </div>

      <div id="manualSection" style="display:none">
        <div class="line-header">
          <span>Description</span>
          <span>Type</span>
          <span>Cost / mo ($)</span>
          <span></span>
        </div>
        <div id="lineItems"></div>
        <button class="abtn" onclick="addLine()">+ Add item</button>
      </div>

      <button class="next-btn" onclick="finish()">
        See My Savings &rarr;
      </button>
      <span class="back-link" onclick="goTo(2)">&larr; Back</span>
    </div>

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
  regular:[{model:"Gemini Flash",share:.50},{model:"Claude Haiku",share:.40},{model:"Claude Sonnet",share:.10}],
  dev:    [{model:"Claude Haiku",share:.60},{model:"Claude Sonnet",share:.30},{model:"Claude Opus",share:.10}],
};
const PLATFORM_FEE = 2000;

let currentModel = "Claude Sonnet";
let mode = "auto";
let lines = [{desc:"",type:"API",cost:0}];

function fmt(v) {
  if (v <= 0) return "$0";
  if (v >= 1e6) return "$"+(v/1e6).toFixed(1)+"M";
  if (v >= 1000) return "$"+Math.round(v).toLocaleString();
  return "$"+Math.round(v);
}

function goTo(step) {
  [1,2,3].forEach(i => {
    document.getElementById("step"+i).style.display = i===step ? "block" : "none";
    const dot = document.getElementById("dot"+i);
    dot.className = "step-dot"+(i<step?" done":i===step?" active":"");
    dot.textContent = i < step ? "\u2713" : i;
    document.getElementById("lbl"+i).className = "step-label"+(i===step?" active":"");
    if (i < 3) document.getElementById("line"+i).className = "step-line"+(i<step?" done":"");
  });
}

function validateStep1() {
  document.getElementById("nextBtn1").disabled =
    document.getElementById("companyName").value.trim().length === 0;
}

function validateStep2() {
  const r = parseInt(document.getElementById("regular").value)||0;
  const d = parseInt(document.getElementById("devs").value)||0;
  document.getElementById("nextBtn2").disabled = (r+d) === 0;
}

function chg(id, delta) {
  const el = document.getElementById(id);
  el.value = Math.max(0,(parseInt(el.value)||0)+delta);
  validateStep2();
}

function setMode(m) {
  mode = m;
  document.getElementById("autoSection").style.display   = m==="auto"   ? "block":"none";
  document.getElementById("manualSection").style.display = m==="manual" ? "block":"none";
  document.getElementById("tbAuto").classList.toggle("active",   m==="auto");
  document.getElementById("tbManual").classList.toggle("active", m==="manual");
}

function buildModels() {
  document.getElementById("modelGrid").innerHTML = Object.keys(MODEL_PRICES).map(n =>
    `<button class="mpill ${n===currentModel?"active":""}" onclick="selectModel('${n}')">${n}</button>`
  ).join("");
}
function selectModel(n) { currentModel=n; buildModels(); }

function renderLines() {
  document.getElementById("lineItems").innerHTML = lines.map((l,i) => `
    <div class="line-row">
      <input type="text" value="${l.desc}" placeholder="e.g. Claude API"
        oninput="lines[${i}].desc=this.value">
      <select onchange="lines[${i}].type=this.value">
        <option value="API"  ${l.type==="API" ?"selected":""}>API</option>
        <option value="sub"  ${l.type==="sub" ?"selected":""}>Subscription</option>
      </select>
      <input type="number" value="${l.cost||''}" min="0" step="100" placeholder="0"
        oninput="lines[${i}].cost=parseFloat(this.value)||0">
      <button class="dbtn" onclick="delLine(${i})">&#10005;</button>
    </div>
  `).join("");
}
function addLine()  { lines.push({desc:"",type:"API",cost:0}); renderLines(); }
function delLine(i) { lines.splice(i,1); if(!lines.length) lines=[{desc:"",type:"API",cost:0}]; renderLines(); }

function calcRouting(tokens, routing, ratio) {
  return routing.reduce((s,r) => {
    const p=MODEL_PRICES[r.model], t=tokens*r.share;
    return s+(t*ratio.input/1e6)*p.input+(t*ratio.output/1e6)*p.output;
  },0);
}

function finish() {
  const reg = Math.max(0,parseInt(document.getElementById("regular").value)||0);
  const dev = Math.max(0,parseInt(document.getElementById("devs").value)||0);
  const company  = document.getElementById("companyName").value.trim();
  const industry = document.getElementById("industry").value;
  const size     = document.getElementById("companySize").value;

  let before, after, savings, pct, breakdownHTML="";

  if (mode === "auto") {
    const p = MODEL_PRICES[currentModel];
    const tR=reg*18500*22, tD=dev*121000*22;
    const bR=reg>0?(tR*.40/1e6)*p.input+(tR*.60/1e6)*p.output:0;
    const bD=dev>0?(tD*.50/1e6)*p.input+(tD*.50/1e6)*p.output:0;
    const aR=reg>0?calcRouting(tR,ROUTING.regular,{input:.40,output:.60}):0;
    const aD=dev>0?calcRouting(tD,ROUTING.dev,    {input:.50,output:.50}):0;
    before=bR+bD; after=aR+aD+PLATFORM_FEE;
    savings=before-after; pct=before>0?savings/before:0;
    breakdownHTML = buildTable(
      ["Category","Before Orgen","After Orgen","Savings"],
      [
        ["Regular Users", fmt(bR), fmt(aR), fmt(bR-aR)],
        ["Developers",    fmt(bD), fmt(aD), fmt(bD-aD)],
        ["Platform Fee",  "&mdash;", fmt(PLATFORM_FEE), "&mdash;"],
        ["Total",         fmt(before), fmt(after), fmt(before-after)],
      ]
    );
  } else {
    const valid=lines.filter(l=>l.cost>0);
    let tot=0,sav=0;
    const bd=valid.map(l=>{
      const sp=l.type==="API"?.45:.20, sa=l.cost*sp;
      tot+=l.cost; sav+=sa;
      return {...l,sp,sa,costAfter:l.cost-sa};
    });
    before=tot; savings=sav; after=tot-sav;
    pct=tot>0?sav/tot:0;
    if (bd.length) {
      const rows=bd.map(i=>[i.desc||"Unnamed", i.type==="API"?"API":"Subscription",
        fmt(i.cost), Math.round(i.sp*100)+"%", fmt(i.costAfter)]);
      rows.push(["Total","",fmt(tot),"",fmt(after)]);
      breakdownHTML=buildTable(["Description","Type","Before","Savings","After"],rows);
    }
  }

  // Summary grid
  const summaryItems = [
    {key:"Company",   val: company},
    {key:"Industry",  val: industry},
    {key:"Size",      val: size},
    {key:"Regular Users", val: reg.toLocaleString()},
    {key:"Developers",    val: dev.toLocaleString()},
    {key:"Cost Method",   val: mode==="auto" ? currentModel : "Manual input"},
  ];
  document.getElementById("summaryGrid").innerHTML = summaryItems.map(i=>
    `<div class="summary-item"><div class="summary-key">${i.key}</div><div class="summary-val">${i.val}</div></div>`
  ).join("");

  document.getElementById("companyBadge").textContent = company;
  document.getElementById("rBefore").innerHTML  = fmt(before);
  document.getElementById("rAfter").innerHTML   = fmt(after);
  document.getElementById("rSavings").innerHTML = fmt(savings);
  document.getElementById("rPct").textContent   = Math.round(pct*100)+"% savings";
  document.getElementById("rAnnual").innerHTML  = fmt(savings*12);
  document.getElementById("breakdownContent").innerHTML = breakdownHTML;

  const overlay = document.getElementById("overlay");
  overlay.style.opacity = "0";
  setTimeout(() => {
    overlay.style.display = "none";
    document.getElementById("resultsPage").classList.add("visible");
  }, 400);
}

function buildTable(headers, rows) {
  let h="<table><thead><tr>"+headers.map(x=>`<th>${x}</th>`).join("")+"</tr></thead><tbody>";
  rows.forEach(r=>{ h+="<tr>"+r.map(c=>`<td>${c}</td>`).join("")+"</tr>"; });
  return h+"</tbody></table>";
}

function restart() {
  lines=[{desc:"",type:"API",cost:0}];
  currentModel="Claude Sonnet"; mode="auto";
  document.getElementById("companyName").value="";
  document.getElementById("regular").value=30;
  document.getElementById("devs").value=10;
  document.getElementById("resultsPage").classList.remove("visible");
  const overlay=document.getElementById("overlay");
  overlay.style.display="flex"; overlay.style.opacity="0";
  setTimeout(()=>{ overlay.style.opacity="1"; },10);
  goTo(1); validateStep1(); buildModels(); renderLines(); setMode("auto");
}

buildModels();
renderLines();
validateStep1();
</script>
</body>
</html>
""", height=1200, scrolling=True)
