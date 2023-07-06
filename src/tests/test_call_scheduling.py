```python
import unittest
from src.call_scheduling import scheduleCall
from src.donor_segmentation import segmentDonors
from src.data_import import importData

class TestCallScheduling(unittest.TestCase):

    def setUp(self):
        self.donor_data = importData('test_data.xlsx')
        self.high_level_donors, self.low_level_donors = segmentDonors(self.donor_data)

    def test_scheduleCall(self):
        # Test if the function returns a call scheduled event for high-level donors
        for donor in self.high_level_donors:
            result = scheduleCall(donor)
            self.assertEqual(result, 'callScheduled')

    def test_noCallForLowLevelDonors(self):
        # Test if the function does not schedule a call for low-level donors
        for donor in self.low_level_donors:
            result = scheduleCall(donor)
            self.assertNotEqual(result, 'callScheduled')

if __name__ == '__main__':
    unittest.main()
```