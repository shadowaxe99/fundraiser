# Fundraising Automation for Charity User Manual

## Getting Started

1. **Installation**: Clone the repository and install the required dependencies by running `pip install -r requirements.txt` in your terminal.

2. **Data Import**: Prepare your Excel document with potential donor information. The document should include contact details and donation history.

## Usage

### Importing Donor Data

1. Run `src/main.py` in your terminal.
2. Click on the `upload-button` to upload your Excel document.
3. The system will extract relevant information and organize it for further processing.

### Customizing Email Templates

1. Navigate to the `email-template-config` section.
2. Customize your email templates as needed. The system will use these templates to generate personalized emails for each potential donor.

### Monitoring Fundraising Progress

1. Navigate to the `donation-progress` section to monitor the progress of your fundraising campaign.

## Features

### Donor Segmentation

The system will analyze the donor history and categorize donors as high-level or low-level based on predefined criteria, such as donation amounts or frequency.

### Call-to-Action for High-Level Donors

The system will include a call-to-action in the customized email encouraging high-level donors to schedule a call with a representative of the charity organization.

### Online Donation for Low-Level Donors

The system will direct low-level donors to a user-friendly online donation platform through a customized email. It will provide clear instructions and links to facilitate online donations quickly and securely.

### Recurring Donation Promotion

The system will emphasize the benefits of recurring donations to online donors, highlighting the impact of sustained support on the charity's mission. It will provide options and incentives to encourage donors to set up recurring donations conveniently.

## Troubleshooting

If you encounter any issues while using the system, please refer to `docs/developer_guide.md` for more detailed information on how the system works. If the issue persists, please raise an issue in the repository.

## Conclusion

The Fundraising Automation for Charity system aims to streamline the fundraising process, allowing your organization to efficiently reach out to potential donors. By leveraging GPT-3.5, it ensures personalized communication, effective donor segmentation, and promotes recurring donations.