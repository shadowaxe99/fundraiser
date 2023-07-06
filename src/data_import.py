```python
import pandas as pd
from typing import List
from src.constants import Donor

def importData(filepath: str) -> List[Donor]:
    """
    Function to import data from the Excel document.
    """
    donor_data = pd.read_excel(filepath)
    donor_list = []

    for index, row in donor_data.iterrows():
        donor = Donor(name=row['name'], email=row['email'], donation_history=row['donation_history'])
        donor_list.append(donor)

    return donor_list
```