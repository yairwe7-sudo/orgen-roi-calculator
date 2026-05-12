# -*- coding: utf-8 -*-
# app.py

import streamlit as st
import pandas as pd
from config import MODEL_PRICES, COLORS
from calculations import (
    calc_cost_before_orgen,
    calc_cost_after_orgen,
    calc_manual_savings,
    format_currency,
)

# ─── הגדרות עמוד ───────────────────────────────────────────
st.set_page_config(
    page_title="Orgen ROI Calculator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CSS מותאם ─────────────────────────────────────────────
st.markdown("""
<style>
    .stApp {
        background-color: #0F0F1A;
        color: #FFFFFF;
    }
    .metric-card {
        background: #1A1A2E;
        border: 1px solid #2D2D4E;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    }
    .metric-card.savings {
        border-color: #00B894;
        background: linear-gradient(135deg, #1A1A2E, #0D2818);
    }
    .metric-label {
        color: #A0A0B0;
        font-size: 14px;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 700;
    }
    .metric-value.green {
        color: #00B894;
    }
    .step-header {
        background: linear-gradient(90deg, #6C5CE7, #00CEC9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 16px;
    }
    .divider {
        border: none;
        border-top: 1px solid #2D2D4E;
        margin: 32px 0;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─── HEADER ────────────────────────────────────────────────
st.markdown("""
<div style='text-align: center; padding: 40px 0 20px 0;'>
    <h1 style='font-size: 48px; font-weight: 800;'>
        <span style='background: linear-gradient(90deg, #6C5CE7, #00CEC9);
                     -webkit-background-clip: text;
                     -webkit-text-fill-color: transparent;'>
            Orgen ROI Calculator
        </span>
    </h1>
    <p style='color: #A0A0B0; font-size: 18px;'>
        גלה כמה תחסוך עם Orgen
    </p>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# שלב 1: פרטי חברה
# ════════════════════════════════════════════════════════════
st.markdown('<p class="step-header">שלב 1 — פרטי החברה</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    company_name = st.text_input("שם החברה", placeholder="Acme Corp")

with col2:
    industry = st.selectbox(
        "תעשייה",
        ["טכנולוגיה", "פיננסים", "בריאות", "חינוך", "קמעונאות", "אחר"]
    )

with col3:
    company_size = st.selectbox(
        "גודל חברה",
        ["1-50", "51-200", "201-500", "501-1000", "1000+"]
    )

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# שלב 2: מספר משתמשים
# ════════════════════════════════════════════════════════════
st.markdown('<p class="step-header">שלב 2 — משתמשים</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**👤 משתמשים רגילים**")
    st.caption("עובדים שמשתמשים בכלי AI ליומיום")
    regular_users = st.number_input(
        "מספר משתמשים רגילים",
        min_value=0, value=30, step=1,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("**👨‍💻 מפתחים**")
    st.caption("מפתחים שמשתמשים ב-API")
    developers = st.number_input(
        "מספר מפתחים",
        min_value=0, value=10, step=1,
        label_visibility="collapsed"
    )

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# שלב 3: הוצאות נוכחיות
# ════════════════════════════════════════════════════════════
st.markdown('<p class="step-header">שלב 3 — הוצאות נוכחיות</p>', unsafe_allow_html=True)

input_method = st.radio(
    "איך תרצה לחשב את ההוצאה הנוכחית?",
    ["חישוב אוטומטי", "הזנה ידנית"],
    horizontal=True,
)

# ── חישוב אוטומטי ──────────────────────────────────────────
if input_method == "חישוב אוטומטי":

    current_model = st.selectbox(
        "איזה מודל AI משתמשת החברה בעיקר היום?",
        list(MODEL_PRICES.keys()),
        index=1  # Claude Sonnet כברירת מחדל
    )

    before = calc_cost_before_orgen(regular_users, developers, current_model)
    after  = calc_cost_after_orgen(regular_users, developers)

    cost_before = before["total"]
    cost_after  = after["total"]
    savings     = cost_before - cost_after
    savings_pct = savings / cost_before if cost_before > 0 else 0

# ── הזנה ידנית ─────────────────────────────────────────────
else:
    st.markdown("**הוסף את ההוצאות שלך:**")

    # ניהול שורות בסשן
    if "line_items" not in st.session_state:
        st.session_state.line_items = [
            {"description": "", "type": "API", "cost": 0.0}
        ]

    # כותרות
    header_cols = st.columns([3, 1.5, 1.5, 0.5])
    header_cols[0].markdown("**תיאור**")
    header_cols[1].markdown("**סוג**")
    header_cols[2].markdown("**עלות חודשית ($)**")
    header_cols[3].markdown("")

    # שורות
    for i, item in enumerate(st.session_state.line_items):
        cols = st.columns([3, 1.5, 1.5, 0.5])

        st.session_state.line_items[i]["description"] = cols[0].text_input(
            f"desc_{i}", value=item["description"],
            placeholder="לדוגמה: Claude API",
            label_visibility="collapsed"
        )
        st.session_state.line_items[i]["type"] = cols[1].selectbox(
            f"type_{i}", ["API", "מנוי"],
            index=0 if item["type"] == "API" else 1,
            label_visibility="collapsed"
        )
        st.session_state.line_items[i]["cost"] = cols[2].number_input(
            f"cost_{i}", value=float(item["cost"]),
            min_value=0.0, step=100.0,
            label_visibility="collapsed"
        )
        if cols[3].button("🗑️", key=f"del_{i}"):
            st.session_state.line_items.pop(i)
            st.rerun()

    # כפתור הוספה
    if st.button("+ הוסף שורה"):
        st.session_state.line_items.append(
            {"description": "", "type": "API", "cost": 0.0}
        )
        st.rerun()

    # חישוב
    valid_items = [
        item for item in st.session_state.line_items
        if item["cost"] > 0
    ]
    manual_result = calc_manual_savings(valid_items)

    cost_before = manual_result["total_before"]
    cost_after  = manual_result["total_after"]
    savings     = manual_result["total_saving"]
    savings_pct = manual_result["saving_pct"]

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# תוצאות
# ════════════════════════════════════════════════════════════
st.markdown('<p class="step-header">התוצאות שלך</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">עלות חודשית נוכחית</div>
        <div class="metric-value">{format_currency(cost_before)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card savings">
        <div class="metric-label">חיסכון חודשי עם Orgen</div>
        <div class="metric-value green">{format_currency(savings)}</div>
        <div style="color: #00B894; font-size: 14px;">
            {savings_pct:.0%} חיסכון
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">עלות חודשית עם Orgen</div>
        <div class="metric-value">{format_currency(cost_after)}</div>
    </div>
    """, unsafe_allow_html=True)

# חיסכון שנתי
annual_savings = savings * 12
st.markdown(f"""
<div style='text-align: center; margin-top: 32px;'>
    <div style='color: #A0A0B0; font-size: 16px;'>חיסכון שנתי משוער</div>
    <div style='font-size: 56px; font-weight: 800;
                background: linear-gradient(90deg, #6C5CE7, #00CEC9);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;'>
        {format_currency(annual_savings)}
    </div>
</div>
""", unsafe_allow_html=True)


# ── פירוט (expandable) ─────────────────────────────────────
if input_method == "חישוב אוטומטי" and cost_before > 0:
    with st.expander("📊 ראה פירוט מלא"):
        detail_data = {
            "קטגוריה": ["משתמשים רגילים", "מפתחים", "Platform Fee", "סה\"כ"],
            "לפני Orgen": [
                format_currency(before.get("regular_user", 0)),
                format_currency(before.get("developer", 0)),
                "-",
                format_currency(cost_before),
            ],
            "אחרי Orgen": [
                format_currency(after.get("regular_user", 0)),
                format_currency(after.get("developer", 0)),
                format_currency(after.get("fee", 0)),
                format_currency(cost_after),
            ],
        }
        st.table(pd.DataFrame(detail_data))

elif input_method == "הזנה ידנית" and cost_before > 0:
    with st.expander("📊 ראה פירוט מלא"):
        if valid_items:
            detail_data = {
                "תיאור": [i["description"] or "ללא שם"
                           for i in manual_result["breakdown"]],
                "סוג":   [i["type"] for i in manual_result["breakdown"]],
                "לפני":  [format_currency(i["cost"])
                           for i in manual_result["breakdown"]],
                "חיסכון":[f'{i["saving_pct"]:.0%}'
                           for i in manual_result["breakdown"]],
                "אחרי":  [format_currency(i["cost_after"])
                           for i in manual_result["breakdown"]],
            }
            st.table(pd.DataFrame(detail_data))
