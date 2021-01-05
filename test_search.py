from unittest import TestCase

from books import search


class TestSearch(TestCase):

    def test_search_in_random_collection_keyword_lower_case_partial_info(self):
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
        actual = (search(collection, "Author", "edd"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_keyword_upper_case_partial_info(self):
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
        actual = (search(collection, "Author", "EDD"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_keyword_mixed_case_partial_info(self):
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
        actual = (search(collection, "Author", "EdDi"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_keyword_mixed_case_complete_name(self):
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
        actual = (search(collection, "Author", "Eddings"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_author(self):
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
        actual = (search(collection, "Author", "Dupre"))
        expected = [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_title(self):
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
        actual = (search(collection, "Title", "Skys"))
        expected = [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_publisher_have_publisher_value(self):
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
        actual = (search(collection, "Publisher", "&"))
        expected = [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_publisher_for_books_with_no_publisher(self):
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
        actual = (search(collection, "Publisher", "None"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_shelf_for_a_numeric_value(self):
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
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': 'Noguchi', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': 'Noguchi', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'\
Author': 'Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', '\
Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'})
        actual = (search(collection, "Shelf", "6"))
        expected = [{'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', 'Publisher': '\
Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Johnson Burgee', '\
Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', '\
Subject': '20th Century'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_shelf_for_a_numeric_value_shelves_are_1_11_111_1111_11111(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '1', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
Publisher': 'Exeter', 'Shelf': '11', 'Category': 'Architecture', 'Subject': '20th Century'}, {'Author': '\
Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '111', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Tzonis', 'Title': '\
Santiago Calatrava The Complete Works Expanded Edition', 'Publisher': 'Rizzoli', 'Shelf': '1111', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Breeze', 'Title': 'L. A. Deco', 'Publisher': '\
Rizzoli', 'Shelf': '11111', 'Category': 'Architecture', 'Subject': 'American Architecture'})
        actual = (search(collection, "Shelf", "111"))
        expected = [{'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', '\
Shelf': '111', 'Category': 'Architecture', 'Subject': '20th Century'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_shelf_for_an_alphabetical_value(self):
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
Noguchi', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': 'Noguchi', 'Category': 'Fiction', '\
Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'})
        actual = (search(collection, "Shelf", "Noguchi"))
        expected = [{'Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': '\
Editoriale Domus', 'Shelf': 'Noguchi', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': 'Noguchi', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_category(self):
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
        actual = (search(collection, "Category", "Fiction"))
        expected = [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}]
        self.assertEqual(expected, actual)

    def test_search_in_random_collection_by_subject_and_value_contains_space(self):
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
        actual = (search(collection, "Subject", "ican Arch"))
        expected = [{'Author': 'Breeze', 'Title': 'L. A. Deco', 'Publisher': 'Rizzoli', 'Shelf': '16', '\
Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Brownlee', 'Title': '\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art', 'Publisher': '\
Philadelphia Museum of Art', 'Shelf': '10', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'\
Author': 'Editoriale Domus', 'Title': 'Empire State Building Kit', 'Publisher': 'Editoriale Domus', 'Shelf': '\
31', 'Category': 'Architecture', 'Subject': 'American Architecture'}, {'Author': 'Gebhard and Winter', 'Title': '\
Los Angeles An Architecture Guide', 'Publisher': 'Gibbs Smith', 'Shelf': '17', 'Category': 'Architecture', '\
Subject': 'American Architecture'}, {'Author': 'Gebhard and Zimmerman', 'Title': '\
The California Architecture of Frank Lloyd Wright', 'Publisher': 'Chronicle Books', 'Shelf': '31', 'Category': '\
Architecture', 'Subject': 'American Architecture'}]
        self.assertEqual(expected, actual)
