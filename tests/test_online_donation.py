```python
import unittest
from src import online_donation

class TestOnlineDonation(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'donation_history': [50, 100, 200],
            'donation_frequency': 'monthly'
        }
        self.low_level_donors = [self.donor_data]

    def test_make_online_donation(self):
        response = online_donation.make_online_donation(self.low_level_donors)
        self.assertEqual(response, 'Donation made successfully')

    def test_promote_recurring_donation(self):
        response = online_donation.promote_recurring_donation(self.low_level_donors)
        self.assertEqual(response, 'Recurring donation promoted successfully')

if __name__ == '__main__':
    unittest.main()
```