from unittest import TestCase

from books import turn_collection_into_str


class TestTurnCollectionIntoStr(TestCase):

    def test_turn_collection_into_str_a_book_collections_with_random_books(self):
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
        actual = turn_collection_into_str(collection)
        expected = "Author	Title	Publisher	Shelf	Category	Subject\n" \
                   "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century\n" \
                   "Hollingsworth	Architecture of the 20th Century	Exeter	6	Architecture	20th Century\n" \
                   "Johnson Burgee	Architecture 1979-1985	Rizzoli	6	Architecture	20th Century\n" \
                   "Tzonis	Santiago Calatrava The Complete Works Expanded Edition	Rizzoli	12	Architecture" \
                   "	20th Century\n" \
                   "Breeze	L. A. Deco	Rizzoli	16	Architecture	American Architecture\n" \
                   "Brownlee	Making a Moden Classic The Architecture of the Philadelphia Museum of Art" \
                   "	Philadelphia Museum of Art	10	Architecture	American Architecture\n" \
                   "Editoriale Domus	Empire State Building Kit	Editoriale Domus	31	Architecture" \
                   "	American Architecture\n" \
                   "Gebhard and Winter	Los Angeles An Architecture Guide	Gibbs Smith	17	Architecture" \
                   "	American Architecture\n" \
                   "Gebhard and Zimmerman	The California Architecture of Frank Lloyd Wright	Chronicle Books" \
                   "	31	Architecture	American Architecture\n" \
                   "Eddings	Belgarath the Sorcerer		34	Fiction	Fantasy\n" \
                   "Eddings	Castle of Wizardry		34	Fiction	Fantasy\n" \
                   "Eddings	Demon Lord of Karanda		34	Fiction	Fantasy\n" \
                   "Eddings	Enchanter's End Game		34	Fiction	Fantasy"
        self.assertEqual(expected, actual)

    def test_turn_collection_into_str_a_book_collections_with_same_books(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', '\
Shelf': '12', 'Category': 'Architecture', 'Subject': '20th Century'})
        actual = turn_collection_into_str(collection)
        expected = "Author	Title	Publisher	Shelf	Category	Subject\n" \
                   "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century\n" \
                   "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century"
        self.assertEqual(expected, actual)

    def test_turn_collection_into_str_a_book_collections_that_books_dont_have_publisher_key(self):
        collection = ({'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'})
        actual = turn_collection_into_str(collection)
        expected = "Author	Title	Publisher	Shelf	Category	Subject\n" \
                   "Eddings	Belgarath the Sorcerer		34	Fiction	Fantasy\n" \
                   "Eddings	Castle of Wizardry		34	Fiction	Fantasy\n" \
                   "Eddings	Demon Lord of Karanda		34	Fiction	Fantasy\n" \
                   "Eddings	Enchanter's End Game		34	Fiction	Fantasy"
        self.assertEqual(expected, actual)

    def test_turn_collection_into_str_book_collections_that_first_book_doesnt_have_publisher_key_second_book_has(self):
        collection = ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': '\
Architecture', 'Subject': '20th Century'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': '\
None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'})
        actual = turn_collection_into_str(collection)
        expected = "Author	Title	Publisher	Shelf	Category	Subject\n" \
                   "Dupre	Skyscrapers	BD&L	12	Architecture	20th Century\n" \
                   "Eddings	Enchanter's End Game		34	Fiction	Fantasy"
        self.assertEqual(expected, actual)
