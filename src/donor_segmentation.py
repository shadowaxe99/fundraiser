```python
import pandas as pd
from typing import List, Dict
from data_import import donor_data

# Define the donation threshold for high-level and low-level donors
HIGH_LEVEL_DONATION_THRESHOLD = 5000

def segment_donors(donor_data: pd.DataFrame) -> Dict[str, List[Dict]]:
    """
    Segments donors into high-level and low-level groups based on their donation history.
    """
    high_level_donors = []
    low_level_donors = []

    for index, donor in donor_data.iterrows():
        if donor['total_donations'] >= HIGH_LEVEL_DONATION_THRESHOLD:
            high_level_donors.append(donor)
        else:
            low_level_donors.append(donor)

    return {
        'high_level_donors': high_level_donors,
        'low_level_donors': low_level_donors
    }

# Segment the donors and store the results in the exported variables
donor_segments = segment_donors(donor_data)
high_level_donors = donor_segments['high_level_donors']
low_level_donors = donor_segments['low_level_donors']
```