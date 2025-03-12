import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


#Load variables
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")


# Define good speed thresholds
GOOD_DOWNLOAD_SPEED = 50
GOOD_UPLOAD_SPEED = 20

# Define possible responses for good internet
good_speeds_messages = [
    "🚀 Finally, my internet is moving like Lagos traffic at 2 AM! @MTNNG",
    "🔥 Streaming in 4K without buffering? Am I still in Nigeria?! @MTNNG",
    "📡 My ISP must have mistakenly upgraded my plan. I won’t ask questions! @MTNNG",
    "💨 This internet fast die! Even NEPA no fit cut am. @MTNNG",
    "🏆 Internet speed like Elon Musk's Starlink—make I no lie, I feel like a big boy! @MTNNG",
    "🤑 With this speed, I fit start my own WiFi hotspot and charge estate people. @MTNNG",
]

# Define possible responses for bad internet
bad_speed_messages = [
    "💀 @MTNNG, is my internet trekking from Lagos to Abuja before loading a page?",
    "🚶‍♂️ My WiFi moves like NEPA trying to restore light after rain. @MTNNG, wetin dey sup?",
    "📞 I called customer care, and even their response time is buffering. @MTNNG, abeg explain!",
    "🐌 My internet is so slow, even a Danfo conductor would shout ‘Oga, move na!’ @MTNNG, fix up!",
    "💨 @MTNNG, my 4G speed be like 2G wey dey struggle for village network. Who do us like this?",
    "⏳ My YouTube video is buffering like JAMB site during registration. @MTNNG, make una talk!",
    "📡 Is my internet waiting for Nigeria to qualify for the World Cup before loading? @MTNNG, abeg nau!",
    "🚀 I subscribed for 5G, but @MTNNG gave me 'G for God go help you' speed.",
    "🦥 This internet dey crawl pass Nigerian traffic on a rainy Monday. @MTNNG, how far?",
    "📲 @MTNNG, my data dey finish fast, but my internet slow pass old mama for market. E no balance!"
]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        self.internet_speed = {}

        self.get_internet_speed(SPEEDTEST_URL)
        #Checking if speeds are good
        is_good_download = float(self.internet_speed["Down"]) >= GOOD_DOWNLOAD_SPEED
        is_good_upload = float(self.internet_speed["Up"]) >= GOOD_UPLOAD_SPEED

        if is_good_upload and is_good_download:
            self.message = good_speeds_messages
        else:
            self.message = bad_speed_messages

        # Get current date and time
        now = datetime.now()
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M")

        self.tweet = f'Just tested my internet speed({formatted_date_time})... \n 🔽 Download: {self.internet_speed["Down"]} Mbps \n🔼 Upload: {self.internet_speed["Up"]} Mbps \n {random.choice(self.message)} \n #InternetStruggles #SpeedTest'
        self.tweet_at_provider()

    def get_internet_speed(self, url):
        self.driver.get(url)
        self.driver.set_page_load_timeout(180)
        self.driver.maximize_window()
        test_btn = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.CLASS_NAME, 'start-button')))
        test_btn.click()
        time.sleep(60)
        #save Up and Down speed
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.internet_speed = {"Up": up.text, "Down": down.text}
        print(self.internet_speed)


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        signin_bn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a'))) #'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a'
        signin_bn.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.NAME, "text")
        time.sleep(5)
        email_input.send_keys(TWITTER_EMAIL)
        next_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_btn.click()
        time.sleep(6)
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys("MtnUser_Bot")
        self.driver.find_element(By.XPATH,'//button[.//span[text()="Next"]]').click()
        time.sleep(5)
        pass_input = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        time.sleep(2)
        pass_input.send_keys(TWITTER_PASS)
        login_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_btn.click()
        time.sleep(10)
        
        # ------- Send Tweet ------- #
        tweet_entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        time.sleep(3)
        pyperclip.copy(self.tweet)
        tweet_entry.send_keys(Keys.CONTROL, "v")
        post_tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        self.driver.execute_script("arguments[0].click();", post_tweet)



app = InternetSpeedTwitterBot()



