import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

#Load variable
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

session = requests.Session()
response = session.get(URL, headers=header, timeout=10)
website = response.text

#Get product price and name
soup = BeautifulSoup(website, "html.parser")
price = soup.find("span", class_="aok-offscreen")
price_num = float(price.getText().split()[0].replace("$", ""))
product_title = soup.find("span", id="productTitle").getText()
product = " ".join(product_title.split())
print(product)
print(price_num)

msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Price Alert"
msg.attach(MIMEText(f"{product} is now ${price_num}. \n\n Go get it now {URL}", "plain", "utf-8"))

#Listen to when price crosses below price threshold
if price_num < 100:
    try:
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=RECEIVER,
                msg=msg.as_string()
            )
    except Exception as e:
        print(e)
    else:
        print("Email sent...")