import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4150453572&f_AL=true&f_WT=2&geoId=92000000&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
# driver.maximize_window()


#Sign in
time.sleep(3)
signin_btn = driver.find_element(By.CSS_SELECTOR, value="#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button")
signin_btn.click()

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
phone_number = os.getenv("NUMBER")

email_input = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal_session_key")
password_input = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal_session_password")
submit_btn = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal > div > section > div > div > form > div.flex.justify-between.sign-in-form__footer--full-width > button")

time.sleep(2)
email_input.send_keys(email)
time.sleep(2)
password_input.send_keys(password)
time.sleep(2)
submit_btn.click()


time.sleep(20)
jobs_list = driver.find_elements(By.CLASS_NAME, "job-card-list")


def safe_click(driver, css_selector, timeout=5):
    #Waits for an element to be clickable and clicks it.
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()
        return True  # Indicate success
    except Exception as e:
        print(f"Could not click {css_selector}: {e}")
        return False  # Indicate failure
for job in jobs_list:
    try:
        modal = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".artdeco-modal-overlay"))
        )

        # Click the "Discard" button
        discard_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Discard')]"))
        )
        discard_button.click()
        print("Clicked 'Discard' successfully.")

    except Exception as e:
        print("Error handling the pop-up:", e)
    job.click()
    time.sleep(3)
    # ----- Easy Apply -----#
    time.sleep(4)
    apply_btn = driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > div.mt4 > div > div > div > button")
    apply_btn.click()

    number_input = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--container input")
    number_input.clear()
    number_input.send_keys(phone_number)

    driver.find_element(By.CSS_SELECTOR, ".pv4 .artdeco-button").click()
    time.sleep(2)

    safe_click(driver, ".pv4 .artdeco-button--primary")
    time.sleep(2)
    # Try clicking the primary button first
    if not safe_click(driver, ".pv4 .artdeco-button--primary"):
        # If the first click fails, try alternative buttons
        safe_click(driver, ".artdeco-button")

    # Additional click after a delay if previous clicks were successful
    time.sleep(3)
    safe_click(driver, ".artdeco-button")


# driver.quit()