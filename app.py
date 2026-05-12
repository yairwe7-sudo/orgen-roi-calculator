import streamlit as st
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="Orgen - AI Cost & ROI Calculator", page_icon="📈")

# עיצוב בסיסי
st.title("💰 Orgen ROI Calculator")
st.markdown("""
חשב כמה הארגון שלך יכול לחסוך באמצעות ניהול מרכזי, ניתוב חכם (Routing) ואופטימיזציה של משאבי AI.
""")

# סרגל צדדי להזנת נתונים
st.sidebar.header("נתוני הארגון")
num_users = st.sidebar.number_input("מספר משתמשי AI בארגון", min_value=1, value=100)
avg_queries_per_user = st.sidebar.slider("ממוצע שאילתות למשתמש ביום", 1, 100, 20)
monthly_api_spend = st.sidebar.number_input("הוצאה חודשית נוכחית על API ($)", min_value=0, value=5000)

st.sidebar.markdown("---")
st.sidebar.header("פרמטרים של Orgen")
routing_efficiency = st.sidebar.slider("אחוז שאילתות לניתוב למודל זול (%)", 0, 100, 60)
token_optimization = st.sidebar.slider("חיסכון בטוקנים בזכות RAG חכם (%)", 0, 100, 30)
license_cleanup = st.sidebar.slider("חיסכון בכפל מנויים (Shadow AI) (%)", 0, 50, 15)

# לוגיקה של חישובים
# חיסכון מניתוב: מודל יקר (0.01$ ל-1K טוקנים) לעומת זול (0.0005$ ל-1K טוקנים)
# נניח ש-60% מהתעבורה עוברת למודל זול פי 20
base_saving_factor = (routing_efficiency / 100) * 0.8 # הערכה שמרנית של 80% חיסכון על השאילתות המנותבות

savings_routing = monthly_api_spend * base_saving_factor
savings_tokens = (monthly_api_spend - savings_routing) * (token_optimization / 100)
savings_licenses = (monthly_api_spend * (license_cleanup / 100))

total_monthly_savings = savings_routing + savings_tokens + savings_licenses
total_annual_savings = total_monthly_savings * 12
new_monthly_cost = monthly_api_spend - total_monthly_savings

# תצוגת תוצאות
col1, col2, col3 = st.columns(3)
col1.metric("עלות חודשית חדשה", f"${int(new_monthly_cost):,}")
col2.metric("חיסכון חודשי", f"${int(total_monthly_savings):,}", f"{int((total_monthly_savings/monthly_api_spend)*100)}%")
col3.metric("חיסכון שנתי", f"${int(total_annual_savings):,}")

# תרשים השוואה
st.markdown("### השוואת עלויות שנתית ($)")
chart_data = pd.DataFrame({
 'סטטוס': ['ללא Orgen', 'עם Orgen'],
 'עלות שנתית ($)': [monthly_api_spend * 12, new_monthly_cost * 12]
})
st.bar_chart(data=chart_data, x='סטטוס', y='עלות שנתית ($)')

# פירוט החיסכון
with st.expander("ראה פירוט של מקורות החיסכון"):
 st.write(f"**1. ניתוב חכם (Smart Routing):** ${int(savings_routing):,} לחודש")
 st.write(f"**2. אופטימיזציה של Context:** ${int(savings_tokens):,} לחודש")
 st.write(f"**3. ביטול כפל מנויים ומשילה:** ${int(savings_licenses):,} לחודש")

st.info("💡 המחשבון מבוסס על היכולות הטכניות של Orgen API Hub כפי שמופיעות במסמך הארכיטקטורה.")

