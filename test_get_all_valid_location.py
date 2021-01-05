from unittest import TestCase

from books import get_all_valid_location


class TestGetAllValidLocation(TestCase):

    def test_get_all_valid_location_a_collection_with_multiple_books_that_some_have_same_shelf_value(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': 'Santiago Calatrava The Complete Works Expanded Edition', '\
Publisher': 'Rizzoli', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', '\
Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', 'Category': 'Architecture', 'Subject': '\
American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': 'Noguchi', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': 'Reading', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': 'Reading', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'\
Author': 'Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', '\
Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'})
        actual = get_all_valid_location(collection)
        expected = ['6', '10', '12', '16', '31', '34', 'Noguchi', 'Reading']
        self.assertEqual(expected, actual)

    def test_get_all_valid_location_a_collection_with_multiple_books_that_all_have_same_shelf_value(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': '\
Santiago Calatrava The Complete Works Expanded Edition', 'Publisher': 'Rizzoli', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', 'Title': 'L. A. Deco', 'Publisher': 'Rizzoli', '\
Shelf': '12', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '12', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
12', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '12', 'Category': 'Architecture', '\
Subject': 'American Architecture'})
        actual = get_all_valid_location(collection)
        expected = ['12']
        self.assertEqual(expected, actual)

    def test_get_all_valid_location_a_collection_with_multiple_books_that_non_have_same_shelf_value(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '10', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': '\
Santiago Calatrava The Complete Works Expanded Edition', 'Publisher': 'Rizzoli', 'Shelf': '1', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', 'Title': 'L. A. Deco', 'Publisher': 'Rizzoli', '\
Shelf': '20', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '22', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
Reading', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '31', 'Category': 'Architecture', '\
Subject': 'American Architecture'})
        actual = get_all_valid_location(collection)
        expected = ['1', '10', '12', '20', '22', '31', 'Noguchi', 'Reading']
        self.assertEqual(expected, actual)

    def test_get_all_valid_location_a_collection_with_multiple_books_shelf_value_is_only_letters(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': 'Reading', '\
Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': '\
Architecture of the 20th Century', 'Publisher': 'Exeter', 'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': '\
20th Century'}, {'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '\
Reading', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': '\
Santiago Calatrava The Complete Works Expanded Edition', 'Publisher': 'Rizzoli', 'Shelf': 'Noguchi', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', 'Title': 'L. A. Deco', 'Publisher': '\
Rizzoli', 'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': '\
Brownlee', 'Title': 'Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': 'Gaby', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
Noguchi', 'Category': 'Architecture', 'Subject': 'American Architecture'})
        actual = get_all_valid_location(collection)
        expected = ['Gaby', 'Noguchi', 'Reading']
        self.assertEqual(expected, actual)

    def test_get_all_valid_location_a_collection_with_multiple_books_shelf_value_is_only_numbers(self):
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
        actual = get_all_valid_location(collection)
        expected = ['6', '10', '12', '16', '17', '31', '34']
        self.assertEqual(expected, actual)

    def test_get_all_valid_location_a_collection_with_one_book(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'},)
        actual = get_all_valid_location(collection)
        expected = ['12']
        self.assertEqual(expected, actual)
