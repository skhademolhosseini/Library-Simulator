"""
Book collection manager
Name: Sam Khademolhosseini
Student#: A01233111
Date: November 6, 2020
"""


def menu() -> str:
    """
    Identify what the users want to do.

    Ensure the user types in a number between 1 and 3 to advance. If not they will be asked to type again.

    :precondition: No precondition.
    :postcondition: Asks for user input until the input is valid.
    :return: Return user input as string.

    """
    user_choice = ""
    while user_choice not in ["1", "2", "3"]:
        user_choice = input("What do you want to do? \n"
                            "Enter 1 to search \n"
                            "Enter 2 to move a book \n"
                            "Enter 3 to save and quit")

        if user_choice == "1":
            return "search"
        elif user_choice == "2":
            return "move"
        elif user_choice == "3":
            return "quit"
        else:
            print("Invalid input, try again")


def search_info() -> tuple:
    """
    Get information regarding search from users.

    Aks the users how they want to search and what they are looking for in that section.

    :precondition: no preconditions.
    :postcondition: will ask for user input and return them as a tuple containing 2 strings.
    :return: a tuple containing information regarding search.

    """
    search_tag = input("You can search by author, title, publisher, shelf, category, and subject.\n"
                       "How do you want to search?")
    search_keyword = input("Please enter the keyword you are looking for:")

    return search_tag.capitalize(), search_keyword


def search(collection_of_books: tuple, search_tag: str, search_keyword: str) -> list:
    """
    Search for specific books inside book collection.

    Find the books that contain the search keyword in their search tag section.

    :param collection_of_books: A tuple containing all books as dictionary.
    :param search_tag: A string that represents one of the keys in a book dictionary, key must be capitalized.
    :param search_keyword: A string that we look for in values in each book dictionary.
    :precondition: Parameters must be the right type.
    :postcondition: All books that meet the conditions will be added to a list.
    :return: A list of found books.

    >>> book_collection = turn_str_into_collection(load_text_file("Testing_book.txt"))
    >>> search_tag1 = "Author"
    >>> search_keyword1 = "edd"
    >>> search(book_collection, search_tag1, search_keyword1)
    [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Castle of Wizardry', 'Publisher': 'None', 'Shelf': '\
34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Demon Lord of Karanda', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', '\
Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}]

     >>> book_collection = turn_str_into_collection(load_text_file("Testing_book.txt"))
     >>> search_tag2 = "Shelf"
     >>> search_keyword2 = "6"
     >>> search(book_collection, search_tag2, search_keyword2)
     [{'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', 'Publisher': 'Exeter', 'Shelf': '6', '\
Category': 'Architecture', 'Subject': '20th Century'}, {'Author': 'Johnson Burgee', 'Title': '\
Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}]

    """
    found_books = []

    if search_tag == "Shelf" and search_keyword.isnumeric():
        found_books = [book for book in collection_of_books if search_keyword == book["Shelf"]]

    else:
        for book in collection_of_books:
            if search_keyword.lower() in book[search_tag].lower():
                found_books.append(book)

    return found_books


def load_text_file(file_name: str) -> str:
    """
    Open a plaintext file

    :param file_name: Name of the file we want to open as string.
    :precondition: File must exist.
    :postcondition: Will return the data from the file as string.
    :return: Data as sting.

    """
    try:
        with open(file_name, encoding='windows-1251') as file_object:
            return file_object.read()
    except FileNotFoundError as err:
        print(f"{err}\n"
              f"Please make sure the file you are trying to open exists!")
        quit()


def turn_str_into_collection(collection_as_str: str) -> tuple:
    """
    Create a tuple from a string.

    :param collection_as_str: A string containing information regarding a collection.
    :precondition: First line must be the keys, and the rest must be values for those keys.\
    :postcondition: Create a tuple containing dictionaries from the information passed to function as the parameter.
    :return: The tuple created.

    >>> book_collection_as_str = load_text_file("Testing_book.txt")
    >>> turn_str_into_collection(book_collection_as_str)
    ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', '\
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

    """
    book_collection = []
    lines = collection_as_str.split("\n")

    keys_line = lines.pop(0)
    book_keys = keys_line.strip().split("\t")

    for line in lines:
        book_value = line.strip().split("\t")
        if "" in book_value:
            book_value[2] = "None"
        book_info = {book_keys[index].capitalize(): book_value[index] for index in range(len(book_keys))}
        book_collection.append(book_info)

    return tuple(book_collection)


def move_book(book_to_move: dict, new_location_of_book: str) -> None:
    """
    Move the book from one location to another.

    :param book_to_move: The book we want to move as a dictionary.
    :param new_location_of_book: Destination of the book we want to move which is a string.
    :precondition: The dictionary of the book must have Shelf key in it, and the new location must be a string.
    :postcondition: The value of the Shelf key inside book dictionary will change to the new location.
    :postcondition: Displays a meaningful sentence to tell the user the move was successful.

    >>> my_book = {'Author': 'Dupre', 'Title': 'Sky', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture'}
    >>> move_book(my_book, "6")
    The book was successfully move to the new location
    New Shelf: 6

    """
    book_to_move["Shelf"] = new_location_of_book
    print(f"The book was successfully move to the new location\n"
          f"New Shelf: {new_location_of_book}")


def get_book_by_index(collection_of_found_books: list) -> dict:
    """
    Ask user to select the number of the book they want to move between the books that have been displayed to them.

    :param collection_of_found_books: A list containing some books as dictionary.
    :precondition: Collection that is passed to the function must be a list that has dictionaries inside it.
    :postcondition: Will find the right book by index and return the dictionary representing that book.
    :return: The dictionary of the selected book.

    """
    book_number = input("Please enter the number of the book you want to move:")
    book_index = int(book_number) - 1

    return collection_of_found_books[book_index]


def valid_new_location(valid_locations: list) -> str:
    """
    Display possible locations and ask for a valid new location for the book the user wants to move.

    :param valid_locations: A list containing all possible location where a book can be.
    :precondition: The user input needs to be valid or the function will keep asking user to enter another input.
    :postcondition: Validates user input in order to find a valid new location for the book.
    :return: The new location as a string.

    """
    print("You can move the book to one of these shelves:")
    for count, shelf in enumerate(valid_locations, 1):
        print(f"{count}: {shelf}")

    new_location = input("Please enter the shelf name/number that you want to move your book to?")

    if new_location not in valid_locations:
        raise ValueError(f"'{new_location}' is not a valid location")

    return new_location


def get_all_valid_location(collection_of_books: tuple) -> list:
    """
    Find all valid location where a book can be.

    :param collection_of_books: A tuple containing all books as dictionary.
    :precondition: Value passed to the function as parameter must be the right type and format.
    :postcondition: Will create a set of all possible places where a book can be placed.
    :postcondition: Will change the set to a list in order to sort the possible locations.
    :return: A list containing all valid locations.

     >>> book_collection = turn_str_into_collection(load_text_file("Testing_book.txt"))
     >>> get_all_valid_location(book_collection)
     ['6', '10', '12', '16', '17', '31', '34']

    """
    possible_locations = set()
    for book in collection_of_books:
        possible_locations.add(book["Shelf"])

    number_list = []
    alpha_list = []
    for shelf in possible_locations:
        if shelf.isnumeric():
            number_list.append(int(shelf))

        if shelf.isalpha():
            alpha_list.append(shelf)

    sorted_possible_locations = []
    for number in sorted(number_list):
        sorted_possible_locations.append(str(number))
    for alpha in sorted(alpha_list):
        sorted_possible_locations.append(alpha)

    return sorted_possible_locations


def save_books(collection_of_books_as_str: str, file_name: str) -> None:
    """
    Save all the changes to the plaintext file.

    :param collection_of_books_as_str: A string containing information of all books. Each book in a single line.
    :param file_name: Complete name of the file that we want to open as string.
    :precondition: The function is not responsible if the formatting of the string passed to it is wrong.
    :postcondition: Saves all the changes into the plaintext file.

    """
    with open(file_name, "w", encoding='windows-1251') as save_file:
        save_file.write(collection_of_books_as_str)

    print("All the changes were successfully saved.\n"
          "Thanks for choosing us! Hope to see you again.")


def turn_collection_into_str(collection_of_books: tuple) -> str:
    """
    Create a string from the information saves in dictionaries.

    :param collection_of_books: A tuple containing all books as dictionary.
    :precondition: The book collection passed to the function must be a tuple that has each book as a dictionary.
    :postcondition: Will turn the dictionaries of the books into string with the right format.
    :return: The string created.

    >>> book_collection = turn_str_into_collection(load_text_file("Testing_book.txt"))
    >>> turn_collection_into_str(book_collection)
    "Author\\tTitle\\tPublisher\\tShelf\\tCategory\\tSubject\\nDupre\\tSkyscrapers\\tBD&L\\t12\\tArchitecture\\t\
20th Century\\nHollingsworth\\tArchitecture of the 20th Century\\tExeter\\t6\\tArchitecture\\t20th Century\\n\
Johnson Burgee\\tArchitecture 1979-1985\\tRizzoli\\t6\\tArchitecture\\t20th Century\\nTzonis\\t\
Santiago Calatrava The Complete Works Expanded Edition\\tRizzoli\\t12\\tArchitecture\\t20th Century\\nBreeze\\t\
L. A. Deco\\tRizzoli\\t16\\tArchitecture\\tAmerican Architecture\\nBrownlee\\t\
Making a Moden Classic The Architecture of the Philadelphia Museum of Art\\tPhiladelphia Museum of Art\\t10\\t\
Architecture\\tAmerican Architecture\\nEditoriale Domus\\tEmpire State Building Kit\\tEditoriale Domus\\t31\\t\
Architecture\\tAmerican Architecture\\nGebhard and Winter\\tLos Angeles An Architecture Guide\\tGibbs Smith\\t\
17\\tArchitecture\\tAmerican Architecture\\nGebhard and Zimmerman\\t\
The California Architecture of Frank Lloyd Wright\\tChronicle Books\\t31\\tArchitecture\\tAmerican Architecture\\n\
Eddings\\tBelgarath the Sorcerer\\t\\t34\\tFiction\\tFantasy\\nEddings\\tCastle of Wizardry\\t\\t34\\tFiction\\t\
Fantasy\\nEddings\\tDemon Lord of Karanda\\t\\t34\\tFiction\\tFantasy\\nEddings\\tEnchanter's End Game\\t\\t34\\t\
Fiction\\tFantasy"

    """
    book_str_list = []
    keys_list = list(collection_of_books[0].keys())
    keys_line = "\t".join(keys_list)
    book_str_list.append(keys_line)

    for book_index in range(len(collection_of_books)):
        value_list = list(collection_of_books[book_index].values())
        if "None" in value_list:
            value_list[2] = ""
        each_book_as_str = "\t".join(value_list)
        book_str_list.append(each_book_as_str)

    collection_of_books_as_str = "\n".join(book_str_list)

    return collection_of_books_as_str


def print_as_ordered_list(collection_of_found_books: list) -> None:
    """
    Print all the books in the book collection in format of an ordered list.

    :param collection_of_found_books: A list containing all books as dictionary.
    :precondition: The list passed to the function must contain dictionaries of the books we want to display in the
                    right format.
    :postcondition: Displays all the books in format of an ordered list.

    >>> book_collection = search(turn_str_into_collection(load_text_file("Testing_book.txt")), "Author", "edd")
    >>> print_as_ordered_list(book_collection)
    There are 4 books in the library that contain the keyword you are looking for:
    <BLANKLINE>
    1:
    Author: Eddings
    Title: Belgarath the Sorcerer
    Publisher: None
    Shelf: 34
    Category: Fiction
    Subject: Fantasy
    <BLANKLINE>
    2:
    Author: Eddings
    Title: Castle of Wizardry
    Publisher: None
    Shelf: 34
    Category: Fiction
    Subject: Fantasy
    <BLANKLINE>
    3:
    Author: Eddings
    Title: Demon Lord of Karanda
    Publisher: None
    Shelf: 34
    Category: Fiction
    Subject: Fantasy
    <BLANKLINE>
    4:
    Author: Eddings
    Title: Enchanter's End Game
    Publisher: None
    Shelf: 34
    Category: Fiction
    Subject: Fantasy
    <BLANKLINE>

    """
    number_of_books = len(collection_of_found_books)
    print(f"There are {number_of_books} books in the library that contain the keyword you are looking for:\n")

    for count, item in enumerate(collection_of_found_books, 1):
        print(f"{count}:")
        print(f"Author: {item['Author']}")
        print(f"Title: {item['Title']}")
        print(f"Publisher: {item['Publisher']}")
        print(f"Shelf: {item['Shelf']}")
        print(f"Category: {item['Category']}")
        print(f"Subject: {item['Subject']}\n")


def search_books_body(collection_of_books: tuple) -> list:
    """
    Invoke the right function to search for a book.

    :param collection_of_books: A tuple containing all books as dictionary.
    :precondition: The collection of books must be the right type and have books as dictionaries in it.
    :postcondition: Will call the right functions in order to search for a book.

    """
    search_tag, search_keyword = search_info()
    try:
        found_books = search(collection_of_books, search_tag, search_keyword)
    except KeyError as err:
        print(f"Invalid input: {err}\n"
              f"{err} raised KeyError. Please follow the instruction carefully.\n")
    else:
        print_as_ordered_list(found_books)

        return found_books


def move_book_body(collection_of_books: tuple) -> None:
    """
    Invoke the right function to move a book.

    :param collection_of_books: A tuple containing all books as dictionary.
    :precondition: The collection of books must be the right type and have books as dictionaries in it.
    :postcondition: Will call the right functions in order to move a book.

    """
    found_books = search_books_body(collection_of_books)

    try:
        if len(found_books) > 0:
            selected_book = get_book_by_index(found_books)
            valid_locations = get_all_valid_location(collection_of_books)
            new_location = valid_new_location(valid_locations)
            move_book(selected_book, new_location)

    except (IndexError, ValueError) as err:
        print(f"Invalid input: {err}\n"
              f"{err} raised an error. Please follow the instruction carefully.\n")

    except TypeError:
        pass


def save_book_body(collection_of_books: tuple, file_name: str) -> None:
    """
    Invoke the right functions to save the changes to the file.

    :param collection_of_books: A tuple containing all books as dictionary.
    :param file_name: Complete name of the file that we want to open as string.
    :precondition: The collection of books must be the right type and have books as dictionaries in it.
    :postcondition: Will call the right functions in order to save all changes to the file.

    """
    book_collection_as_str = turn_collection_into_str(collection_of_books)
    save_books(book_collection_as_str, file_name)


def books():
    """
    Runs the code for a digital library.

    Allows the user to open a plaintext file containing the information of many books and search for a book or
    move a book from one shelf to another, and at the end save the changes to the file.

    """
    file_to_edit = input("Please enter the name of the file you want to open:")
    book_collection_str = load_text_file(file_to_edit)
    book_collection = turn_str_into_collection(book_collection_str)
    still_running = True
    while still_running:
        menu_result = menu()

        if menu_result == "search":
            search_books_body(book_collection)

        elif menu_result == "move":
            move_book_body(book_collection)

        elif menu_result == "quit":
            save_book_body(book_collection, file_to_edit)
            still_running = False


def main():
    """
    Drives the program.
    """
    books()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
