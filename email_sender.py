import smtplib
import pandas as pd
from email.message import EmailMessage
import os

#------SETTING-------*
EMAIL_ADDRESS = "akashkumar11jul@gmail.com"
EMAIL_PASSWORD = "kvcfkolhnxkweysa"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

#------Read Email List-----
df = pd.read_csv('email_list.csv')

#------Email Content------
subject = "Greetings from Akash Kumar!"
body = """Hi There,

This is an autonated generated email sent via python.

Regards
Akash Kumar
"""
#-------ATTACHMENT PATH------
attachment_path = "attachment/sample.pdf"

#--------SEND EMAIL----------
def send_email(to_email):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach File
    if os.path.exists(attachment_path):
        with open(attachment_path, 'rb')as f:
            file_data = f.read()
            file_name = os.path.basement(f.name)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Send via SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Email sent to{to_email}")

# --------LOOP THROUGH RECIPIENTS---------
for _, row in df.iterrows():
    send_email(row['email'])

