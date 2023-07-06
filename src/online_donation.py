```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD
from src.utils import get_donation_link

def make_online_donation(low_level_donors):
    for donor in low_level_donors:
        send_donation_email(donor)

def send_donation_email(donor):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = donor.email
    msg['Subject'] = "Support Our Cause"

    body = f"""
    Dear {donor.name},

    Thank you for your continued support. We invite you to make an online donation to our cause.

    Please follow this link to make your donation: {get_donation_link()}

    Thank you,
    Your Charity Team
    """

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, donor.email, text)
    server.quit()
```