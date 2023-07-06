import pandas as pd
from typing import List
from src.utils import DonorSchema

def import_data(file_path: str) -> List[DonorSchema]:
    """
    Function to import data from an Excel document.
    :param file_path: Path to the Excel document.
    :return: List of DonorSchema objects.
    """
    donor_data = pd.read_excel(file_path)
    donor_list = []

    for index, row in donor_data.iterrows():
        donor = DonorSchema(
            name=row['name'],
            contact_details=row['contact_details'],
            donation_history=row['donation_history']
        )
        donor_list.append(donor)

    return donor_list
```
