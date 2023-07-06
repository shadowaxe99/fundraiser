```python
# src/config.py

# Define the configuration parameters for the application

# File paths
EXCEL_FILE_PATH = "path/to/excel/file"
EMAIL_TEMPLATE_PATH = "path/to/email/template"

# Email settings
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "username@example.com"
EMAIL_PASSWORD = "password"

# Donation platform URL
DONATION_PLATFORM_URL = "https://donation-platform.example.com"

# Donor segmentation criteria
HIGH_LEVEL_DONOR_CRITERIA = {
    "min_donation_amount": 1000,
    "min_donation_frequency": 4
}

LOW_LEVEL_DONOR_CRITERIA = {
    "max_donation_amount": 999,
    "max_donation_frequency": 3
}

# UI element IDs
UI_ELEMENT_IDS = {
    "upload_file": "upload-file",
    "email_template": "email-template",
    "donation_link": "donation-link",
    "progress_indicator": "progress-indicator"
}

# Event names
EVENT_NAMES = {
    "email_generated": "emailGenerated",
    "donor_segmented": "donorSegmented",
    "call_scheduled": "callScheduled",
    "donation_made": "donationMade"
}
```