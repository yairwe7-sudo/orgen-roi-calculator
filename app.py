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
 .stApp { background: #0B1020; }
 #MainMenu, footer, header { visibility: hidden; }
 .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root {
 --bg: #0B1020;
 --bg2: #111827;
 --bg-card: #0F1629;
 --cyan: #22D3EE;
 --blue: #3B82F6;
 --glow: #67E8F9;
 --txt: #FFFFFF;
 --txt2: #9CA3AF;
 --border: rgba(229,231,235,0.08);
 --border-a: rgba(34,211,238,0.25);
 --grad: linear-gradient(135deg, #22D3EE 0%, #3B82F6 100%);
 --r-lg: 20px; --r-md: 14px; --r-sm: 10px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);min-height:100vh;-webkit-font-smoothing:antialiased;}

@media print {
 .no-print{display:none!important;}
 .overlay{display:none!important;}
 body{background:#fff;color:#000;}
 .results-page{opacity:1!important;padding:20px;}
 .kpi-card,.annual-box,.summary-item{background:#f8fafc!important;border:1px solid #e2e8f0!important;}
 .kpi-val,.summary-val{color:#000!important;-webkit-text-fill-color:#000!important;}
 .kpi-val.cyan{color:#0891b2!important;-webkit-text-fill-color:#0891b2!important;}
 .annual-val{font-size:40px!important;background:none!important;color:#0891b2!important;-webkit-text-fill-color:#0891b2!important;}
 .section-title{color:#0891b2!important;}
 .ambient{display:none!important;}
}

/* ── AMBIENT ── */
.ambient{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}
.orb{position:absolute;border-radius:50%;filter:blur(130px);opacity:.10;animation:float 10s ease-in-out infinite;}
.orb.a{width:700px;height:700px;background:#22D3EE;top:-250px;right:-150px;animation-delay:0s;}
.orb.b{width:500px;height:500px;background:#3B82F6;bottom:-150px;left:-150px;animation-delay:4s;}
.orb.c{width:350px;height:350px;background:#22D3EE;top:45%;left:38%;animation-delay:7s;}
@keyframes float{0%,100%{transform:translateY(0)scale(1);}50%{transform:translateY(-28px)scale(1.04);}}

/* ═══ RESULTS PAGE ═══ */
.results-page{max-width:900px;margin:0 auto;padding:48px 28px 80px;opacity:0;transition:opacity .6s ease;position:relative;z-index:1;}
.results-page.visible{opacity:1;}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:translateY(0);}}

/* ── HERO ── */
.hero{text-align:center;margin-bottom:36px;animation:fadeUp .6s ease both;}
.logo-wrap{display:inline-flex;align-items:center;justify-content:center;margin-bottom:20px;}
.logo-wrap img{height:64px;width:auto;object-fit:contain;filter:brightness(1.1);}
.hero-tagline{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--cyan);margin-bottom:10px;opacity:.85;}
.hero-title{font-size:36px;font-weight:900;letter-spacing:-1.5px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:6px;}
.hero-sub{font-size:14px;color:var(--txt2);}
.company-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(34,211,238,.07);border:1px solid var(--border-a);border-radius:100px;padding:7px 20px;font-size:13px;font-weight:600;color:var(--cyan);margin-bottom:36px;box-shadow:0 0 20px rgba(34,211,238,.08);}
.company-badge::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--cyan);box-shadow:0 0 8px var(--cyan);}

/* ── SECTION TITLE ── */
.section-title{font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--cyan);margin-bottom:14px;display:flex;align-items:center;gap:10px;}
.section-title::after{content:'';flex:1;height:1px;background:var(--border);}

/* ── SUMMARY GRID ── */
.summary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:28px;}
.summary-item{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r-md);padding:14px 16px;transition:border-color .2s;}
.summary-item:hover{border-color:var(--border-a);}
.summary-key{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--txt2);margin-bottom:5px;}
.summary-val{font-size:14px;font-weight:600;color:var(--txt);}

/* ── KPI ROW ── */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px;}
.kpi-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px 16px;text-align:center;position:relative;overflow:hidden;transition:transform .2s,border-color .2s,box-shadow .2s;}
.kpi-card:hover{transform:translateY(-2px);border-color:var(--border-a);box-shadow:0 8px 32px rgba(34,211,238,.06);}
.kpi-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(34,211,238,.025),transparent);pointer-events:none;}
.kpi-card.highlight{border-color:rgba(34,211,238,.3);background:linear-gradient(145deg,rgba(34,211,238,.07),rgba(59,130,246,.04),var(--bg2));box-shadow:0 0 40px rgba(34,211,238,.08),inset 0 1px 0 rgba(34,211,238,.1);}
.kpi-card.highlight:hover{box-shadow:0 0 60px rgba(34,211,238,.15),inset 0 1px 0 rgba(34,211,238,.15);}
.kpi-label{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--txt2);margin-bottom:10px;}
.kpi-val{font-size:26px;font-weight:800;letter-spacing:-1px;color:var(--txt);}
.kpi-val.cyan{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.kpi-pct{font-size:12px;font-weight:600;color:var(--cyan);margin-top:5px;}

/* ── ANNUAL BOX ── */
.annual-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r-lg);padding:44px 28px;text-align:center;margin-bottom:24px;position:relative;overflow:hidden;transition:box-shadow .3s;}
.annual-box:hover{box-shadow:0 0 60px rgba(34,211,238,.07);}
.annual-box::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% -10%,rgba(34,211,238,.07) 0%,transparent 65%);pointer-events:none;}
.annual-label{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--txt2);margin-bottom:14px;}
.annual-val{font-size:72px;font-weight:900;letter-spacing:-4px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;}
.annual-sub{font-size:13px;color:var(--txt2);margin-top:10px;}

/* ── BREAKDOWN ── */
details{margin-top:6px;}
details summary{font-size:13px;font-weight:500;color:var(--txt2);cursor:pointer;list-style:none;display:flex;align-items:center;gap:8px;padding:12px 0;transition:color .2s;}
details summary:hover{color:var(--txt);}
details summary::before{content:"\25B8";font-size:10px;transition:transform .2s;color:var(--cyan);}
details[open] summary::before{transform:rotate(90deg);}
table{width:100%;border-collapse:collapse;margin-top:14px;font-size:13px;}
th{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--txt2);text-align:left;padding:8px 12px 12px;border-bottom:1px solid var(--border);}
td{padding:10px 12px;border-bottom:1px solid var(--border);color:#CBD5E1;}
tr:last-child td{border-bottom:none;font-weight:700;color:var(--txt);}
tr:hover td{background:rgba(255,255,255,.02);}
.details-box{background:rgba(17,24,39,.8);border:1px solid var(--border);border-radius:var(--r-md);padding:20px;margin-top:14px;backdrop-filter:blur(8px);}
.token-section{margin-bottom:20px;}
.token-section:last-child{margin-bottom:0;}
.token-section-title{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--cyan);margin-bottom:10px;display:flex;align-items:center;gap:8px;}
.token-section-title::after{content:'';flex:1;height:1px;background:var(--border);}
.token-row{display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.04);font-size:13px;}
.token-row:last-child{border-bottom:none;}
.token-key{color:var(--txt2);}
.token-val{color:var(--txt);font-weight:500;font-variant-numeric:tabular-nums;}

/* ── ACTIONS ── */
.action-row{display:flex;gap:12px;margin-top:24px;}
.btn-ghost,.btn-primary{flex:1;padding:14px;border-radius:var(--r-md);font-size:14px;font-weight:600;font-family:inherit;cursor:pointer;transition:all .2s;}
.btn-ghost{border:1px solid var(--border);background:transparent;color:var(--txt2);}
.btn-ghost:hover{border-color:var(--border-a);color:var(--txt);background:rgba(34,211,238,.04);}
.btn-primary{border:none;background:var(--grad);color:#fff;box-shadow:0 4px 24px rgba(34,211,238,.2);}
.btn-primary:hover{box-shadow:0 8px 36px rgba(34,211,238,.35);transform:translateY(-1px);}

/* ═══ MODAL ═══ */
.overlay{position:fixed;inset:0;background:rgba(7,10,22,.85);backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;z-index:100;transition:opacity .4s ease;}
.modal{background:var(--bg-card);border:1px solid var(--border);border-radius:24px;width:580px;max-width:calc(100vw - 32px);max-height:92vh;overflow-y:auto;box-shadow:0 32px 80px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.04);animation:modalIn .35s cubic-bezier(.16,1,.3,1) both;position:relative;}
.modal::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(34,211,238,.5),transparent);border-radius:24px 24px 0 0;}
@keyframes modalIn{from{opacity:0;transform:translateY(20px)scale(.98);}to{opacity:1;transform:translateY(0)scale(1);}}

/* ── MODAL LOGO ── */
.modal-logo{display:flex;justify-content:center;padding:28px 0 4px;}
.modal-logo img{height:42px;width:auto;object-fit:contain;filter:brightness(1.1);}

/* ── PROGRESS ── */
.progress-wrap{padding:22px 32px 0;}
.step-labels{display:flex;justify-content:space-between;margin-bottom:10px;}
.step-label{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--txt2);text-align:center;flex:1;transition:color .3s;}
.step-label.active{color:var(--cyan);}
.progress-steps{display:flex;align-items:center;margin-bottom:2px;}
.step-dot{width:30px;height:30px;border-radius:50%;border:1.5px solid rgba(255,255,255,.1);background:var(--bg2);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--txt2);flex-shrink:0;transition:all .3s;z-index:1;}
.step-dot.active{border-color:var(--cyan);background:rgba(34,211,238,.12);color:var(--cyan);box-shadow:0 0 14px rgba(34,211,238,.3);}
.step-dot.done{border-color:var(--cyan);background:var(--grad);color:#fff;box-shadow:0 0 12px rgba(34,211,238,.3);}
.step-line{flex:1;height:1px;background:rgba(255,255,255,.08);transition:background .4s;}
.step-line.done{background:var(--grad);}

/* ── MODAL BODY ── */
.modal-body{padding:24px 32px 32px;}
.modal-title{font-size:22px;font-weight:800;letter-spacing:-.5px;color:var(--txt);margin-bottom:6px;}
.modal-sub{font-size:13px;color:var(--txt2);margin-bottom:26px;line-height:1.5;}
.field{margin-bottom:18px;}
label.fl{display:block;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--txt2);margin-bottom:8px;}
input[type=text],input[type=number],select{width:100%;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:var(--r-sm);padding:12px 16px;color:var(--txt);font-size:14px;font-family:inherit;outline:none;transition:all .2s;appearance:none;-webkit-appearance:none;}
input:hover,select:hover{border-color:rgba(255,255,255,.15);}
input:focus,select:focus{border-color:var(--cyan);background:rgba(34,211,238,.04);box-shadow:0 0 0 3px rgba(34,211,238,.1);}
select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239CA3AF' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px;}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}

/* ── VENDOR CARDS (step 2) ── */
.vendor-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px;}
.vendor-pill{padding:14px 10px 12px;border-radius:var(--r-sm);border:1px solid var(--border);background:rgba(255,255,255,.02);color:var(--txt2);font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;transition:all .2s;text-align:center;position:relative;}
.vendor-pill:hover{border-color:rgba(34,211,238,.3);color:var(--txt);background:rgba(34,211,238,.04);}
.vendor-pill.active{border-color:var(--cyan);background:rgba(34,211,238,.08);color:var(--cyan);box-shadow:0 0 16px rgba(34,211,238,.1);}
.vendor-name{font-size:12px;font-weight:700;margin-bottom:6px;}
.vendor-check{position:absolute;top:5px;right:5px;width:14px;height:14px;border-radius:50%;background:var(--grad);color:#fff;font-size:7px;display:none;align-items:center;justify-content:center;font-weight:900;}
.vendor-pill.active .vendor-check{display:flex;}

/* ── COST TYPE TOGGLE ── */
.cost-type-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px;}
.cost-type-btn{padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:transparent;color:var(--txt2);font-size:11px;font-weight:600;font-family:inherit;cursor:pointer;transition:all .2s;text-align:center;}
.cost-type-btn.active{background:rgba(34,211,238,.08);border-color:var(--cyan);color:var(--cyan);}
.vendor-note{font-size:11px;color:rgba(156,163,175,.6);margin-bottom:18px;line-height:1.5;}

/* ── USER BLOCKS ── */
.user-block{background:rgba(255,255,255,.02);border:1px solid var(--border);border-radius:var(--r-md);padding:18px;margin-bottom:12px;transition:border-color .2s;}
.user-block:hover{border-color:rgba(255,255,255,.12);}
.user-block-header{display:flex;align-items:center;gap:12px;margin-bottom:14px;}
.user-icon-wrap{width:38px;height:38px;border-radius:10px;background:rgba(34,211,238,.1);border:1px solid rgba(34,211,238,.2);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;}
.user-info-title{font-size:14px;font-weight:700;color:var(--txt);}
.user-info-desc{font-size:12px;color:var(--txt2);margin-top:2px;}

/* ── NUMBER INPUT ── */
.num-input-wrap{display:flex;align-items:center;gap:12px;}
.cbtn{width:38px;height:38px;border-radius:10px;border:1px solid var(--border);background:rgba(255,255,255,.04);color:var(--cyan);font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;flex-shrink:0;}
.cbtn:hover{border-color:var(--cyan);background:rgba(34,211,238,.08);box-shadow:0 0 12px rgba(34,211,238,.15);}
.num-input{flex:1;text-align:center;font-size:28px;font-weight:900;letter-spacing:-1px;color:var(--txt);border:1px solid var(--border);border-radius:10px;padding:10px;background:rgba(255,255,255,.03);}
.num-input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(34,211,238,.1);}

/* ── TOGGLE ── */
.toggle-wrap{display:flex;gap:4px;margin-bottom:18px;background:rgba(255,255,255,.03);border:1px solid var(--border);border-radius:var(--r-sm);padding:4px;}
.tbtn{flex:1;padding:10px;border-radius:8px;border:none;background:transparent;color:var(--txt2);font-size:13px;font-weight:600;font-family:inherit;cursor:pointer;transition:all .2s;}
.tbtn.active{background:rgba(34,211,238,.12);color:var(--cyan);}

/* ── LINE ITEMS ── */
.line-header{display:grid;grid-template-columns:1fr 130px 110px 34px;gap:8px;margin-bottom:8px;}
.line-header span{font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--txt2);}
.line-row{display:grid;grid-template-columns:1fr 130px 110px 34px;gap:8px;margin-bottom:8px;align-items:center;}
.dbtn{width:34px;height:38px;border-radius:8px;border:1px solid var(--border);background:transparent;color:var(--txt2);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;}
.dbtn:hover{border-color:rgba(239,68,68,.4);color:#EF4444;background:rgba(239,68,68,.06);}
.abtn{width:100%;margin-top:8px;padding:10px;border-radius:var(--r-sm);border:1px dashed rgba(34,211,238,.2);background:transparent;color:rgba(34,211,238,.6);font-size:13px;font-weight:600;font-family:inherit;cursor:pointer;transition:all .2s;}
.abtn:hover{border-color:var(--cyan);color:var(--cyan);background:rgba(34,211,238,.04);}

/* ── BUTTONS ── */
.next-btn{width:100%;margin-top:26px;padding:15px;border-radius:var(--r-md);border:none;background:var(--grad);color:#fff;font-size:15px;font-weight:700;font-family:inherit;cursor:pointer;transition:all .2s;box-shadow:0 4px 24px rgba(34,211,238,.2);}
.next-btn:hover{box-shadow:0 8px 36px rgba(34,211,238,.35);transform:translateY(-1px);}
.next-btn:disabled{opacity:.3;cursor:not-allowed;transform:none;box-shadow:none;}
.back-link{display:block;text-align:center;margin-top:14px;font-size:13px;font-weight:500;color:var(--txt2);cursor:pointer;transition:color .2s;}
.back-link:hover{color:var(--txt);}

/* ── AUTO VENDOR CARDS (step 3) ── */
.auto-vendor-card{background:rgba(255,255,255,.02);border:1px solid var(--border);border-radius:var(--r-md);padding:14px 16px;transition:border-color .2s;margin-bottom:10px;}
.auto-vendor-card.avc-active{border-color:rgba(34,211,238,.3);background:rgba(34,211,238,.03);}
.avc-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;}
.avc-name{font-size:13px;font-weight:700;color:var(--txt);}
.avc-badge{font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--cyan);background:rgba(34,211,238,.1);border:1px solid rgba(34,211,238,.2);border-radius:100px;padding:2px 8px;}
.avc-tiers{display:flex;flex-wrap:wrap;gap:8px;}
.tier-pill{display:flex;align-items:center;gap:6px;padding:7px 12px;border-radius:8px;border:1px solid var(--border);background:transparent;color:var(--txt2);font-size:12px;font-family:inherit;cursor:pointer;transition:all .2s;}
.tier-pill:hover{border-color:rgba(34,211,238,.3);color:var(--txt);}
.tier-pill.active{border-color:var(--cyan);background:rgba(34,211,238,.08);color:var(--cyan);}
.tier-check{width:14px;font-size:10px;font-weight:900;color:var(--cyan);}
.tier-label{font-weight:600;}
.tier-price{font-size:11px;color:var(--txt2);font-weight:400;}
.tier-pill.active .tier-price{color:rgba(34,211,238,.7);}

::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-thumb{background:rgba(34,211,238,.2);border-radius:4px;}
</style>
</head>
<body>

<div class="ambient">
 <div class="orb a"></div>
 <div class="orb b"></div>
 <div class="orb c"></div>
</div>

<!-- ═══ RESULTS PAGE ═══ -->
<div class="results-page" id="resultsPage">
 <div class="hero">
 <div class="logo-wrap"><img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCACEAUADASIAAhEBAxEB/8QAHAABAAIDAQEBAAAAAAAAAAAAAAMFBAYHAggB/8QAOhAAAgIBAgQEAggEBQUAAAAAAAECAwQFEQYSITETQVFhInEHFDJCUoGRsWKhwdEVIzNy4RYkNEOC/8QAGgEBAAMBAQEAAAAAAAAAAAAAAAMEBQIBBv/EAC8RAAICAQMCBQIEBwAAAAAAAAABAgMRBBIhEzEFFCJBUWGhFTIzgXGRscHR4fD/2gAMAwEAAhEDEQA/APjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAttO0ad2PPLy7Pq+NCPM3tvJr2Xv2R1GLk8I4nOMFmTKkFvjYNGRb8FM1X5Jz3f5sz7eFrbqnPDn8flXN9/k/7lnyVzjlLJH
