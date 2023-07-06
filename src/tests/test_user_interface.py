```python
import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.initUI')
    def test_initUI(self, mock_initUI):
        user_interface.initUI()
        mock_initUI.assert_called_once()

    @patch('src.user_interface.upload_file')
    def test_upload_file(self, mock_upload_file):
        user_interface.upload_file('test_file.xlsx')
        mock_upload_file.assert_called_once_with('test_file.xlsx')

    @patch('src.user_interface.email_template')
    def test_email_template(self, mock_email_template):
        user_interface.email_template('test_template')
        mock_email_template.assert_called_once_with('test_template')

    @patch('src.user_interface.donation_link')
    def test_donation_link(self, mock_donation_link):
        user_interface.donation_link('test_link')
        mock_donation_link.assert_called_once_with('test_link')

    @patch('src.user_interface.progress_indicator')
    def test_progress_indicator(self, mock_progress_indicator):
        user_interface.progress_indicator(50)
        mock_progress_indicator.assert_called_once_with(50)

if __name__ == '__main__':
    unittest.main()
```