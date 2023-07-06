```python
import unittest
from src import data_import

class TestDataImport(unittest.TestCase):

    def setUp(self):
        self.donor_data = data_import.import_data('test_data.xlsx')

    def test_data_import(self):
        self.assertIsNotNone(self.donor_data, "Data import failed. Returned None.")

    def test_data_structure(self):
        self.assertIsInstance(self.donor_data, list, "Data import failed. Not a list.")
        self.assertGreater(len(self.donor_data), 0, "Data import failed. List is empty.")

    def test_donor_schema(self):
        donor = self.donor_data[0]
        self.assertIn('name', donor, "Data import failed. 'name' not in donor data.")
        self.assertIn('contact_details', donor, "Data import failed. 'contact_details' not in donor data.")
        self.assertIn('donation_history', donor, "Data import failed. 'donation_history' not in donor data.")

if __name__ == '__main__':
    unittest.main()
```