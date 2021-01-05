from unittest import TestCase
from unittest.mock import patch
import io

from books import move_book


class TestMoveBook(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_complete_dictionary_new_location_is_number(self, mock_stdout):
        move_book({'Author': 'Dupre', 'Title': 'Sky', 'Publisher': 'BD&L', 'Shelf': '12', '\
        Category': 'Architecture', 'Subject': '20th Century'}, "6")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: 6\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_complete_dictionary_new_location_is_letter(self, mock_stdout):
        move_book({'Author': 'Dupre', 'Title': 'Sky', 'Publisher': 'BD&L', 'Shelf': '12', '\
                Category': 'Architecture', 'Subject': '20th Century'}, "Bedroom shelf")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: Bedroom shelf\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_complete_dictionary_new_location_same_as_old_location(self, mock_stdout):
        move_book({'Author': 'Dupre', 'Title': 'Sky', 'Publisher': 'BD&L', 'Shelf': '12', '\
                Category': 'Architecture', 'Subject': '20th Century'}, "12")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: 12\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_complete_dictionary_new_location_mixed_characters(self, mock_stdout):
        move_book({'Author': 'Dupre', 'Title': 'Sky', 'Publisher': 'BD&L', 'Shelf': '12', '\
                Category': 'Architecture', 'Subject': '20th Century'}, "123NEW8location")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: 123NEW8location\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_only_Shelf_key_new_location_is_number(self, mock_stdout):
        move_book({'Shelf': '12'}, "34")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: 34\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_only_Shelf_key_new_location_is_letter(self, mock_stdout):
        move_book({'Shelf': '12'}, "Noguchi")
        expected_print = "The book was successfully move to the new location\n" \
                         "New Shelf: Noguchi\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
