```python
from src.email_generation import generate_email

def schedule_call(donor):
    """
    Function to schedule a call with a high-level donor.
    """
    call_details = {
        "time": "to be decided",
        "date": "to be decided",
        "donor_name": donor["name"],
        "donor_email": donor["email"]
    }

    return call_details

def call_to_action(high_level_donors, email_templates):
    """
    Function to send a call-to-action to high-level donors.
    """
    for donor in high_level_donors:
        call_details = schedule_call(donor)
        email_subject = "Invitation to schedule a call with our charity organization"
        email_body = f"Dear {donor['name']},\n\nWe appreciate your generous support to our cause. We would like to invite you to schedule a call with us to discuss further collaboration. Please find the details below:\n\nCall Time: {call_details['time']}\nCall Date: {call_details['date']}\n\nLooking forward to speaking with you.\n\nBest,\n[Your Name]"
        email = generate_email(donor["email"], email_subject, email_body, email_templates)
        print(f"Email sent to {donor['name']}")
```