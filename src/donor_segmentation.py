```python
import pandas as pd
from src.utils import Donor

def segmentDonors(donor_data):
    high_level_donors = []
    low_level_donors = []

    for donor in donor_data:
        if donor.donation_history.mean() > 500:  # Arbitrary threshold for high-level donors
            high_level_donors.append(donor)
        else:
            low_level_donors.append(donor)

    return high_level_donors, low_level_donors

def loadDonorData(file_path):
    donor_data_df = pd.read_excel(file_path)
    donor_data = []

    for index, row in donor_data_df.iterrows():
        donor = Donor(name=row['name'], email=row['email'], donation_history=row['donation_history'])
        donor_data.append(donor)

    return donor_data

if __name__ == "__main__":
    donor_data = loadDonorData('donor_data.xlsx')
    high_level_donors, low_level_donors = segmentDonors(donor_data)

    print(f"Number of high-level donors: {len(high_level_donors)}")
    print(f"Number of low-level donors: {len(low_level_donors)}")
```