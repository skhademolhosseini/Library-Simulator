from unittest import TestCase
from unittest.mock import patch
import io

from books import print_as_ordered_list


class TestPrintAsOrderedList(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_as_ordered_list_different_books(self, mock_stdout):
        collection = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        print_as_ordered_list(collection)
        expected_print = "There are 4 books in the library that contain the keyword you are looking for:\n\n"\
                         "1:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "2:\nAuthor: Eddings\nTitle: Castle of Wizardry\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "3:\nAuthor: Eddings\nTitle: Demon Lord of Karanda\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "4:\nAuthor: Eddings\nTitle: Enchanter's End Game\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n"

        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_as_ordered_list_same_book(self, mock_stdout):
        collection = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '\
34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}]
        print_as_ordered_list(collection)
        expected_print = "There are 2 books in the library that contain the keyword you are looking for:\n\n"\
                         "1:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "2:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n"

        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_as_ordered_list_empty_list(self, mock_stdout):
        collection = []
        print_as_ordered_list(collection)
        expected_print = "There are 0 books in the library that contain the keyword you are looking for:\n\n"\

        self.assertEqual(expected_print, mock_stdout.getvalue())
