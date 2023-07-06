```python
import unittest
from src import email_generation

class TestEmailGeneration(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'contact': 'johndoe@example.com',
            'donation_history': [100, 200, 300],
            'alignment': 'Supports education initiatives'
        }
        self.email_templates = {
            'subject': 'Thank you for your support, {name}!',
            'body': 'Dear {name},\n\nWe noticed that you have been a generous supporter of our cause. Your last donation was {last_donation}. We would like to express our gratitude and encourage you to continue supporting our mission: {alignment}.\n\nBest,\nCharity Team'
        }

    def test_generate_email(self):
        email = email_generation.generate_email(self.donor_data, self.email_templates)
        self.assertEqual(email['recipient'], self.donor_data['contact'])
        self.assertEqual(email['subject'], self.email_templates['subject'].format(name=self.donor_data['name']))
        self.assertEqual(email['body'], self.email_templates['body'].format(name=self.donor_data['name'], last_donation=self.donor_data['donation_history'][-1], alignment=self.donor_data['alignment']))

if __name__ == '__main__':
    unittest.main()
```