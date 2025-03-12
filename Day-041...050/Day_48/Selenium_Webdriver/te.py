import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.set_page_load_timeout(150)

# Select language
time.sleep(5)
language = driver.find_element(By.CLASS_NAME, value="langSelectButton")
language.click()

# Global stop flag
stop_flag = False


def check_for_upgrade():
    prices = driver.find_elements(By.CSS_SELECTOR, value="#products .price")
    cookies = int(driver.find_element(By.ID, value="cookies").text.split()[0].replace(",", "").strip())

    # Convert prices, handling empty strings
    upgrades_list = []
    for price in prices:
        price_text = price.text.strip().replace(",", "")
        if price_text:
            upgrades_list.append(int(price_text))

    affordable_upgrades = [price for price in upgrades_list if price < cookies]

    # Try clicking upgrade
    try:
        driver.find_element(By.CSS_SELECTOR, value="#upgrades .enabled").click()
    except Exception as e:
        print(e)

    if affordable_upgrades:
        most_expensive_upgrade = max(affordable_upgrades)
        index_of_upgrade = upgrades_list.index(most_expensive_upgrade)
        try:
            driver.find_element(By.ID, value=f"product{index_of_upgrade}").click()
        except Exception as e:
            print(f'Upgrade failed: {e}')





# Click cookie
cookie = driver.find_element(By.ID, value="bigCookie")

timeout = 30  # [seconds]
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    for n in range(50):
        cookie.click()

    check_for_upgrade()


# Print final results and quit
cookies_per_second = driver.find_element(By.ID, value="cookies").text.split(":")[1].strip()
print(f'Cookies/seconds {cookies_per_second}')
driver.quit()
