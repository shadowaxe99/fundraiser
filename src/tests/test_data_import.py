```python
import unittest
from src import data_import

class TestDataImport(unittest.TestCase):

    def setUp(self):
        self.donor_data = data_import.importData('test_data.xlsx')

    def test_data_import(self):
        self.assertIsNotNone(self.donor_data, "Failed to import data")

    def test_data_structure(self):
        sample_donor = self.donor_data[0]
        self.assertTrue('name' in sample_donor)
        self.assertTrue('email' in sample_donor)
        self.assertTrue('donation_history' in sample_donor)

    def test_data_values(self):
        sample_donor = self.donor_data[0]
        self.assertIsInstance(sample_donor['name'], str)
        self.assertIsInstance(sample_donor['email'], str)
        self.assertIsInstance(sample_donor['donation_history'], list)

if __name__ == '__main__':
    unittest.main()
```