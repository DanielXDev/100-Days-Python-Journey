import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSe4MR4bfmnUyQbr1S0HQMxX2s-6s_aqlMoeOm2hXQNed38VOw/viewform?usp=header"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
def fill_form(address, price, link):
    driver.get(GOOGLE_FORM)
    time.sleep(6)
    address_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@jsname="YPqjbf"]')))
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address_input.send_keys(address)
    price_input.send_keys(price)
    link_input.send_keys(link)

    time.sleep(2)
    submit_btn.click()

response = requests.get(ZILLOW_URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

prices = [price.text.split()[0].replace("/mo", "") for price in soup.select("#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > div.StyledPropertyCardDataArea-fDSTNn > div > span")]
addresses = [address.text.strip() for address in soup.select("#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a > address")]
links = [link.get("href") for link in soup.select("#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a")]


num = 0
for a in addresses:
    fill_form(a, prices[num], links[num])
    num += 1

print("All data from research successfully saved!!!")
driver.quit()
