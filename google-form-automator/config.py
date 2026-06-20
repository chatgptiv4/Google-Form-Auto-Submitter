"""
Configuration file for Google Form Auto-Submitter
Copy this file to config_local.py and add your form details
"""

# ============================================================
# FORM CONFIGURATION
# ============================================================

# Your Google Form ID (from the URL)
# Example: https://docs.google.com/forms/d/e/FORM_ID/viewform
FORM_ID = "YOUR_FORM_ID_HERE"

# Complete form URL
FORM_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/viewform"

# ============================================================
# ENTRY FIELD MAPPING
# ============================================================
# Map your form's entry IDs to descriptive names
# Find these by:
# 1. Opening form in browser
# 2. View Page Source (Ctrl+U)
# 3. Search for "entry."

ENTRY_IDS = {
    # Demographics
    "gender": "entry.XXXXXXXXXX",
    "age": "entry.YYYYYYYYYY",
    "education": "entry.ZZZZZZZZZZ",
    "industry": "entry.AAAAAAAAAA",
    "experience": "entry.BBBBBBBBBB",
    
    # Likert scale questions (add all your questions here)
    "q1": "entry.CCCCCCCCCC",
    "q2": "entry.DDDDDDDDDD",
    # ... add more as needed
}

# ============================================================
# ANSWER POOLS
# ============================================================
# Customize the answer options for each question

DEMOGRAPHICS = {
    "genders": [
        "Male",
        "Female",
        "Other",
        "Prefer not to say"
    ],
    
    "ages": [
        "18–25 years",
        "26–35 years",
        "36–45 years",
        "46–55 years",
        "56 years and above"
    ],
    
    "educations": [
        "High School",
        "Bachelor's Degree",
        "Master's Degree",
        "Doctorate",
        "Other"
    ],
    
    "industries": [
        "Technology",
        "Healthcare",
        "Education",
        "Finance",
        "Retail",
        "Manufacturing",
        "Other"
    ],
    
    "experiences": [
        "Less than 1 year",
        "1–3 years",
        "4–6 years",
        "7–10 years",
        "10+ years"
    ]
}

# Likert scale options
LIKERT_SCALE = [
    "Strongly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly agree"
]

# Alternative Likert scale (some forms use "Strongly Agree")
LIKERT_SCALE_ALT = [
    "Strongly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly Agree"
]

# ============================================================
# SUBMISSION SETTINGS
# ============================================================

# Number of submissions to make
NUM_SUBMISSIONS = 100

# Delay between submissions (seconds)
MIN_DELAY = 5
MAX_DELAY = 15

# Response bias: 'positive', 'negative', or 'neutral'
RESPONSE_BIAS = "neutral"

# Run browser in headless mode? (True = no browser window)
HEADLESS_MODE = False

# ============================================================
# ADVANCED SETTINGS
# ============================================================

# User-Agent string
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Maximum retries on failure
MAX_RETRIES = 3

# Save screenshots on errors?
SAVE_SCREENSHOTS = True

# Log level: 'DEBUG', 'INFO', 'WARNING', 'ERROR'
LOG_LEVEL = "INFO"