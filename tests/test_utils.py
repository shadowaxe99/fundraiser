import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.donor_data = {
            'name': 'John Doe',
            'contact': 'johndoe@example.com',
            'donation_history': [100, 200, 300]
        }
        self.email_template = {
            'recipient': 'johndoe@example.com',
            'subject': 'Thank you for your support',
            'body': 'Dear John Doe, thank you for your generous donations...'
        }

    def test_import_data(self):
        result = utils.import_data('test_data.xlsx')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_generate_email(self):
        result = utils.generate_email(self.donor_data, self.email_template)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['recipient'], self.email_template['recipient'])

    def test_segment_donors(self):
        result = utils.segment_donors(self.donor_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('high_level_donors', result)
        self.assertIn('low_level_donors', result)

    def test_schedule_call(self):
        result = utils.schedule_call(self.donor_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('call_scheduled', result)

    def test_make_online_donation(self):
        result = utils.make_online_donation(self.donor_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('donation_made', result)

    def test_promote_recurring_donation(self):
        result = utils.promote_recurring_donation(self.donor_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('recurring_donation_set', result)

    def test_init_ui(self):
        result = utils.init_ui()
        self.assertIsNotNone(result)

    def test_integrate_system(self):
        result = utils.integrate_system()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()