```python
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.data_import import import_data
from src.email_generation import generate_email

def integrate_system(excel_file, email_server, email_port, email_user, email_password):
    # Import data from Excel file
    donor_data = import_data(excel_file)

    # Connect to the email server
    server = smtplib.SMTP(email_server, email_port)
    server.starttls()
    server.login(email_user, email_password)

    # Iterate over the donor data
    for index, donor in donor_data.iterrows():
        # Generate the email
        email = generate_email(donor)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = donor['email']
        msg['Subject'] = email['subject']
        msg.attach(MIMEText(email['body'], 'plain'))

        # Send the email
        server.send_message(msg)

    # Close the connection to the server
    server.quit()
```