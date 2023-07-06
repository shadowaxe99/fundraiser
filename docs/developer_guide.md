# Developer Guide

## Getting Started

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in the root directory of the project.

## Project Structure

The project is structured as follows:

- `src/`: Contains the source code for the application.
- `tests/`: Contains the test cases for the application.
- `docs/`: Contains the documentation for the application.

## Source Code

The source code is divided into several modules, each responsible for a specific functionality:

- `main.py`: The entry point of the application.
- `data_import.py`: Handles the import of data from the Excel document.
- `email_generation.py`: Generates personalized emails for each potential donor.
- `donor_segmentation.py`: Segments donors into high-level and low-level groups.
- `call_to_action.py`: Includes a call-to-action in the customized email for high-level donors.
- `online_donation.py`: Facilitates online donations for low-level donors.
- `recurring_donation.py`: Promotes recurring donations to online donors.
- `user_interface.py`: Manages the user interface of the application.
- `integration_compatibility.py`: Ensures the compatibility of the system with Excel and email platforms.
- `utils.py`: Contains utility functions used across the application.

## Testing

The test cases for the application are located in the `tests/` directory. To run the tests, use the command `pytest`.

## Documentation

The user manual and this developer guide are located in the `docs/` directory.

## Contributing

When contributing to this project, please ensure that your code adheres to the style guide and that all tests pass before submitting a pull request.