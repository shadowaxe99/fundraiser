```python
import pandas as pd

def load_excel_data(file_path):
    """
    Function to load data from an Excel file into a pandas DataFrame.
    """
    donor_data = pd.read_excel(file_path)
    return donor_data

def validate_email(email):
    """
    Function to validate an email address.
    """
    if '@' in email and '.' in email:
        return True
    return False

def validate_donation_amount(amount):
    """
    Function to validate a donation amount.
    """
    try:
        amount = float(amount)
        if amount > 0:
            return True
    except ValueError:
        pass
    return False

def validate_donation_frequency(frequency):
    """
    Function to validate a donation frequency.
    """
    try:
        frequency = int(frequency)
        if frequency > 0:
            return True
    except ValueError:
        pass
    return False
```