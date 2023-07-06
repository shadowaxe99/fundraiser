```python
import unittest
from unittest.mock import patch
from src import user_interface as ui

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.init_ui')
    def test_init_ui(self, mock_init_ui):
        ui.init_ui()
        mock_init_ui.assert_called_once()

    @patch('src.user_interface.upload_button')
    def test_upload_button(self, mock_upload_button):
        ui.upload_button()
        mock_upload_button.assert_called_once()

    @patch('src.user_interface.email_template_config')
    def test_email_template_config(self, mock_email_template_config):
        ui.email_template_config()
        mock_email_template_config.assert_called_once()

    @patch('src.user_interface.donation_progress')
    def test_donation_progress(self, mock_donation_progress):
        ui.donation_progress()
        mock_donation_progress.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```