from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

date_lists = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li a")
starter = 0
upcoming_events = {}
for n in date_lists:
    upcoming_events[f'{starter}'] = {
        "time": n.text,
        "event": events[starter].text
    }
    starter +=1
print(upcoming_events)



driver.quit()