from unittest import TestCase
from unittest.mock import patch
import io

from books import move_book_body

"""
In this unittest, we only check the situations when we catch an error. 
All other function used inside this function have passed their own unittest.
"""


class TestMoveBookBody(TestCase):

    @patch('builtins.input', side_effect=['author', 'edd', 'yas'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_body_index_error(self, mock_stdout, mock_input):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': 'Santiago Calatrava The Complete Works Expanded Edition', '\
Publisher': 'Rizzoli', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', '\
Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', 'Category': 'Architecture', 'Subject': '\
American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'})
        move_book_body(collection)
        expected_print = "There are 4 books in the library that contain the keyword you are looking for:\n\n"\
                         "1:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "2:\nAuthor: Eddings\nTitle: Castle of Wizardry\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "3:\nAuthor: Eddings\nTitle: Demon Lord of Karanda\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "4:\nAuthor: Eddings\nTitle: Enchanter's End Game\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n"\
                         "Invalid input: invalid literal for int() with base 10: 'yas'\n" \
                         "invalid literal for int() with base 10: 'yas' raised an error. Please follow the " \
                         "instruction carefully.\n\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['author', 'edd', '55'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_body_index_error_a_number_greater_than_length_of_list(self, mock_stdout, mock_input):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': 'Santiago Calatrava The Complete Works Expanded Edition', '\
Publisher': 'Rizzoli', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', '\
Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', 'Category': 'Architecture', 'Subject': '\
American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'})
        move_book_body(collection)
        expected_print = "There are 4 books in the library that contain the keyword you are looking for:\n\n"\
                         "1:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "2:\nAuthor: Eddings\nTitle: Castle of Wizardry\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "3:\nAuthor: Eddings\nTitle: Demon Lord of Karanda\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "4:\nAuthor: Eddings\nTitle: Enchanter's End Game\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n"\
                         "Invalid input: list index out of range\n" \
                         "list index out of range raised an error. Please follow the instruction carefully.\n\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['author', 'edd', '2', 'random shelf'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_body_value_error_invalid_book_location(self, mock_stdout, mock_input):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': 'Santiago Calatrava The Complete Works Expanded Edition', '\
Publisher': 'Rizzoli', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', '\
Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', 'Category': 'Architecture', 'Subject': '\
American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'})
        move_book_body(collection)
        expected_print = "There are 4 books in the library that contain the keyword you are looking for:\n\n"\
                         "1:\nAuthor: Eddings\nTitle: Belgarath the Sorcerer\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "2:\nAuthor: Eddings\nTitle: Castle of Wizardry\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "3:\nAuthor: Eddings\nTitle: Demon Lord of Karanda\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "4:\nAuthor: Eddings\nTitle: Enchanter's End Game\nPublisher: None\nShelf: 34\n" \
                         "Category: Fiction\nSubject: Fantasy\n\n" \
                         "You can move the book to one of these shelves:\n" \
                         "1: 6\n2: 10\n3: 12\n4: 16\n5: 17\n6: 31\n7: 34\n"\
                         "Invalid input: 'random shelf' is not a valid location\n" \
                         "'random shelf' is not a valid location raised an error. Please follow the " \
                         "instruction carefully.\n\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['wrong search tag', 'edd'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_body_type_error(self, mock_stdout, mock_input):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': 'Santiago Calatrava The Complete Works Expanded Edition', '\
Publisher': 'Rizzoli', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', '\
Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', 'Category': 'Architecture', 'Subject': '\
American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'})
        move_book_body(collection)
        expected_print = f"Invalid input: 'Wrong search tag'\n" \
                         f"'Wrong search tag' raised KeyError. Please follow the instruction carefully.\n\n"
        self.assertEqual(expected_print, mock_stdout.getvalue())
