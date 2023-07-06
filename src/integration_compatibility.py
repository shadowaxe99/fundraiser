```python
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

def integrate(file_path):
    try:
        donor_data = pd.read_excel(file_path)
        return donor_data
    except Exception as e:
        print(f"Error in reading Excel file: {e}")
        return None

def send_email(to_address, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Error in sending email: {e}")
```