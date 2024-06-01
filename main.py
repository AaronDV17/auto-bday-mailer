import smtplib
import datetime as dt
import pandas as pd
from random import choice
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()

# Get email credentials from environment variables
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASS = os.environ["MY_PASS"]

# Create an empty recipients list
recipients = []


def populate_recipients():
    """
    Check if today's date matches the date of anyone's birthday in the birthdays.csv file &
    append the relevant peoples details (name & email address) as a dictionary to the recipients list
    """
    now = dt.datetime.now()
    today_date = now.date()
    global recipients
    recipients = [
        {"name": row["name"], "email": row["email"]}
        for _, row in data.iterrows()
        if (today_date.month, today_date.day) == (row["month"], row["day"])
    ]


def add_message():
    """
    Adds a personalized birthday message to each recipient in the list.
    """
    message_list = os.listdir("./letter_templates")
    for recipient in recipients:
        with open(file=f"./letter_templates/{choice(message_list)}", mode='r') as f:
            contents = f.read()
        recipient['message'] = contents.replace("[NAME]", recipient["name"])


def send_emails():
    """
    Sends recipients their personalized birthday message
    """
    if len(recipients) > 0:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)

            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = MY_EMAIL
                msg['To'] = recipient['email']
                msg['Subject'] = f"Happy Birthday {recipient['name']}!"
                body = recipient['message'].replace('\n', '<br>')
                msg.attach(MIMEText(body, 'html', 'utf-8'))

                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=recipient['email'],
                    msg=msg.as_string()
                )


if __name__ == '__main__':
    data = pd.read_csv("birthdays.csv")

    populate_recipients()
    add_message()
    send_emails()
