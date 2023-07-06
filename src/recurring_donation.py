```python
from src.utils import send_email
from src.constants import RECURRING_DONATION_EMAIL_TEMPLATE

def promote_recurring_donation(donor_data, low_level_donors):
    for donor in low_level_donors:
        donor_info = donor_data[donor]
        email_content = RECURRING_DONATION_EMAIL_TEMPLATE.format(donor_info['name'])
        send_email(donor_info['email'], "Consider Recurring Donations", email_content)
```