from unittest import TestCase
from unittest.mock import patch
import io

from books import menu


class TestMenu(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_menu_input_is_1(self, mock_input):
        actual = menu()
        expected = "search"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_menu_input_is_2(self, mock_input):
        actual = menu()
        expected = "move"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_menu_input_is_3(self, mock_input):
        actual = menu()
        expected = "quit"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_first_input_not_in_range(self, mock_stdout, mock_input):
        actual = menu()
        expected_return = "search"
        expected_print = "Invalid input, try again\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
        self.assertEqual(expected_return, actual)

    @patch('builtins.input', side_effect=['app', '0', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_first_input_string_second_input_not_in_range(self, mock_stdout, mock_input):
        actual = menu()
        expected_return = "move"
        expected_print = "Invalid input, try again\n" \
                         "Invalid input, try again\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
        self.assertEqual(expected_return, actual)
