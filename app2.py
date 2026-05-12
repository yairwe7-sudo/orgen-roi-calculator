<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
 <meta charset="UTF-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
 <title>Orgen ROI Calculator</title>
 <style>
 * { margin: 0; padding: 0; box-sizing: border-box; }

 body {
 font-family: 'Segoe UI', system-ui, sans-serif;
 background: #0A0A0A;
 color: #FFFFFF;
 min-height: 100vh;
 display: flex;
 align-items: center;
 justify-content: center;
 }

 /* ─── Language Toggle ─── */
 .lang-toggle {
 position: fixed;
 top: 24px;
 left: 24px;
 display: flex;
 gap: 8px;
 z-index: 100;
 }
 .lang-btn {
 padding: 6px 16px;
 border-radius: 20px;
 border: 1px solid #2D2D3F;
 background: transparent;
 color: #A1A1AA;
 cursor: pointer;
 font-size: 13px;
 transition: all 0.2s;
 }
 .lang-btn.active {
 background: linear-gradient(135deg, #7C3AED, #3B82F6);
 border-color: transparent;
 color: #fff;
 }

 /* ─── Progress Bar ─── */
 .progress-wrap {
 position: fixed;
 top: 0; left: 0; right: 0;
 height: 3px;
 background: #1A1A2E;
 z-index: 99;
 }
 .progress-bar {
 height: 100%;
 background: linear-gradient(90deg, #7C3AED, #3B82F6);
 transition: width 0.5s ease;
 }

 /* ─── Logo ─── */
 .logo {
 position: fixed;
 top: 20px;
 right: 24px;
 font-size: 22px;
 font-weight: 700;
 background: linear-gradient(135deg, #7C3AED, #3B82F6);
 -webkit-background-clip: text;
 -webkit-text-fill-color: transparent;
 }

 /* ─── Card ─── */
 .card {
 background: #16213E;
 border: 1px solid #2D2D3F;
 border-radius: 24px;
 padding: 48px;
 width: 100%;
 max-width: 580px;
 margin: 80px 20px;
 position: relative;
 }

 .step-label {
 font-size: 12px;
 color: #7C3AED;
 text-transform: uppercase;
 letter-spacing: 2px;
 margin-bottom: 12px;
 }

 h2 {
 font-size: 28px;
 font-weight: 700;
 margin-bottom: 8px;
 line-height: 1.3;
 }

 .subtitle {
 color: #A1A1AA;
 font-size: 15px;
 margin-bottom: 36px;
 line-height: 1.6;
 }

 /* ─── Form Elements ─── */
 .field {
 margin-bottom: 20px;
 }

 label {
 display: block;
 font-size: 14px;
 color: #A1A1AA;
 margin-bottom: 8px;
 }

 input[type="text"],
 input[type="number"],
 input[type="email"],
 select {
 width: 100%;
 padding: 14px 18px;
 background: #0A0A0A;
 border: 1px solid #2D2D3F;
 border-radius: 12px;
 color: #fff;
 font-size: 15px;
 transition: border-color 0.2s;
 outline: none;
 }

 input:focus, select:focus {
 border-color: #7C3AED;
 }

 select option { background: #0A0A0A; }

 /* ─── Toggle Switch ─── */
 .toggle-row {
 display: flex;
 align-items: center;
 justify-content: space-between;
 padding: 14px 18px;
 background: #0A0A0A;
 border: 1px solid #2D2D3F;
 border-radius: 12px;
 margin-bottom: 12px;
 }

 .toggle-label { font-size: 15px; }

 .switch {
 position: relative;
 width: 44px;
 height: 24px;
 }
 .switch input { display: none; }
 .slider {
 position: absolute;
 inset: 0;
 background: #2D2D3F;
 border-radius: 24px;
 cursor: pointer;
 transition: 0.3s;
 }
 .slider:before {
 content: '';
 position: absolute;
 width: 18px; height: 18px;
 left: 3px; top: 3px;
 background: #fff;
 border-radius: 50%;
 transition: 0.3s;
 }
 .switch input:checked + .slider {
 background: linear-gradient(135deg, #7C3AED, #3B82F6);
 }
 .switch input:checked + .slider:before {
 transform: translateX(20px);
 }

 /* ─── Sub-panels (revealed by toggle) ─── */
 .sub-panel {
 background: #0D1117;
 border: 1px solid #2D2D3F;
 border-radius: 12px;
 padding: 20px;
 margin-bottom: 16px;
 display: none;
 }
 .sub-panel.open { display: block; }
 .sub-panel .field { margin-bottom: 14px; }
 .sub-panel label { font-size: 13px; }

 /* Checkbox group */
 .checkbox-group {
 display: grid;
 grid-template-columns: 1fr 1fr;
 gap: 8px;
 }
 .check-item {
 display: flex;
 align-items: center;
 gap: 8px;
 padding: 10px 12px;
 background: #16213E;
 border: 1px solid #2D2D3F;
 border-radius: 8px;
 cursor: pointer;
 font-size: 13px;
 transition: border-color 0.2s;
 }
 .check-item:has(input:checked) {
 border-color: #7C3AED;
 background: #1e1b4b;
 }
 .check-item input { accent-color: #7C3AED; }

 /* ─── Buttons ─── */
 .btn-primary {
 width: 100%;
 padding: 16px;
 background: linear-gradient(135deg, #7C3AED, #3B82F6);
 border: none;
 border-radius: 12px;
 color: #fff;
 font-size: 16px;
 font-weight: 600;
 cursor: pointer;
 margin-top: 12px;
 transition: opacity 0.2s, transform 0.1s;
 }
 .btn-primary:hover { opacity: 0.9; transform: translateY(-1px); }
 .btn-primary:active { transform: translateY(0); }

 .btn-back {
 background: transparent;
 border: 1px solid #2D2D3F;
 border-radius: 12px;
 color: #A1A1AA;
 font-size: 14px;
 padding: 10px 20px;
 cursor: pointer;
 margin-top: 12px;
 transition: border-color 0.2s;
 }
 .btn-back:hover { border-color: #7C3AED; color: #fff; }

 .btn-row {
 display: flex;
 gap: 12px;
 align-items: center;
 }
 .btn-row .btn-primary { flex: 1; margin-top: 0; }

 /* ─── Results ─── */
 .results-grid {
 display: grid;
 grid-template-columns: 1fr 1fr;
 gap: 16px;
 margin-bottom: 24px;
 }

 .result-card {
 background: #0A0A0A;
 border: 1px solid #2D2D3F;
 border-radius: 16px;
 padding: 20px;
 text-align: center;
 }
 .result-card.highlight {
 border-color: #7C3AED;
 background: #1e1b4b;
 }
 .result-card .amount {
 font-size: 32px;
 font-weight: 700;
 background: linear-gradient(135deg, #7C3AED, #3B82F6);
 -webkit-background-clip: text;
 -webkit-text-fill-color: transparent;
 }
 .result-card .amount.red { 
 background: none;
 -webkit-text-fill-color: #F87171;
 }
 .result-card .amount.green {
 background: none;
 -webkit-text-fill-color: #34D399;
 }
 .result-card .rlabel {
 font-size: 12px;
 color: #A1A1AA;
 margin-top: 4px;
 }

 /* ─── Chart ─── */
 .chart-wrap {
 background: #0A0A0A;
 border: 1px solid #2D2D3F;
 border-radius: 16px;
 padding: 24px;
 margin-bottom: 24px;
 }
 .chart-title {
 font-size: 14px;
 color: #A1A1AA;
 margin-bottom: 20px;
 }
 .bar-group {
 display: flex;
 align-items: flex-end;
 justify-content: center;
 gap: 32px;
 height: 160px;
 }
 .bar-col { display: flex; flex-direction: column; align-items: center; gap: 8px; }
 .bar {
 width: 80px;
 border-radius: 8px 8px 0 0;
 transition: height 1s ease;
 position: relative;
 }
 .bar.before { background: #374151; }
 .bar.after { background: linear-gradient(180deg, #7C3AED, #3B82F6); }
 .bar-val {
 font-size: 13px;
 font-weight: 600;
 color: #fff;
 }
 .bar-name { font-size: 12px; color: #A1A1AA; }

 /* Savings banner */
 .savings-banner {
 background: linear-gradient(135deg, #7C3AED22, #3B82F622);
 border: 1px solid #7C3AED66;
 border-radius: 16px;
 padding: 20px 24px;
 display: flex;
 justify-content: space-between;
 align-items: center;
 margin-bottom: 16px;
 }
 .savings-banner .s-label { font-size: 14px; color: #A1A1AA; }
 .savings-banner .s-value {
 font-size: 24px;
 font-weight: 700;
 color: #34D399;
 }

 /* Breakdown */
 .breakdown {
 background: #0A0A0A;
 border: 1px solid #2D2D3F;
 border-radius: 16px;
 padding: 20px;
 margin-bottom: 24px;
 }
 .breakdown-title {
 font-size: 13px;
 color: #A1A1AA;
 margin-bottom: 16px;
 text-transform: uppercase;
 letter-spacing: 1px;
 }
 .breakdown-row {
 display: flex;
 justify-content: space-between;
 align-items: center;
 padding: 10px 0;
 border-bottom: 1px solid #1A1A2E;
 font-size: 14px;
 }
 .breakdown-row:last-child { border-bottom: none; }
 .breakdown-row .model-name { color: #A1A1AA; }
 .breakdown-row .model-cost { font-weight: 600; }

 /* Hidden */
 .step { display: none; }
 .step.active { display: block; }
 </style>
</head>
<body>

<!-- Progress -->
<div class="progress-wrap">
 <div class="progress-bar" id="progressBar" style="width:33%"></div>
</div>

<!-- Logo -->
<div class="logo">Orgen</div>

<!-- Language -->
<div class="lang-toggle">
 <button class="lang-btn active" onclick="setLang('en')">EN</button>
 <button class="lang-btn" onclick="setLang('he')">עב</button>
</div>

<!-- ════════════════════════════════
 STEP 1 - Company Details
════════════════════════════════ -->
<div class="card step active" id="step1">
 <div class="step-label" data-en="Step 1 of 3" data-he="שלב 1 מתוך 3">Step 1 of 3</div>
 <h2 data-en="Tell us about your team" data-he="ספר לנו על הצוות שלך">Tell us about your team</h2>
 <p class="subtitle" data-en="We'll use this to calculate your current AI spend." data-he="נשתמש בזה כדי לחשב את ההוצאה הנוכחית שלך על AI.">We'll use this to calculate your current AI spend.</p>

 <div class="field">
 <label data-en="Company name" data-he="שם החברה">Company name</label>
 <input type="text" id="companyName" placeholder="Acme Inc." />
 </div>

 <div class="field">
 <label data-en="Regular users (non-developers)" data-he="משתמשים רגילים (לא מפתחים)">Regular users (non-developers)</label>
 <input type="number" id="regularUsers" min="0" value="0" />
 </div>

 <div class="field">
 <label data-en="Developers" data-he="מפתחים">Developers</label>
 <input type="number" id="devUsers" min="0" value="0" />
 </div>

 <button class="btn-primary" onclick="goStep2()" data-en="Next →" data-he="הבא ←">Next →</button>
</div>

<!-- ════════════════════════════════
 STEP 2 - Current Spend
════════════════════════════════ -->
<div class="card step" id="step2">
 <div class="step-label" data-en="Step 2 of 3" data-he="שלב 2 מתוך 3">Step 2 of 3</div>
 <h2 data-en="Your current AI setup" data-he="ה-AI setup הנוכחי שלך">Your current AI setup</h2>
 <p class="subtitle" data-en="Select everything that applies to your organization." data-he="סמן את כל מה שרלוונטי לארגון שלך.">Select everything that applies to your organization.</p>

 <!-- Subscription -->
 <div class="toggle-row">
 <span class="toggle-label" data-en="We use a subscription plan" data-he="אנחנו עובדים עם מנוי">We use a subscription plan</span>
 <label class="switch"><input type="checkbox" id="toggleSub" onchange="togglePanel('subPanel',this)"><span class="slider"></span></label>
 </div>
 <div class="sub-panel" id="subPanel">
 <div class="field">
 <label data-en="Plan type" data-he="סוג המנוי">Plan type</label>
 <select id="subType" onchange="updateSubCost()">
 <option value="chatgpt_business" data-en="ChatGPT Business (₪62/user)" data-he="ChatGPT Business (₪62/משתמש)">ChatGPT Business (₪62/user)</option>
 <option value="claude_standard" data-en="Claude Team Standard ($20/user/mo)" data-he="Claude Team Standard ($20/משתמש/חודש)">Claude Team Standard ($20/user/mo)</option>
 <option value="claude_premium" data-en="Claude Team Premium ($100/user/mo)" data-he="Claude Team Premium ($100/משתמש/חודש)">Claude Team Premium ($100/user/mo)</option>
 <option value="claude_enterprise" data-en="Claude Enterprise ($75/user/mo)" data-he="Claude Enterprise ($75/משתמש/חודש)">Claude Enterprise ($75/user/mo)</option>
 <option value="chatgpt_enterprise" data-en="ChatGPT Enterprise (custom)" data-he="ChatGPT Enterprise (custom)">ChatGPT Enterprise (custom)</option>
 <option value="other" data-en="Other (enter manually)" data-he="אחר (הזנה ידנית)">Other (enter manually)</option>
 </select>
 </div>
 <div class="field" id="subUsersField">
 <label data-en="Number of seats" data-he="מספר מושבים">Number of seats</label>
 <input type="number" id="subUsers" min="0" value="0" />
 </div>
 <div class="field" id="subCustomField" style="display:none">
 <label data-en="Monthly cost ($)" data-he="עלות חודשית ($)">Monthly cost ($)</label>
 <input type="number" id="subCustomCost" min="0" value="0" />
 </div>
 </div>

 <!-- API -->
 <div class="toggle-row">
 <span class="toggle-label" data-en="We use AI via API" data-he="אנחנו עובדים עם API">We use AI via API</span>
 <label class="switch"><input type="checkbox" id="toggleApi" onchange="togglePanel('apiPanel',this)"><span class="slider"></span></label>
 </div>
 <div class="sub-panel" id="apiPanel">
 <div class="field">
 <label data-en="Models in use" data-he="מודלים בשימוש">Models in use</label>
 <div class="checkbox-group">
 <label class="check-item"><input type="checkbox" value="claude_opus"> Claude Opus</label>
 <label class="check-item"><input type="checkbox" value="claude_sonnet"> Claude Sonnet</label>
 <label class="check-item"><input type="checkbox" value="claude_haiku"> Claude Haiku</label>
 <label class="check-item"><input type="checkbox" value="gpt4o"> GPT-4o</label>
 <label class="check-item"><input type="checkbox" value="gpt4o_mini"> GPT-4o-mini</label>
 <label class="check-item"><input type="checkbox" value="gemini_flash"> Gemini Flash</label>
 </div>
 </div>
 <div class="field">
 <label data-en="Monthly API spend ($)" data-he="הוצאה חודשית על API ($)">Monthly API spend ($)</label>
 <input type="number" id="apiSpend" min="0" value="0" />
 </div>
 </div>

 <!-- Cloud Platform -->
 <div class="toggle-row">
 <span class="toggle-label" data-en="We use a Cloud AI Platform" data-he="אנחנו עובדים דרך Cloud Platform">We use a Cloud AI Platform</span>
 <label class="switch"><input type="checkbox" id="toggleCloud" onchange="togglePanel('cloudPanel',this)"><span class="slider"></span></label>
 </div>
 <div class="sub-panel" id="cloudPanel">
 <div class="field">
 <label data-en="Platform" data-he="פלטפורמה">Platform</label>
 <select id="cloudType">
 <option value="bedrock" data-en="AWS Bedrock" data-he="AWS Bedrock">AWS Bedrock</option>
 <option value="azure" data-en="Microsoft Azure AI Foundry" data-he="Microsoft Azure AI Foundry">Microsoft Azure AI Foundry</option>
 <option value="both" data-en="Both" data-he="שניהם">Both</option>
 </select>
 </div>
 <div class="field">
 <label data-en="Monthly cloud AI spend ($)" data-he="הוצאה חודשית על Cloud AI ($)">Monthly cloud AI spend ($)</label>
 <input type="number" id="cloudSpend" min="0" value="0" />
 </div>
 </div>

 <div style="margin-top:24px" class="btn-row">
 <button class="btn-back" onclick="goStep1()" data-en="← Back" data-he="→ חזור">← Back</button>
 <button class="btn-primary" onclick="goStep3()" data-en="Calculate →" data-he="חשב ←">Calculate →</button>
 </div>
</div>

<!-- ════════════════════════════════
 STEP 3 - Results
════════════════════════════════ -->
<div class="card step" id="step3" style="max-width:680px">
 <div class="step-label" data-en="Step 3 of 3" data-he="שלב 3 מתוך 3">Step 3 of 3</div>
 <h2 id="resultsTitle">Acme Inc. — AI Cost Analysis</h2>
 <p class="subtitle" data-en="Here's what you spend today vs. with Orgen's intelligent routing." data-he="הנה ההוצאה שלך היום לעומת ניתוב חכם עם Orgen.">Here's what you spend today vs. with Orgen's intelligent routing.</p>

 <!-- Top 4 KPIs -->
 <div class="results-grid">
 <div class="result-card">
 <div class="amount red" id="kpiCurrentMonthly">$0</div>
 <div class="rlabel" data-en="Current monthly spend" data-he="הוצאה חודשית נוכחית">Current monthly spend</div>
 </div>
 <div class="result-card highlight">
 <div class="amount" id="kpiOrgenMonthly">$0</div>
 <div class="rlabel" data-en="With Orgen (monthly)" data-he="עם Orgen (חודשי)">With Orgen (monthly)</div>
 </div>
 <div class="result-card">
 <div class="amount green" id="kpiSavingsMonthly">$0</div>
 <div class="rlabel" data-en="Monthly savings" data-he="חיסכון חודשי">Monthly savings</div>
 </div>
 <div class="result-card">
 <div class="amount green" id="kpiSavingsAnnual">$0</div>
 <div class="rlabel" data-en="Annual savings" data-he="חיסכון שנתי">Annual savings</div>
 </div>
 </div>

 <!-- Savings banner -->
 <div class="savings-banner">
 <div>
 <div class="s-label" data-en="Total savings with Orgen" data-he="סה״כ חיסכון עם Orgen">Total savings with Orgen</div>
 <div style="font-size:12px;color:#A1A1AA;margin-top:4px" id="savingsPct"></div>
 </div>
 <div class="s-value" id="bannerSavings">$0</div>
 </div>

 <!-- Bar Chart -->
 <div class="chart-wrap">
 <div class="chart-title" data-en="Monthly cost comparison" data-he="השוואת עלות חודשית">Monthly cost comparison</div>
 <div class="bar-group">
 <div class="bar-col">
 <div class="bar-val" id="chartBeforeVal">$0</div>
 <div class="bar before" id="barBefore" style="height:0px"></div>
 <div class="bar-name" data-en="Without Orgen" data-he="ללא Orgen">Without Orgen</div>
 </div>
 <div class="bar-col">
 <div class="bar-val" id="chartAfterVal">$0</div>
 <div class="bar after" id="barAfter" style="height:0px"></div>
 <div class="bar-name" data-en="With Orgen" data-he="עם Orgen">With Orgen</div>
 </div>
 </div>
 </div>

 <!-- Breakdown -->
 <div class="breakdown">
 <div class="breakdown-title" data-en="Cost breakdown with Orgen" data-he="פירוט עלויות עם Orgen">Cost breakdown with Orgen</div>
 <div class="breakdown-row">
 <span class="model-name" data-en="Regular users → Gemini Flash + Haiku" data-he="משתמשים רגילים → Gemini Flash + Haiku">Regular users → Gemini Flash + Haiku</span>
 <span class="model-cost" id="bdRegular">$0</span>
 </div>
 <div class="breakdown-row">
 <span class="model-name" data-en="Developers → Sonnet + Opus (15%)" data-he="מפתחים → Sonnet + Opus (15%)">Developers → Sonnet + Opus (15%)</span>
 <span class="model-cost" id="bdDev">$0</span>
 </div>
 <div class="breakdown-row">
 <span class="model-name" data-en="Orgen platform fee" data-he="דמי שימוש Orgen">Orgen platform fee</span>
 <span class="model-cost">$2,000</span>
 </div>
 <div class="breakdown-row" style="border-top:1px solid #2D2D3F;margin-top:4px;padding-top:14px">
 <span style="font-weight:600" data-en="Total with Orgen" data-he="סה״כ עם Orgen">Total with Orgen</span>
 <span class="model-cost" id="bdTotal">$0</span>
 </div>
 </div>

 <button class="btn-back" onclick="goStep2()" data-en="← Recalculate" data-he="→ חשב מחדש">← Recalculate</button>
</div>

<script>
// ══════════════════════════════════════
// CONSTANTS
// ══════════════════════════════════════
const ILS_TO_USD = 0.27;

const SUBSCRIPTION_PRICES = {
 chatgpt_business: 62 * ILS_TO_USD, // ~$16.74
 claude_standard: 20,
 claude_premium: 100,
 claude_enterprise: 75,
 chatgpt_enterprise: 65,
 other: 0
};

// Claude API prices (per MTok)
const API_PRICES = {
 claude_opus: { input: 5, output: 25 },
 claude_sonnet: { input: 3, output: 15 },
 claude_haiku: { input: 1, output: 5 },
 gpt4o: { input: 2.50, output: 10 },
 gpt4o_mini: { input: 0.15, output: 0.60 },
 gemini_flash: { input: 0.075,output: 0.30 }
};

// Daily tokens per user type
const TOKENS_PER_DAY = {
 regular: 18500,
 developer: 121000
};

const WORK_DAYS = 22;
const ORGEN_FEE = 2000;

// Orgen routing (fraction of traffic × model)
// Regular: 50% Flash, 40% Haiku, 10% Sonnet
// Developer: 35%+30%+20% Sonnet, 15% Opus
const ORGEN_ROUTING = {
 regular: [
 { model: 'gemini_flash', share: 0.50, inputRatio: 0.40 },
 { model: 'claude_haiku', share: 0.40, inputRatio: 0.40 },
 { model: 'claude_sonnet', share: 0.10, inputRatio: 0.40 }
 ],
 developer: [
 { model: 'claude_sonnet', share: 0.85, inputRatio: 0.50 },
 { model: 'claude_opus', share: 0.15, inputRatio: 0.50 }
 ]
};

// ══════════════════════════════════════
// STATE
// ══════════════════════════════════════
let lang = 'en';
let currentStep = 1;

// ══════════════════════════════════════
// LANGUAGE
// ══════════════════════════════════════
function setLang(l) {
 lang = l;
 document.documentElement.lang = l === 'he' ? 'he' : 'en';
 document.documentElement.dir = l === 'he' ? 'rtl' : 'ltr';

 document.querySelectorAll('[data-en]').forEach(el => {
 el.textContent = el.getAttribute('data-' + l) || el.getAttribute('data-en');
 });

 // Update select options
 document.querySelectorAll('select option[data-en]').forEach(opt => {
 opt.textContent = opt.getAttribute('data-' + l) || opt.getAttribute('data-en');
 });

 document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
 document.querySelector(`.lang-btn[onclick="setLang('${l}')"]`).classList.add('active');

 // Re-render results if on step 3
 if (currentStep === 3) renderResults();
}

// ══════════════════════════════════════
// NAVIGATION
// ══════════════════════════════════════
function showStep(n) {
 currentStep = n;
 document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
 document.getElementById('step' + n).classList.add('active');
 document.getElementById('progressBar').style.width = (n * 33.33) + '%';
 window.scrollTo({ top: 0, behavior: 'smooth' });
}

function goStep1() { showStep(1); }

function goStep2() {
 const reg = parseInt(document.getElementById('regularUsers').value) || 0;
 const dev = parseInt(document.getElementById('devUsers').value) || 0;
 if (reg + dev === 0) {
 alert(lang === 'he' ? 'נא להזין לפחות משתמש אחד' : 'Please enter at least one user.');
 return;
 }
 showStep(2);
}

function goStep3() {
 renderResults();
 showStep(3);
}

// ══════════════════════════════════════
// TOGGLE PANELS
// ══════════════════════════════════════
function togglePanel(panelId, checkbox) {
 const panel = document.getElementById(panelId);
 if (checkbox.checked) panel.classList.add('open');
 else panel.classList.remove('open');
}

document.getElementById('subType').addEventListener('change', function() {
 const isOther = this.value === 'other' || this.value === 'chatgpt_enterprise';
 document.getElementById('subCustomField').style.display = isOther ? 'block' : 'none';
 document.getElementById('subUsersField').style.display = isOther ? 'none' : 'block';
});

// ══════════════════════════════════════
// CALCULATIONS
// ══════════════════════════════════════
function calcCurrentSpend() {
 let total = 0;

 // Subscription
 if (document.getElementById('toggleSub').checked) {
 const type = document.getElementById('subType').value;
 if (type === 'other' || type === 'chatgpt_enterprise') {
 total += parseFloat(document.getElementById('subCustomCost').value) || 0;
 } else {
 const seats = parseInt(document.getElementById('subUsers').value) || 0;
 total += seats * SUBSCRIPTION_PRICES[type];
 }
 }

 // API
 if (document.getElementById('toggleApi').checked) {
 total += parseFloat(document.getElementById('apiSpend').value) || 0;
 }

 // Cloud
 if (document.getElementById('toggleCloud').checked) {
 total += parseFloat(document.getElementById('cloudSpend').value) || 0;
 }

 return total;
}

function calcOrgenSpend(regularUsers, devUsers) {
 // Monthly tokens per group
 const regularTok = regularUsers * TOKENS_PER_DAY.regular * WORK_DAYS; // total tokens
 const devTok = devUsers * TOKENS_PER_DAY.developer * WORK_DAYS;

 let regularCost = 0;
 let devCost = 0;

 ORGEN_ROUTING.regular.forEach(route => {
 const tok = regularTok * route.share;
 const input = tok * route.inputRatio;
 const output= tok * (1 - route.inputRatio);
 const p = API_PRICES[route.model];
 regularCost += (input * p.input + output * p.output) / 1_000_000;
 });

 ORGEN_ROUTING.developer.forEach(route => {
 const tok = devTok * route.share;
 const input = tok * route.inputRatio;
 const output= tok * (1 - route.inputRatio);
 const p = API_PRICES[route.model];
 devCost += (input * p.input + output * p.output) / 1_000_000;
 });

 return { regularCost, devCost, total: regularCost + devCost + ORGEN_FEE };
}

// ══════════════════════════════════════
// RENDER RESULTS
// ══════════════════════════════════════
function fmt(n) {
 return '$' + Math.round(n).toLocaleString('en-US');
}

function renderResults() {
 const company = document.getElementById('companyName').value || 'Your Company';
 const regularUsers = parseInt(document.getElementById('regularUsers').value) || 0;
 const devUsers = parseInt(document.getElementById('devUsers').value) || 0;

 const currentMonthly = calcCurrentSpend();
 const orgen = calcOrgenSpend(regularUsers, devUsers);
 const orgenMonthly = orgen.total;

 const savingsMonthly = Math.max(0, currentMonthly - orgenMonthly);
 const savingsAnnual = savingsMonthly * 12;
 const savingsPct = currentMonthly > 0
 ? Math.round((savingsMonthly / currentMonthly) * 100)
 : 0;

 // Title
 document.getElementById('resultsTitle').textContent =
 company + (lang === 'he' ? ' — ניתוח עלויות AI' : ' — AI Cost Analysis');

 // KPIs
 document.getElementById('kpiCurrentMonthly').textContent = fmt(currentMonthly);
 document.getElementById('kpiOrgenMonthly').textContent = fmt(orgenMonthly);
 document.getElementById('kpiSavingsMonthly').textContent = fmt(savingsMonthly);
 document.getElementById('kpiSavingsAnnual').textContent = fmt(savingsAnnual);

 // Banner
 document.getElementById('bannerSavings').textContent = fmt(savingsAnnual);
 document.getElementById('savingsPct').textContent =
 lang === 'he'
 ? `חיסכון של ${savingsPct}% בהוצאות ה-AI שלך`
 : `${savingsPct}% reduction in your AI spend`;

 // Breakdown
 document.getElementById('bdRegular').textContent = fmt(orgen.regularCost);
 document.getElementById('bdDev').textContent = fmt(orgen.devCost);
 document.getElementById('bdTotal').textContent = fmt(orgenMonthly);

 // Chart
 document.getElementById('chartBeforeVal').textContent = fmt(currentMonthly);
 document.getElementById('chartAfterVal').textContent = fmt(orgenMonthly);

 const maxVal = Math.max(currentMonthly, orgenMonthly, 1);
 const maxHeight = 130;
 setTimeout(() => {
 document.getElementById('barBefore').style.height =
 Math.max(8, (currentMonthly / maxVal) * maxHeight) + 'px';
 document.getElementById('barAfter').style.height =
 Math.max(8, (orgenMonthly / maxVal) * maxHeight) + 'px';
 }, 100);
}

// Init lang
setLang('en');
</script>
</body>
</html>

