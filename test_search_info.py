from unittest import TestCase
from unittest.mock import patch

from books import search_info


class TestSearchInfo(TestCase):

    @patch('builtins.input', side_effect=['Title', 'edd'])
    def test_search_info_capitalized_first_input(self, mock_input):
        actual = search_info()
        expected = ('Title', 'edd')
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['SHELF', '16'])
    def test_search_info_all_capitalized_first_input(self, mock_input):
        actual = search_info()
        expected = ('Shelf', '16')
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['PubLISheR', 'BD&L'])
    def test_search_info_mixed_case_first_input(self, mock_input):
        actual = search_info()
        expected = ('Publisher', 'BD&L')
        self.assertEqual(expected, actual)
