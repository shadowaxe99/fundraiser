```python
import unittest
from src.online_donation import makeOnlineDonation

class TestOnlineDonation(unittest.TestCase):

    def setUp(self):
        self.low_level_donors = [
            {
                'name': 'Donor 1',
                'email': 'donor1@example.com',
                'donation_history': [50, 30, 20]
            },
            {
                'name': 'Donor 2',
                'email': 'donor2@example.com',
                'donation_history': [25, 15]
            }
        ]

    def test_make_online_donation(self):
        for donor in self.low_level_donors:
            response = makeOnlineDonation(donor)
            self.assertEqual(response.status_code, 200)
            self.assertIn('donationMade', response.json())

if __name__ == '__main__':
    unittest.main()
```