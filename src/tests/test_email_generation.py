```python
import unittest
from src.email_generation import generateEmail

class TestEmailGeneration(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'donation_history': [100, 200, 300],
            'alignment_with_mission': 'High'
        }

    def test_generateEmail(self):
        email_subject, email_body = generateEmail(self.donor_data)
        
        self.assertIn(self.donor_data['name'], email_subject)
        self.assertIn(self.donor_data['name'], email_body)
        self.assertIn(str(sum(self.donor_data['donation_history'])), email_body)
        self.assertIn(self.donor_data['alignment_with_mission'], email_body)

if __name__ == '__main__':
    unittest.main()
```