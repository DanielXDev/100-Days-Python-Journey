import random
import smtplib
import datetime as dt
import pandas
from dotenv import load_dotenv
import os
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

load_dotenv()

birthdays = pandas.read_csv("birthdays.csv")
date = dt.datetime.now()
my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

for (index, row) in birthdays.iterrows():
    if row.day == 26:
        random_num = random.randint(1,3)
        with open(f"letter_templates/letter_{random_num}.txt") as letter:
            letter_to_send = letter.read()
            letter_to_send= letter_to_send.replace("[NAME]", f"{row['name']}")
            print(letter_to_send)
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f"Subject: Wishes!!!\n\n{letter_to_send}"
            )