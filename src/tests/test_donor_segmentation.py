```python
import unittest
from src.donor_segmentation import segmentDonors

class TestDonorSegmentation(unittest.TestCase):

    def setUp(self):
        self.donor_data = [
            {"name": "Donor1", "email": "donor1@example.com", "donation_history": [100, 200]},
            {"name": "Donor2", "email": "donor2@example.com", "donation_history": [50]},
            {"name": "Donor3", "email": "donor3@example.com", "donation_history": [500, 300, 200]},
            {"name": "Donor4", "email": "donor4@example.com", "donation_history": [30, 20]},
        ]

    def test_segmentDonors(self):
        high_level_donors, low_level_donors = segmentDonors(self.donor_data)
        
        # Check if the segmentation is correct
        self.assertEqual(len(high_level_donors), 2)
        self.assertEqual(len(low_level_donors), 2)

        # Check if the correct donors are in the high-level group
        self.assertEqual(high_level_donors[0]['name'], 'Donor1')
        self.assertEqual(high_level_donors[1]['name'], 'Donor3')

        # Check if the correct donors are in the low-level group
        self.assertEqual(low_level_donors[0]['name'], 'Donor2')
        self.assertEqual(low_level_donors[1]['name'], 'Donor4')

if __name__ == '__main__':
    unittest.main()
```