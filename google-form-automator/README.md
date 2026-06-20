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

git clone https://github.com/yourusername/google-form-automator.git

cd google-form-automator

