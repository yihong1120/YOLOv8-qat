import unittest
from unittest.mock import patch, MagicMock
import os

# Import the main function
from main import main

class TestMain(unittest.TestCase):

    @patch('main.Trainer')
    @patch('main.Tester')
    @patch('main.util.load_config')
    @patch('os.makedirs')
    @patch('os.getenv')
    @patch('sys.argv', ['main.py', '--train'])
    def test_main_train(self, mock_getenv, mock_makedirs, mock_load_config, mock_tester, mock_trainer):
        """
        Test the main function for training scenario.
        """
        # Set up mock environment
        mock_getenv.side_effect = lambda x, default: {'LOCAL_RANK': '0', 'WORLD_SIZE': '1'}.get(x, default)
        mock_load_config.return_value = MagicMock()

        # Call the main function
        main()

        # Assertions to verify the correct calls were made
        mock_makedirs.assert_called_once_with('weights')
        mock_load_config.assert_called_once_with('utils/args.yaml')
        mock_trainer.assert_called_once()

    @patch('main.Trainer')
    @patch('main.Tester')
    @patch('main.util.load_config')
    @patch('os.makedirs')
    @patch('os.getenv')
    @patch('sys.argv', ['main.py', '--test'])
    def test_main_test(self, mock_getenv, mock_makedirs, mock_load_config, mock_tester, mock_trainer):
        """
        Test the main function for testing scenario.
        """
        # Set up mock environment
        mock_getenv.side_effect = lambda x, default: {'LOCAL_RANK': '0', 'WORLD_SIZE': '1'}.get(x, default)
        mock_load_config.return_value = MagicMock()

        # Call the main function
        main()

        # Assertions to verify the correct calls were made
        mock_makedirs.assert_not_called()
        mock_load_config.assert_called_once_with('utils/args.yaml')
        mock_tester.assert_called_once()

if __name__ == '__main__':
    unittest.main()