\# Google Form Auto-Submitter



\[!\[Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

\[!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

\[!\[Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



A Python-based automation tool for Google Forms that demonstrates web automation, HTTP request handling, and browser automation techniques. This project serves as an educational resource for understanding web form mechanics and automation testing.



> \*\*⚠️ IMPORTANT DISCLAIMER\*\*: This tool is intended for \*\*EDUCATIONAL PURPOSES ONLY\*\*. Only use it on forms you own or have explicit permission to test. Unauthorized automated submissions to forms you don't own may violate Google's Terms of Service and applicable laws.



\## 🎯 Features



\- \*\*Two Implementation Methods\*\*:

&#x20; - `requests\_submitter.py` - Lightweight HTTP-based submission using direct POST requests

&#x20; - `selenium\_submitter.py` - Full browser automation with human-like behavior

&#x20; 

\- \*\*Intelligent Form Handling\*\*:

&#x20; - Automatic extraction of required hidden form fields

&#x20; - Dynamic session management with cookie persistence

&#x20; - Handles all form input types (radio buttons, text fields, etc.)

&#x20; 

\- \*\*Realistic Data Generation\*\*:

&#x20; - Configurable demographic data pools

&#x20; - Weighted random distributions for Likert scale responses

&#x20; - Support for positive, negative, and neutral response biases

&#x20; 

\- \*\*Production-Ready Features\*\*:

&#x20; - Comprehensive error handling and recovery

&#x20; - Configurable rate limiting with random delays

&#x20; - Detailed JSON logging of all submissions

&#x20; - Progress tracking with time estimates

&#x20; - Screenshot capture on errors (Selenium version)

&#x20; - Graceful keyboard interrupt handling



\## 📋 Prerequisites



\- Python 3.8 or higher

\- Chrome browser (for Selenium version)

\- Git (for cloning)



\## 🚀 Quick Start



\### 1. Clone the Repository



```bash

git clone https://github.com/chatgptiv4/Google-Form-Auto-Submitter.git

cd google-form-automator

```


\### 2. Install Dependencies


```bash

pip install -r requirements.txt

```

\### 3. Configure Your Form

```bash
Edit config.py with your form details:

python
# config.py
FORM_CONFIG = {
    "form_id": "YOUR_FORM_ID_HERE",  # From your form URL
    "form_url": "https://docs.google.com/forms/d/e/YOUR_FORM_ID_HERE/viewform",
    
    # Map your form fields
    "entry_ids": {
        "gender": "entry.XXXXXXXXXX",
        "age": "entry.YYYYYYYYYY",
        # ... add all your entry IDs
    },
    
    # Customize answer pools
    "demographics": {
        "genders": ["Male", "Female", "Other"],
        "ages": ["18-25", "26-35", "36-45", "46+"],
        # ... add your options
    }
}
```

\###  4. Run the Submitter
Selenium Version (Recommended for reliability):

```bash
python selenium_submitter.py
Requests Version (Faster, lighter):
```

```bash
python requests_submitter.py
📖 How to Get Your Form Entry IDs
Method 1: Browser Developer Tools (Recommended)
Open your Google Form in Chrome

Press F12 to open Developer Tools

Go to the Network tab

Check "Preserve log"

Fill and submit the form once manually

Find the formResponse request

Click on it and go to the Payload tab

Copy all entry.XXXXXXXXXX fields

Method 2: View Page Source
Open your form's live URL (not edit mode)

Right-click → View Page Source

Search for entry.

Note all entry IDs and their corresponding question
```

Method 3: JavaScript Console
Run this in your browser console on the form page:

javascript
Array.from(document.querySelectorAll('[name^="entry."]'))
    .map(el => el.name)
    .filter((v, i, a) => a.indexOf(v) === i)
    .forEach(entry => console.log(entry));

⚙️ Configuration Options
selenium_submitter.py
python
submitter = SeleniumFormSubmitter(
    form_url="YOUR_FORM_URL",
    headless=False,  # Set True for no browser window
)

submitter.run_campaign(
    num_submissions=100,  # Number of submissions
    min_delay=5,          # Min seconds between submissions
    max_delay=15,         # Max seconds between submissions
    bias='neutral'        # 'positive', 'negative', or 'neutral'
)
requests_submitter.py
python
submitter = RequestsFormSubmitter(
    form_id="YOUR_FORM_ID"
)

submitter.run_campaign(
    num_submissions=50,
    min_delay=3,
    max_delay=8
)
📁 Project Structure
text
google-form-automator/
│
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── config.py                    # User configuration
│
├── selenium_submitter.py        # Selenium-based implementation
├── requests_submitter.py        # Requests-based implementation
│
└── examples/
    ├── sample_config.py         # Example configuration
    └── sample_log.json          # Example log output
🔧 Technical Details
How It Works
HTTP Method (requests_submitter.py)
Fetches the form page to extract hidden fields (fbzx, fvv, etc.)

Maintains session cookies for CSRF protection

Constructs proper form data with all required fields

Sends POST requests with appropriate headers

Validates successful submission via response content

Browser Automation (selenium_submitter.py)
Launches a Chrome browser instance

Navigates to the form URL

Interacts with form elements like a real user

Uses JavaScript clicks for reliability

Implements random delays for human-like behavior

Captures screenshots on errors for debugging

Anti-Detection Measures
Realistic User-Agent strings

Random delays between actions (300ms - 15s)

Human-like scrolling and interaction patterns

JavaScript execution to bypass automation detection

Cookie and session management

Referer header spoofing

📊 Sample Output
text
============================================================
🚀 GOOGLE FORM AUTO-SUBMITTER
============================================================
📋 Form: https://docs.google.com/forms/...
🎯 Submissions: 100
⏱️  Delay: 5-15s
📊 Bias: neutral
============================================================

📤 Submission 1/100
============================================================
   📝 Filling demographics...
      Q1 - Gender: Female
      Q2 - Age: 26-35 years
      Q3 - Education: HND/B.Sc.
      Q4 - Industry: Technology/IT
      Q5 - Experience: 4-6 years
   📝 Filling survey questions...
      Found 30 radio groups
   🤔 Reviewing answers (1.5s)...
   📤 Submitting form...
✅ Submission 1: SUCCESS

📊 1.0% | ✅ 1 | ❌ 0 | ⏳ ~16m 30s remaining
⏳ Next submission in 8.3s...
⚠️ Rate Limiting & Best Practices
Start Small: Test with 5-10 submissions first

Use Conservative Delays: 8-15 seconds between submissions

Avoid Peak Hours: Run during off-peak times

Respect Limits: Google may temporarily block IPs after excessive submissions

Use VPNs Carefully: May trigger additional security checks

Monitor Responses: Check your form responses after initial submissions

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

⚖️ Legal & Ethical Guidelines
✅ DO use on forms you own

✅ DO use for testing and development

✅ DO obtain permission before testing on others' forms

❌ DON'T use for spam or unauthorized submissions

❌ DON'T use to manipulate survey results

❌ DON'T use to bypass form submission limits

🔗 Resources
Google Forms API Documentation

Selenium Documentation

Requests Library Documentation

📧 Contact
Your Name - @chatgptiv4 - chatgptiv4@example.com

Project Link:  https://github.com/chatgptiv4/Google-Form-Auto-Submitter.git



