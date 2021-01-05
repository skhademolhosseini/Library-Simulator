from unittest import TestCase
from unittest.mock import patch

from books import get_book_by_index


class TestGetBookByIndex(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_book_by_index_first_book(self, mock_input):
        collection = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Castle of Wizardry', 'Publisher': '\
None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        actual = get_book_by_index(collection)
        expected = {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_book_by_index_second_book(self, mock_input):
        collection = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Castle of Wizardry', 'Publisher': '\
None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        actual = get_book_by_index(collection)
        expected = {'Author': 'Eddings', 'Title': 'Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_book_by_index_collection_contains_similar_books(self, mock_input):
        collection = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': '\
None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}]
        actual = get_book_by_index(collection)
        expected = {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}
        self.assertEqual(expected, actual)
