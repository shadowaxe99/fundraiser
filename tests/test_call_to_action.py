```python
import unittest
from src.call_to_action import schedule_call

class TestCallToAction(unittest.TestCase):

    def setUp(self):
        self.high_level_donors = [
            {"name": "Donor A", "email": "donorA@example.com", "donation_amount": 5000},
            {"name": "Donor B", "email": "donorB@example.com", "donation_amount": 10000},
        ]

    def test_schedule_call(self):
        for donor in self.high_level_donors:
            result = schedule_call(donor)
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
```