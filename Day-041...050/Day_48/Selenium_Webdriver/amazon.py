from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium_stealth import stealth

chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = "eager"
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(180)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()


price_dollars = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f'The product price is ${price_dollars}.{price_cents}')

driver.quit()