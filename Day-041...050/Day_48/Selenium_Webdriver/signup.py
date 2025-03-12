from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


fname_input = driver.find_element(By.NAME, value="fName")
lname_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")

fname_input.send_keys("thebedev")
lname_input.send_keys("se")
email_input.send_keys("thebedev@gmail.com", Keys.ENTER)


time.sleep(5)
driver.quit()