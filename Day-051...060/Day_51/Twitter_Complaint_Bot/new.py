import os
import time
import random
import logging
from datetime import datetime
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")

GOOD_DOWNLOAD_SPEED = 50
GOOD_UPLOAD_SPEED = 20

good_speeds_messages = [
    "🚀 Finally, my internet is moving like Lagos traffic at 2 AM! @MTNNG",
    "🔥 Streaming in 4K without buffering? Am I still in Nigeria?! @MTNNG",
    "📡 My ISP must have mistakenly upgraded my plan. I won’t ask questions! @MTNNG",
    "💨 This internet fast die! Even NEPA no fit cut am. @MTNNG",
]

bad_speed_messages = [
    "💀 @MTNNG, is my internet trekking from Lagos to Abuja before loading a page?",
    "🚶‍♂️ My WiFi moves like NEPA trying to restore light after rain. @MTNNG, wetin dey sup?",
    "📞 I called customer care, and even their response time is buffering. @MTNNG, abeg explain!",
    "🐌 My internet is so slow, even a Danfo conductor would shout ‘Oga, move na!’ @MTNNG, fix up!",
]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = self.setup_driver()
        self.internet_speed = {}

    def setup_driver(self):
        #Initializes and returns the WebDriver.
        logging.info("Setting up WebDriver...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def get_internet_speed(self):
        #Runs a speed test and extracts download & upload speeds.
        logging.info("Opening Speedtest website...")
        try:
            self.driver.get(SPEEDTEST_URL)
            self.driver.set_page_load_timeout(180)

            # Handle cookie banner if present
            try:
                cookie_banner = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                )
                cookie_banner.click()
                logging.info("Accepted cookie policy.")
            except Exception:
                logging.info("No cookie banner found.")

            # Click start button
            test_btn = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.CLASS_NAME, 'start-button')))
            test_btn.click()
            logging.info("Speed test started. Waiting for results...")

            time.sleep(60)  # Allow test to complete

            # Extract speed values
            try:
                down_speed = self.driver.find_element(By.XPATH,
                                                '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
                up_speed = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

                self.internet_speed = {"Down": float(down_speed), "Up": float(up_speed)}
                logging.info(f"Speed Test Results: Download = {down_speed} Mbps, Upload = {up_speed} Mbps")
            except Exception:
                logging.error("Failed to retrieve speed test results.")
                self.internet_speed = {"Down": 0.0, "Up": 0.0}  # Default values

        except Exception as e:
            logging.error(f"Error in speed test: {e}")
            self.driver.quit()

    def generate_tweet(self):
        #Generates a tweet based on internet speed results.
        if not self.internet_speed or self.internet_speed["Down"] == 0.0 or self.internet_speed["Up"] == 0.0:
            logging.error("No valid internet speed data available. Skipping tweet generation.")
            return None  # Prevents tweet from being posted

        is_good_download = self.internet_speed["Down"] >= GOOD_DOWNLOAD_SPEED
        is_good_upload = self.internet_speed["Up"] >= GOOD_UPLOAD_SPEED
        messages = good_speeds_messages if is_good_download and is_good_upload else bad_speed_messages

        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        tweet = f'Just tested my internet speed ({formatted_time})... \n' \
                f'🔽 Download: {self.internet_speed["Down"]} Mbps \n' \
                f'🔼 Upload: {self.internet_speed["Up"]} Mbps \n' \
                f'{random.choice(messages)} \n #InternetStruggles #SpeedTest'

        logging.info(f"Generated Tweet: {tweet}")
        return tweet

    def tweet_at_provider(self, tweet):
        #Logs into Twitter and posts the tweet.
        if not tweet:
            logging.error("No tweet to post. Skipping Twitter step.")
            return

        logging.info("Opening Twitter login page...")
        try:
            self.driver.get(TWITTER_URL)
            signin_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "login")]'))
            )
            signin_btn.click()

            # Login process
            time.sleep(5)
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            email_input.send_keys(TWITTER_EMAIL)

            next_btn = self.driver.find_element(By.XPATH, '//button[.//span[text()="Next"]]')
            next_btn.click()

            # time.sleep(5)
            # username_input = self.driver.find_element(By.NAME, "text")
            # username_input.send_keys("MtnUser_Bot")  # Hardcoded as per request
            # next_btn = self.driver.find_element(By.XPATH, '//button[.//span[text()="Next"]]')
            # next_btn.click()

            time.sleep(5)
            pass_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
            pass_input.send_keys(TWITTER_PASS)
            login_btn = self.driver.find_element(By.XPATH, '//button[.//span[text()="Log in"]]')
            login_btn.click()

            logging.info("Successfully logged into Twitter.")
            time.sleep(5)

            # Posting tweet
            tweet_entry = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            time.sleep(3)
            pyperclip.copy(tweet)
            tweet_entry.send_keys(Keys.CONTROL, "v")
            post_tweet = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            self.driver.execute_script("arguments[0].click();", post_tweet)
            logging.info("Tweet successfully posted!")

        except Exception as e:
            logging.error(f"Error while tweeting: {e}")
        finally:
            time.sleep(5)
            self.driver.quit()

    def run(self):
        #Executes the full process.
        self.get_internet_speed()
        tweet = self.generate_tweet()

        if not tweet:
            logging.info("No tweet generated due to invalid internet speed data. Exiting process.")
            return  # Exit early if no valid data

        self.tweet_at_provider(tweet)


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.run()
