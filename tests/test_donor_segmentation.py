```python
import unittest
from src.donor_segmentation import segment_donors

class TestDonorSegmentation(unittest.TestCase):

    def setUp(self):
        self.donor_data = [
            {"name": "Donor1", "donation_amount": 5000, "donation_frequency": "monthly"},
            {"name": "Donor2", "donation_amount": 100, "donation_frequency": "yearly"},
            {"name": "Donor3", "donation_amount": 10000, "donation_frequency": "quarterly"},
            {"name": "Donor4", "donation_amount": 50, "donation_frequency": "monthly"},
        ]

    def test_segment_donors(self):
        high_level_donors, low_level_donors = segment_donors(self.donor_data)
        
        # Check if the segmentation is correct
        self.assertEqual(len(high_level_donors), 2)
        self.assertEqual(len(low_level_donors), 2)

        # Check if the correct donors are in the high-level group
        self.assertTrue(any(donor["name"] == "Donor1" for donor in high_level_donors))
        self.assertTrue(any(donor["name"] == "Donor3" for donor in high_level_donors))

        # Check if the correct donors are in the low-level group
        self.assertTrue(any(donor["name"] == "Donor2" for donor in low_level_donors))
        self.assertTrue(any(donor["name"] == "Donor4" for donor in low_level_donors))

if __name__ == "__main__":
    unittest.main()
```