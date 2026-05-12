# config.py - כל המספרים במקום אחד

# צבעי המותג
COLORS = {
 "primary": "#6C5CE7", # סגול Orgen
 "secondary": "#00CEC9", # טורקיז
 "success": "#00B894", # ירוק לחיסכון
 "background": "#0F0F1A", # רקע כהה
 "card": "#1A1A2E", # רקע כרטיס
 "text": "#FFFFFF",
 "text_secondary": "#A0A0B0"
}

# מחירי מודלים ($ לכל מיליון טוקן)
MODEL_PRICES = {
 "Claude Opus": {"input": 15.00, "output": 75.00},
 "Claude Sonnet": {"input": 3.00, "output": 15.00},
 "Claude Haiku": {"input": 0.25, "output": 1.25},
 "GPT-4o": {"input": 2.50, "output": 10.00},
 "GPT-4o mini": {"input": 0.15, "output": 0.60},
 "Gemini Flash": {"input": 0.075, "output": 0.30},
}

# ניתוב Orgen
ORGEN_ROUTING = {
 "regular_users": [
 {"model": "Gemini Flash", "share": 0.50},
 {"model": "Claude Haiku", "share": 0.40},
 {"model": "Claude Sonnet", "share": 0.10},
 ],
 "developers": [
 {"model": "Claude Haiku", "share": 0.60},
 {"model": "Claude Sonnet", "share": 0.30},
 {"model": "Claude Opus", "share": 0.10},
 ]
}

# טוקנים ליום
TOKENS_PER_DAY = {
 "regular_user": 18_500,
 "developer": 121_000,
}

# ימי עבודה בחודש
WORKING_DAYS = 22

# יחס input/output
INPUT_OUTPUT_RATIO = {
 "regular_user": {"input": 0.40, "output": 0.60},
 "developer": {"input": 0.50, "output": 0.50},
}

# Platform fee
PLATFORM_FEE = 2_000

# אחוזי חיסכון להזנה ידנית
MANUAL_SAVINGS = {
 "API": 0.45, # 45%
 "מנוי": 0.20, # 20%
}
