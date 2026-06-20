"""
Google Form Auto-Submitter (Selenium Version)
Automated form submission using browser automation
For educational purposes only - use on forms you own
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from datetime import datetime
import json
import sys


class SeleniumFormSubmitter:
    """
    Automated Google Form submission using Selenium WebDriver
    Implements human-like behavior patterns and comprehensive error handling
    """
    
    def __init__(self, form_url, headless=False):
        """
        Initialize the form submitter
        
        Args:
            form_url: Full URL of the Google Form to submit
            headless: Run browser without GUI if True
        """
        self.form_url = form_url
        self.headless = headless
        self.driver = None
        
        # Statistics tracking
        self.submission_count = 0
        self.successful_submissions = 0
        self.failed_submissions = 0
        self.start_time = None
        
        # Configure your answer pools here
        self.setup_answer_pools()
    
    def setup_answer_pools(self):
        """
        Configure the answer pools for form questions
        Modify these lists to match your form's options
        """
        # Demographic options
        self.demographics = {
            "gender": ["Male", "Female", "Other", "Prefer not to say"],
            "age": ["18-25 years", "26-35 years", "36-45 years", "46-55 years", "56+"],
            "education": ["High School", "Bachelor's", "Master's", "PhD", "Other"],
            "industry": ["Technology", "Healthcare", "Education", "Finance", "Retail", "Other"],
            "experience": ["< 1 year", "1-3 years", "4-6 years", "7-10 years", "10+ years"]
        }
        
        # Likert scale responses
        self.likert_options = [
            "Strongly Disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree"
        ]
    
    def setup_driver(self):
        """Configure and initialize Chrome WebDriver"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        # Anti-detection measures
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Realistic user agent
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Hide automation flags
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
    
    def click_option(self, label_text):
        """
        Click a radio button or option by its label text
        
        Args:
            label_text: The text label of the option to click
        
        Returns:
            bool: True if successful, False otherwise
        """
        # Multiple strategies to find elements
        strategies = [
            f"//div[@role='radio' and @aria-label='{label_text}']",
            f"//div[@role='radio' and contains(@aria-label, '{label_text}')]",
            f"//span[text()='{label_text}']/ancestor::div[@role='radio']",
            f"//div[@role='radio' and contains(., '{label_text}')]",
            f"//label[contains(text(), '{label_text}')]",
        ]
        
        for xpath in strategies:
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(0.2)
                return True
            except:
                continue
        
        return False
    
    def fill_demographics(self):
        """
        Fill demographic questions with random answers
        Override this method to match your specific form structure
        """
        print("   📝 Filling demographic questions...")
        
        # Example: Fill 5 demographic questions
        # Modify these to match your actual form questions
        
        questions = [
            ("Q1 - Gender", random.choice(self.demographics["gender"])),
            ("Q2 - Age", random.choice(self.demographics["age"])),
            ("Q3 - Education", random.choice(self.demographics["education"])),
            ("Q4 - Industry", random.choice(self.demographics["industry"])),
            ("Q5 - Experience", random.choice(self.demographics["experience"])),
        ]
        
        for question, answer in questions:
            print(f"      {question}: {answer}")
            if not self.click_option(answer):
                print(f"      ⚠️ Failed to select: {answer}")
            time.sleep(random.uniform(0.3, 0.7))
    
    def fill_survey_questions(self, bias='neutral'):
        """
        Fill all remaining survey/Likert scale questions
        
        Args:
            bias: 'positive', 'negative', or 'neutral'
        """
        print("   📝 Filling survey questions...")
        
        # Scroll to load all elements
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)
        
        # Find all radio groups
        radio_groups = self.driver.find_elements(By.XPATH, "//div[@role='radiogroup']")
        print(f"   Found {len(radio_groups)} question groups")
        
        # Configure weights based on bias
        weights = self._get_bias_weights(bias)
        
        # Process each question group
        for i, group in enumerate(radio_groups):
            try:
                options = group.find_elements(By.XPATH, ".//div[@role='radio']")
                
                if not options:
                    continue
                
                # Skip if already answered
                if any(opt.get_attribute('aria-checked') == 'true' for opt in options):
                    continue
                
                # Select random option with bias
                if len(options) == len(weights):
                    choice = random.choices(options, weights=weights, k=1)[0]
                else:
                    choice = random.choice(options)
                
                choice_label = choice.get_attribute('aria-label') or f'Option {i+1}'
                self.driver.execute_script("arguments[0].click();", choice)
                print(f"      Q{i+1}: {choice_label}")
                
                time.sleep(random.uniform(0.1, 0.3))
                
            except StaleElementReferenceException:
                continue
            except Exception as e:
                print(f"      Q{i+1}: Error - {str(e)[:50]}")
                continue
    
    def _get_bias_weights(self, bias):
        """Get probability weights based on response bias"""
        if bias == 'positive':
            return [0.02, 0.08, 0.15, 0.35, 0.40]
        elif bias == 'negative':
            return [0.40, 0.35, 0.15, 0.08, 0.02]
        else:
            return [0.1, 0.2, 0.4, 0.2, 0.1]
    
    def submit_form(self):
        """Click submit and verify successful submission"""
        try:
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            # Find and click submit button
            submit_xpaths = [
                "//span[text()='Submit']",
                "//div[@role='button' and contains(., 'Submit')]",
                "//div[contains(@class, 'submit')]//span[contains(text(), 'Submit')]",
            ]
            
            submit_button = None
            for xpath in submit_xpaths:
                try:
                    submit_button = self.driver.find_element(By.XPATH, xpath)
                    if submit_button.is_displayed():
                        break
                except:
                    continue
            
            if not submit_button:
                print("   ⚠️ Submit button not found")
                return False
            
            self.driver.execute_script("arguments[0].click();", submit_button)
            time.sleep(3)
            
            # Check for success indicators
            success_phrases = [
                "thank you",
                "your response has been recorded",
                "response submitted"
            ]
            
            page_text = self.driver.page_source.lower()
            return any(phrase in page_text for phrase in success_phrases)
            
        except Exception as e:
            print(f"   ❌ Submit error: {str(e)[:100]}")
            return False
    
    def make_submission(self, bias='neutral'):
        """Execute a single complete form submission"""
        try:
            # Load form
            self.driver.get(self.form_url)
            time.sleep(random.uniform(3, 5))
            
            # Fill form sections
            self.fill_demographics()
            time.sleep(1)
            self.fill_survey_questions(bias)
            
            # Brief pause (simulating review)
            time.sleep(random.uniform(1, 3))
            
            # Submit
            return self.submit_form()
            
        except Exception as e:
            print(f"   ❌ Submission error: {str(e)[:200]}")
            self._save_error_screenshot()
            return False
    
    def _save_error_screenshot(self):
        """Save screenshot on error for debugging"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"error_screenshot_{timestamp}.png"
            self.driver.save_screenshot(filename)
            print(f"   📸 Screenshot saved: {filename}")
        except:
            pass
    
    def run(self, num_submissions=10, min_delay=5, max_delay=15, bias='neutral'):
        """
        Execute the full submission campaign
        
        Args:
            num_submissions: Total number of submissions to make
            min_delay: Minimum seconds between submissions
            max_delay: Maximum seconds between submissions
            bias: Response bias ('positive', 'negative', 'neutral')
        """
        self._print_header(num_submissions, min_delay, max_delay, bias)
        
        if not self._confirm_start():
            return
        
        self.setup_driver()
        self.start_time = time.time()
        
        try:
            for i in range(1, num_submissions + 1):
                self.submission_count = i
                
                print(f"\n{'='*60}")
                print(f"📤 Submission {i}/{num_submissions}")
                print(f"{'='*60}")
                
                success = self.make_submission(bias)
                
                if success:
                    self.successful_submissions += 1
                    print(f"\n✅ Submission {i}: SUCCESS")
                else:
                    self.failed_submissions += 1
                    print(f"\n❌ Submission {i}: FAILED")
                
                self._print_progress(i, num_submissions)
                
                # Delay before next submission
                if i < num_submissions:
                    delay = random.uniform(min_delay, max_delay)
                    print(f"⏳ Waiting {delay:.1f}s...")
                    time.sleep(delay)
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
        except Exception as e:
            print(f"\n\n❌ Fatal error: {e}")
        finally:
            self.cleanup()
            self._print_summary(num_submissions)
    
    def _print_header(self, num_submissions, min_delay, max_delay, bias):
        """Print campaign header"""
        print("=" * 60)
        print("🚀 GOOGLE FORM AUTO-SUBMITTER")
        print("=" * 60)
        print(f"📋 Form: {self.form_url}")
        print(f"🎯 Submissions: {num_submissions}")
        print(f"⏱️  Delay: {min_delay}-{max_delay}s")
        print(f"📊 Bias: {bias}")
        print(f"👁️  Headless: {self.headless}")
        print("=" * 60)
        print("\n⚠️  Only use on forms you own or have permission to test!\n")
    
    def _confirm_start(self):
        """Ask user confirmation before starting"""
        response = input("Start submissions? (yes/no): ").strip().lower()
        return response in ['yes', 'y']
    
    def _print_progress(self, current, total):
        """Print progress statistics"""
        progress = (current / total) * 100
        elapsed = time.time() - self.start_time
        
        if self.successful_submissions > 0:
            avg_time = elapsed / self.successful_submissions
            remaining = (total - current) * avg_time
            mins = int(remaining // 60)
            secs = int(remaining % 60)
            print(f"📊 {progress:.1f}% | ✅ {self.successful_submissions} | "
                  f"❌ {self.failed_submissions} | ⏳ ~{mins}m {secs}s left")
        else:
            print(f"📊 {progress:.1f}% | ✅ {self.successful_submissions} | "
                  f"❌ {self.failed_submissions}")
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            try:
                self.driver.quit()
                print("\n🔒 Browser closed")
            except:
                pass
    
    def _print_summary(self, total):
        """Print final campaign summary"""
        if not self.start_time:
            return
        
        elapsed = time.time() - self.start_time
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        print(f"\n{'='*60}")
        print("📊 CAMPAIGN COMPLETE")
        print(f"{'='*60}")
        print(f"🎯 Attempted:  {total}")
        print(f"✅ Successful: {self.successful_submissions}")
        print(f"❌ Failed:     {self.failed_submissions}")
        
        if total > 0:
            rate = (self.successful_submissions / total) * 100
            print(f"📈 Success rate: {rate:.1f}%")
        
        print(f"⏱️  Total time:  {hours}h {minutes}m {seconds}s")
        
        if self.successful_submissions > 0:
            avg = elapsed / self.successful_submissions
            print(f"⏱️  Avg/submission: {avg:.1f}s")
        
        print(f"{'='*60}")
        
        self._save_log(total, elapsed)
    
    def _save_log(self, total, elapsed):
        """Save submission log to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"submission_log_{timestamp}.json"
        
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "form_url": self.form_url,
            "total_attempted": total,
            "successful": self.successful_submissions,
            "failed": self.failed_submissions,
            "success_rate": f"{(self.successful_submissions/total)*100:.1f}%" if total > 0 else "0%",
            "elapsed_seconds": elapsed,
            "headless_mode": self.headless
        }
        
        with open(filename, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\n📝 Log saved: {filename}")


def main():
    """Entry point - configure your form here"""
    
    # ============================================================
    # CONFIGURATION - EDIT THESE VALUES
    # ============================================================
    
    # Your Google Form URL
    FORM_URL = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"
    
    # Submission settings
    NUM_SUBMISSIONS = 10  # Total submissions to make
    MIN_DELAY = 5         # Minimum seconds between submissions
    MAX_DELAY = 15        # Maximum seconds between submissions
    RESPONSE_BIAS = "neutral"  # 'positive', 'negative', or 'neutral'
    HEADLESS_MODE = False      # True = no browser window
    
    # ============================================================
    
    # Create and run the submitter
    submitter = SeleniumFormSubmitter(
        form_url=FORM_URL,
        headless=HEADLESS_MODE
    )
    
    submitter.run(
        num_submissions=NUM_SUBMISSIONS,
        min_delay=MIN_DELAY,
        max_delay=MAX_DELAY,
        bias=RESPONSE_BIAS
    )


if __name__ == "__main__":
    main()