"""
Sample configuration file
This shows how to configure the script for a typical survey form
"""

FORM_CONFIG = {
    "form_id": "1FAIpQLSdX4XBAg-uJOp6i-ZkL04L7EAas_VP1kJWBG3bTRYhw",
    
    "entry_ids": {
        "gender": "entry.2005620554",
        "age_group": "entry.1045781291",
        "education": "entry.1065046570",
        "industry": "entry.1166974658",
        "experience": "entry.839337160",
        "satisfaction_q1": "entry.544327140",
        "satisfaction_q2": "entry.130481341",
        "recommendation": "entry.501222558",
    },
    
    "demographics": {
        "genders": ["Male", "Female", "Non-binary"],
        "age_groups": ["18-25", "26-35", "36-45", "46-55", "56+"],
        "education_levels": [
            "High School",
            "Bachelor's",
            "Master's",
            "PhD",
            "Other"
        ]
    },
    
    "submission_settings": {
        "num_submissions": 50,
        "min_delay": 5,
        "max_delay": 10,
        "bias": "neutral",
        "headless": False
    }
}