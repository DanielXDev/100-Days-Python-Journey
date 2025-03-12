from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount > ul > li:nth-child(1) > a")
print(active_editors.text)

#Sending keys to the input
search_input = driver.find_element(By.NAME, value="search")
search_input.send_keys("Python", Keys.ENTER)




time.sleep(5)
driver.quit()