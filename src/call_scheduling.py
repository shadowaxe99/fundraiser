```python
from src.email_generation import generateEmail
from src.utils import sendEmail

def scheduleCall(high_level_donors):
    for donor in high_level_donors:
        email_subject = "Invitation to Schedule a Call with Our Charity Organization"
        email_body = generateEmail(donor, email_subject, call_to_action=True)
        sendEmail(donor.email, email_subject, email_body)

    print("Call scheduling emails have been sent to high-level donors.")
```