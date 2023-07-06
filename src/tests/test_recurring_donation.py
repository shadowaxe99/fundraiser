```python
import unittest
from src.recurring_donation import promoteRecurringDonation

class TestRecurringDonation(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'donation_history': [100, 200, 150]
        }

    def test_promote_recurring_donation(self):
        result = promoteRecurringDonation(self.donor_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```