```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.utils import EmailSchema

def make_online_donation(donor, email_template):
    """
    Function to facilitate online donations for low-level donors.
    """
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Support Our Cause"
    msg['From'] = "charity@organization.com"
    msg['To'] = donor.email

    # Create the body of the message
    html = email_template.format(name=donor.name)

    # Record the MIME types
    part = MIMEText(html, 'html')

    # Attach parts into message container
    msg.attach(part)

    # Send the message via local SMTP server
    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

def send_donation_link(low_level_donors, email_template):
    """
    Function to send donation link to all low-level donors.
    """
    for donor in low_level_donors:
        make_online_donation(donor, email_template)
```