from unittest import TestCase
from unittest.mock import patch
import io

from books import valid_new_location


class TestValidNewLocation(TestCase):

    @patch('builtins.input', side_effect=['34'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_new_location_both_numbers_and_letters(self, mock_stdout, mock_input):
        collection = ['6', '10', '12', '16', '34', 'Noguchi', 'Reading']
        actual = valid_new_location(collection)
        expected_return = "34"
        expected_print = "You can move the book to one of these shelves:\n" \
                         "1: 6\n2: 10\n3: 12\n4: 16\n5: 34\n6: Noguchi\n7: Reading\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
        self.assertEqual(expected_return, actual)

    @patch('builtins.input', side_effect=['Noguchi'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_new_location_only_letters(self, mock_stdout, mock_input):
        collection = ['Island', 'Noguchi', 'Reading']
        actual = valid_new_location(collection)
        expected_return = "Noguchi"
        expected_print = "You can move the book to one of these shelves:\n" \
                         "1: Island\n2: Noguchi\n3: Reading\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
        self.assertEqual(expected_return, actual)

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_new_location_only_numbers(self, mock_stdout, mock_input):
        collection = ['6', '10', '12', '16', '34']
        actual = valid_new_location(collection)
        expected_return = "6"
        expected_print = "You can move the book to one of these shelves:\n" \
                         "1: 6\n2: 10\n3: 12\n4: 16\n5: 34\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
        self.assertEqual(expected_return, actual)

    @patch('builtins.input', side_effect=['Wrong input'])
    def test_valid_new_location_not_a_valid_input(self, mock_input):

        collection = ['6', '10', '12', '16', '34', 'Noguchi', 'Reading']

        self.assertRaises(ValueError, valid_new_location, collection)
