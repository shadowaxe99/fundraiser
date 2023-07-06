```python
from src.email_generation import generate_email
from src.utils import send_email

def promote_recurring_donation(donor_data, email_templates):
    for donor in donor_data:
        if donor['donation_frequency'] == 'low':
            email = generate_email(donor, email_templates['recurring_donation'])
            send_email(email)

def setup_recurring_donation(donor, donation_amount):
    donor['recurring_donation'] = True
    donor['donation_amount'] = donation_amount
    return donor
```