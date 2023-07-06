# Fundraising Automation for Charity

This project aims to develop a system that automates the fundraising process for a charity organization. Leveraging GPT-3.5 as the logic engine, this system takes an input Excel document, sends customized emails to potential donors, and encourages high-level donors to schedule a call while prompting low-level donors to make online donations. Additionally, the system aims to promote recurring donations for online donors.

## Objectives

- Streamline Fundraising: Automate the manual tasks involved in the fundraising process, allowing the organization to efficiently reach out to potential donors.
- Personalized Communication: Generate customized emails using GPT-3.5, ensuring that each communication resonates with the recipient and increases the likelihood of positive engagement.
- Donor Segmentation: Identify high-level donors who warrant personalized follow-ups and encourage them to schedule a call. Prompt low-level donors to make online donations seamlessly.
- Promote Recurring Donations: Encourage online donors to consider recurring donation options for sustained support to the charity.

## Features and Functionality

- Data Import: Accept an Excel document as input containing potential donor information, including contact details and donation history.
- Customized Email Generation: Utilize GPT-3.5 as the logic engine to generate personalized emails for each potential donor.
- Donor Segmentation: Analyze donor history and categorize donors as high-level or low-level based on predefined criteria.
- Call Scheduling for High-Level Donors: Identify high-level donors and include a call-to-action in the customized email encouraging them to schedule a call with a representative of the charity organization.
- Online Donation for Low-Level Donors: Direct low-level donors to a user-friendly online donation platform through a customized email.
- Recurring Donation Promotion: Emphasize the benefits of recurring donations to online donors, highlighting the impact of sustained support on the charity's mission.

## User Interface (UI) and User Experience (UX)

Develop an intuitive and user-friendly interface for uploading the Excel document, configuring email templates, and monitoring the fundraising progress.

## Integration and Compatibility

Design the system to be compatible with standard Excel file formats and popular email platforms to facilitate seamless integration into existing workflows.

## Installation

To install the dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the main script, navigate to the src directory and run:

```
python main.py
```

## Testing

To run the tests, navigate to the src/tests directory and run:

```
python -m unittest discover
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)