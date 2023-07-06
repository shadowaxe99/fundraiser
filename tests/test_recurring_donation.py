```python
import unittest
from src import recurring_donation

class TestRecurringDonation(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'donation_history': [100, 200, 300],
            'recurring': False
        }

    def test_promote_recurring_donation(self):
        result = recurring_donation.promote_recurring_donation(self.donor_data)
        self.assertTrue(result)

    def test_recurring_donation_email_content(self):
        email_content = recurring_donation.generate_recurring_donation_email(self.donor_data)
        self.assertIn('recurring donation', email_content.lower())
        self.assertIn(self.donor_data['name'], email_content)

    def test_recurring_donation_link(self):
        link = recurring_donation.generate_recurring_donation_link(self.donor_data)
        self.assertTrue(link.startswith('http'))

if __name__ == '__main__':
    unittest.main()
```