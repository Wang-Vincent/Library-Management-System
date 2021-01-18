"""
Book collection manager.
Author: Vincent Wang
Student #: A01208123
Date: November 6, 2020
"""
from typing import List
from textwrap import fill


def load_data():
    """load book list from text file and convert them in to a list of dictionaries.

    for each line in the book list return them as dictionaries describing information of each book in the book list.

    :precondition: each field of the book must be strings separated by tabs, and each line must contains fields of only\
     one book
    :postcondition: return dictionaries describing information of each book in the book list.
    :return: list of dictionaries representing the book list
    """
    # filename = input("Please enter the load file name of the tab-separated book list: ")
    # user input disabled for filename for test purpose

    filename = "books.txt"

    with open(filename, encoding='utf-16') as file_object:
        fields = file_object.readline().strip()
        field_list = fields.split('\t')
        raw_collection: List[List[str]] = []
        book_list = []
        for line in file_object:
            book_line = line.strip().split('\t')
            raw_collection.append(book_line)

        for book in raw_collection:
            book_dict = {field_list[i]: book[i] for i in range(len(book))}
            book_list.append(book_dict)

    return book_list


def books():
    """convert the list of dictionaries into a tuple and replace all empty string with 'n/a' to represent missing info.

    :precondition: the load_data() must return a list of dictionaries
    :postcondition: convert the list of dictionaries into a tuple representing a collection of book.
    :return: a tuple of dictionaries representing a collection of book
    """
    collection = tuple(load_data())
    for book in collection:
        for field in book:
            if book[field] == '':
                book[field] = 'n/a'
    return collection


def menu(book_collection):
    """prompt user to to choose a number to input representing their command from the printed menu.

    By entering user can choose from what field they want to search by or if they want to move books or quit.

    :param book_collection: a tuple of dictionaries
    :precondition: no precondition, can always execute
    :postcondition: corresponding function will invoke base on user's input
    :return: none
    """
    while True:
        print_menu_options()

        try:
            menu_selection = int(input("\nPlease choose one of the following options above: "))
            if menu_selection in range(1, 6 + 1):
                search_handler(menu_selection, book_collection)
            elif menu_selection == 7:
                move_handler(book_collection)
            elif menu_selection == 0:
                quit_books(book_collection)

        except (TypeError, ValueError):
            print("Invalid input. Please enter again!")


def print_menu_options():
    """print the menu.

    :precondition: no precondition, can always execute
    :postcondition: no postcondition.
    :return: none

    >>> print_menu_options()
    <BLANKLINE>
    ------------------------------BOOKS MANAGEMENT SYSTEM------------------------------
    <BLANKLINE>
    1: Search Book by Author
    2: Search Book by Title
    3: Search Book by Publisher
    4: Search Book by Shelf/Location
    5: Search Book by Category
    6: Search Book by Subject
    7: Move Book
    0: Save & Quit
    <BLANKLINE>
    SEARCH GUIDANCE:
    A. If you want to search for the books that have no information in certain field (e.g. Publisher)
    please enter "N/A" into the search keyword when it prompt.
    B. If you want to search by numbered shelf, please enter the exact number of that shelf into the
    search keyword when it prompt.
    """
    print("\n------------------------------BOOKS MANAGEMENT SYSTEM------------------------------\n")
    print("1: Search Book by Author\n2: Search Book by Title\n3: Search Book by Publisher\n4: Search Book by "
          "Shelf/Location\n5: Search Book by Category\n6: Search Book by Subject\n7: Move Book\n0: Save & Quit\n")
    print("SEARCH GUIDANCE:")
    print(fill('A. If you want to search for the books that have no information in certain field (e.g. Publisher) '
               'please enter "N/A" into the search keyword when it prompt.', 100))
    print(fill('B. If you want to search by numbered shelf, please enter the exact number of that shelf into the search'
               ' keyword when it prompt.', 100))


def back_or_quit(book_collection):
    """Ask user if they want to back to menu or save and quit. Take param to save file if user choose to save and quit.

    :param book_collection: a tuple of dictionaries
    :precondition: user_choice must be 9 or 0.
    :postcondition: base on user's choice, invoke either the back to menu or save and quit function.
    :return: None

    """
    user_choice = int(input(fill("If you want to return to the main menu, please enter 9, if you want to save & quit, "
                                 "please enter 0: ", 100)))
    if user_choice == 9:
        return
    elif user_choice == 0:
        quit_books(book_collection)


def search_handler(menu_selection: int, book_collection):
    """Take a integer as the 1st param to represent user choice of fields to search and pass it to the function that
    execute the search.

    after the search is completed, prompt user to back to main menu or save and quit. Take book_collection as second
    param to pass it to back or quit function since it need to be used to save file.

    :param menu_selection: an integer
    :param book_collection: a tuple of dictionaries
    :precondition: the number must be in the range (1, 6+1)
    :postcondition: invoke search_actions function
    :return: none
    """
    search_actions(menu_selection, book_collection)
    back_or_quit(book_collection)

    return


def search_actions(menu_selection: int, book_collection):
    """take an integer as 1st param to represent user choice of fields to search, search it in the collection of 2nd
    param and print result.

    :param menu_selection: an integer
    :param book_collection: a tuple of dictionaries
    :precondition: menu_selection must be an integer in the range(1,6+1) and keyword must be a string
    :postcondition: return and print a list of deep-copied dictionaries that represents books.
    :return: a enumerated list of dictionaries that represents search result of the books after its formatted at
    print_result()
    """
    keyword = input("please enter the search keyword: ")
    result_list = search_action_logic(book_collection, keyword, menu_selection)

    if len(result_list) != 0:
        enumerated_result = print_result(result_list)
        print("Voila! Here is your search result. ")
        return enumerated_result
    else:
        print("Apologies(in Spencer's tone), Your search did not match any book in the collection. ")
        return


def search_action_logic(book_collection, keyword, menu_selection):
    """Base on choices of fields to search by, search keyword, loop keyword in the book collection to find matches.

    if search by shelf, the function will check if its number, if it is, return results at the exact match numbered
    shelf only.

    :param book_collection: a tuple of dictionaries
    :param keyword: a string
    :param menu_selection: an integer
    :precondition: menu_selection must be an integer in the range(1,6+1) and keyword must be a string
    :postcondition: return and print a list of deep-copied dictionaries that represents books.
    :return: a list of deep-copied dictionaries that represents books

    >>> bc = books()
    >>> search_action_logic(bc, "abrams", 1)
    [{'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson', 'Shelf': \
'18', 'Category': 'Fiction', 'Subject': 'SF'}, {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number \
12', 'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'}, {'Author': 'Abramson', 'Title': \
'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': \
'SF'}, {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace', 'Shelf': '2', \
'Category': 'Language', 'Subject': 'English'}]

    >>> bc = books()
    >>> search_action_logic(bc, "THE STARS", 2)
    [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', 'Category': 'Fiction', \
'Subject': 'SF'}, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11', 'Category': \
'Fiction', 'Subject': 'SF'}]

    >>> bc = books()
    >>> search_action_logic(bc, "1", 4)
    [{'Author': 'Ambroziak', 'Title': 'Michael Graves Images of a Grand Tour', 'Publisher': 'Princeton Architectural \
Press', 'Shelf': '1', 'Category': 'Architecture', 'Subject': 'Architectural History'}, {'Author': 'Lambert', 'Title': \
'Building Seagram', 'Publisher': 'Yale', 'Shelf': '1', 'Category': 'Architecture', 'Subject': 'Architectural \
History'}, {'Author': 'Gustafson', 'Title': 'Craft Perception and Practice 1', 'Publisher': 'Ronsdale Press', 'Shelf': \
'1', 'Category': 'Art', 'Subject': 'Craft'}, {'Author': 'Gustafson', 'Title': 'Craft Perception and Practice 2', \
'Publisher': 'Ronsdale Press', 'Shelf': '1', 'Category': 'Art', 'Subject': 'Craft'}, {'Author': 'Mather', 'Title': \
'Cyberstorm', 'Publisher': 'Harper Collins', 'Shelf': '1', 'Category': 'Fiction', 'Subject': 'SF'}, {'Author': \
'Davis', 'Title': 'History of Vancouver', 'Publisher': 'Harbour', 'Shelf': '1', 'Category': 'History', 'Subject': \
'Vancouver'}, {'Author': 'McConnell', 'Title': 'Vive le francais 7', 'Publisher': 'Addison Wesley', 'Shelf': '1', \
'Category': 'Language', 'Subject': 'French'}, {'Author': 'Stempek', 'Title': 'Polski Krok Po Kroku 2', 'Publisher': \
'Glossa', 'Shelf': '1', 'Category': 'Language', 'Subject': 'Polish'}, {'Author': 'Campbell', 'Title': 'Calculus and \
Analytic Geometry 2e', 'Publisher': '"Prindle, Weber & Schmidt"', 'Shelf': '1', 'Category': 'Mathematics', 'Subject': \
'Calculus'}, {'Author': 'Hurley', 'Title': 'Intermediate Calculus', 'Publisher': 'Saunders College', 'Shelf': '1', \
'Category': 'Mathematics', 'Subject': 'Calculus'}, {'Author': 'Repka', 'Title': 'Calculus with Analytic Geometry', \
'Publisher': 'WCB', 'Shelf': '1', 'Category': 'Mathematics', 'Subject': 'Calculus'}, {'Author': 'Pogorelov', 'Title': \
'Differential Geometry', 'Publisher': 'Noordhoff', 'Shelf': '1', 'Category': 'Mathematics', 'Subject': 'Differential \
Geometry'}, {'Author': 'Epp', 'Title': 'Discrete Mathematics With Applications 3e', 'Publisher': 'Brooks/Cole', \
'Shelf': '1', 'Category': 'Mathematics', 'Subject': 'Discrete Math'}, {'Author': 'Epp', 'Title': 'Solutions Manual \
for Discrete Mathematics With Applications 3e', 'Publisher': 'Brooks/Cole', 'Shelf': '1', 'Category': 'Mathematics', \
'Subject': 'Discrete Math'}, {'Author': 'Grimaldi', 'Title': 'Discrete and Combinatorial Mathematics', 'Publisher': \
'Pearson', 'Shelf': '1', 'Category': 'Mathematics', 'Subject': 'Discrete Math'}, {'Author': 'Liu', 'Title': 'Elements \
of Discrete Mathematics', 'Publisher': 'McGraw Hill', 'Shelf': '1', 'Category': 'Mathematics', 'Subject': 'Discrete \
Math'}, {'Author': 'Ashley', 'Title': 'ANS Cobol 2e', 'Publisher': 'Wiley', 'Shelf': '1', 'Category': 'Programming', \
'Subject': 'Cobol'}, {'Author': 'Brown', 'Title': 'Advanced ANS Cobol with Structured Programming', 'Publisher': \
'Wiley', 'Shelf': '1', 'Category': 'Programming', 'Subject': 'Cobol'}, {'Author': 'Bunt', 'Title': 'Structured \
Fortran', 'Publisher': 'McGraw Hill', 'Shelf': '1', 'Category': 'Programming', 'Subject': 'Fortran'}, {'Author': \
'Krishnamurthi', 'Title': 'Programming Languages', 'Publisher': 'Brown', 'Shelf': '1', 'Category': 'Programming', \
'Subject': 'Programming'}, {'Author': 'Lin', 'Title': 'Principles of Parallel Programming', 'Publisher': 'Pearson', \
'Shelf': '1', 'Category': 'Programming', 'Subject': 'Programming'}]


    """
    fields = [field for book in book_collection for field in book]
    result_list = []
    for book in book_collection:
        if keyword.isdigit() and menu_selection == 4:
            if book.get(fields[menu_selection - 1]).isdigit() and int(keyword) == int(book.get(fields[menu_selection -
                                                                                                      1])):
                result_list.append(book)
        elif keyword.lower() in book.get(fields[menu_selection - 1]).lower().strip():
            result_list.append(book)
    return result_list


def print_result(result_list: list):
    """enumerate and print the resulted list in a good readability style.

    :param result_list: a list of dictionaries
    :precondition: result_list must a list of dictionaries
    :postcondition: return an enumerated list
    :return: an enumerated list

    >>> rl = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', \
'Shelf': '11', 'Category': 'Fiction', 'Subject': 'SF'}]
    >>> print_result(rl)
    --------------------------------------------------
    Result #1
    Author: Asimov
    Title: "The Stars, Like Dust"
    Publisher: n/a
    Shelf: 38
    Category: Fiction
    Subject: SF
    --------------------------------------------------
    Result #2
    Author: Norton
    Title: Postmarked the Stars
    Publisher: Ace
    Shelf: 11
    Category: Fiction
    Subject: SF
    [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', 'Category': \
'Fiction', 'Subject': 'SF'}), (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', \
'Shelf': '11', 'Category': 'Fiction', 'Subject': 'SF'})]

    >>> rl = [{'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}]
    >>> print_result(rl)
    --------------------------------------------------
    Result #1
    Author: Asimov
    Title: "The Currents of Space"
    Publisher: n/a
    Shelf: 38
    Category: Fiction
    Subject: SF
    [(1, {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38', 'Category': \
'Fiction', 'Subject': 'SF'})]
    """
    numbered_list = list(enumerate(result_list, 1))
    for numbered in numbered_list:
        print(f'--------------------------------------------------\nResult #{numbered[0]}')
        for field in numbered[1]:
            print(f'{field}: {numbered[1].get(field)}')

    return numbered_list


def move_handler(book_collection):
    """
    Change shelf-location of a book by choosing it from the search result and entering a valid destined location.

    :param book_collection: a tuple of dictionaries
    :precondition: book_collection must be a tuple of dictionaries
    :postcondition: the shelf-location of the selected book will be updated
    :return: none

    """
    print("1: Search book by Author \n2: Search book by Title \n3: Search book by Publisher \n4: Search book by "
          "Shelf/Location \n5: Search book by Category \n6: Search book by Subject \n")
    field_selection = int(input(fill("In order to move a book, you need to find it first. What field  of the book do "
                                     "you what to search by? Please choose from the above options: ", 100)))

    result_list = search_actions(field_selection, book_collection)
    if result_list:
        move_selection = input(fill("Please select the book you want to move from the above search results. If you "
                                    "cannot find the book you want to move from the list above, please enter 'R' "
                                    "to return to main menu: ", 100))
        if move_selection.upper() == "R":
            return

        else:
            print('------------------------------------------------------------')
            selected_book = select_book(result_list, move_selection)
            if selected_book:
                print_valid_location(get_valid_locations(book_collection))
                new_location = input(fill("Here are all the locations you can move the selected book to. If you want to"
                                          " move the book to a numbered shelf, enter the exact number of that shelf. "
                                          "Otherwise, please enter the exact name of that named location ", 100))
                move_actions(selected_book, new_location, book_collection)
                back_or_quit(book_collection)

            elif not selected_book:
                back_or_quit(book_collection)

    else:
        back_or_quit(book_collection)

    return


def select_book(result_list: list, move_selection: str):
    """
    take the selection input and the enumerated search result list as params, return the selected book as a dictionary

    after the book is selected in select_book_logic, prompt the user to confirm and proceed.

    :param move_selection: a integer that represent user selection
    :param result_list: a enumerated list that represents search results
    :precondition: user must choose one of the number in the result list.
    :postcondition: return one dictionary that represents a selected book from select_book_logic, which can be pass to
    move action.
    :return: a dictionary that represents a selected book
    """
    selected_book = select_book_logic(move_selection, result_list)

    confirmation = input("Is this the book you want to move? (Y/N)")
    if confirmation.upper() == "Y":
        return selected_book
    elif confirmation.upper() == "N":
        print("Apology if this is not the book you want to move. ")
        return


def select_book_logic(move_selection, result_list):
    """
    matches user selection input and the enumerated list, print and return the dictionary that represents selected book.

    :param result_list: a enumerated list that represents search results
    :param move_selection: a integer that represent user selection
    :precondition: user must choose one of the number in the result list.
    :postcondition: return one dictionary that represents a selected book
    :return: a dictionary that represents a selected book

    >>> rl = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}), (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace',\
 'Shelf': '11', 'Category': 'Fiction', 'Subject': 'SF'})]
    >>> select_book_logic(2, rl)
    Author: Norton
    Title: Postmarked the Stars
    Publisher: Ace
    Shelf: 11
    Category: Fiction
    Subject: SF
    {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11', 'Category': 'Fiction', \
'Subject': 'SF'}

    >>> rl = [(1, {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'})]
    >>> select_book_logic(1, rl)
    Author: Asimov
    Title: "The Currents of Space"
    Publisher: n/a
    Shelf: 38
    Category: Fiction
    Subject: SF
    {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38', 'Category': \
'Fiction', 'Subject': 'SF'}

    """
    selected_book = {}

    for numbered in result_list:
        for _ in numbered:
            if numbered[0] == int(move_selection):
                selected_book = numbered[1]
    for field in selected_book:
        print(f'{field}: {selected_book.get(field)}')
    return selected_book


def move_actions(selected_book: dict, new_location: str, book_collection):
    """
    perform a move actions of the selected book.

    print a list of valid location for user to choose from, after user enter their choice, print updated information
    of that book and notify user that the book was just moved.

    :param selected_book: a dictionary
    :param book_collection: a tuple of dictionaries
    :param new_location: a string, must matched with the set generated by get_valid_location
    :precondition: new_location must be a valid location
    :postcondition: the shelf-location of the selected book will be updated
    :return: none

    >>> bc = books()
    >>> sb = {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}
    >>> move_actions(sb, "ISLAND", bc)
    <BLANKLINE>
    ----------Your Book Has Successfully Moved!----------
    Author: Asimov
    Title: "The Stars, Like Dust"
    Publisher: n/a
    Shelf: Island
    Category: Fiction
    Subject: SF
    ----------Your Book Has Successfully Moved!----------
    <BLANKLINE>

    >>> bc = books()
    >>> sb= {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}
    >>> move_actions(sb, "lego", bc)
    <BLANKLINE>
    ----------Your Book Has Successfully Moved!----------
    Author: Asimov
    Title: "The Stars, Like Dust"
    Publisher: n/a
    Shelf: Lego
    Category: Fiction
    Subject: SF
    ----------Your Book Has Successfully Moved!----------
    <BLANKLINE>

    >>> bc = books()
    >>> sb = {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38', \
'Category': 'Fiction', 'Subject': 'SF'}
    >>> move_actions(sb, "1", bc)
    <BLANKLINE>
    ----------Your Book Has Successfully Moved!----------
    Author: Asimov
    Title: "The Stars, Like Dust"
    Publisher: n/a
    Shelf: 1
    Category: Fiction
    Subject: SF
    ----------Your Book Has Successfully Moved!----------
    <BLANKLINE>
    """
    valid_location = [location.lower().strip() for location in get_valid_locations(book_collection)]

    if new_location.lower().strip() in valid_location:
        print("\n----------Your Book Has Successfully Moved!----------")
        for _ in selected_book:
            selected_book["Shelf"] = new_location.capitalize()
        for field in selected_book:
            print(f'{field}: {selected_book.get(field)}')
        print("----------Your Book Has Successfully Moved!----------\n")
    elif new_location.lower().strip() not in valid_location:
        print("Sorry, you did not entered a valid location. I can not move the book over there.")
        back_or_quit(book_collection)


def get_valid_locations(book_collection):
    """
    loop through collection, add all shelf-location to set, sort and return a list of these locations.

    the location printout will be sorted in alphabetical order and numeric order.

    :param book_collection: a tuple of dictionaries
    :precondition: no precondition, the function will always execute
    :postcondition: return and print a list of strings that represents valid shelf entries
    :return: a list of strings that represents valid shelf entries

    >>> bc = books()
    >>> get_valid_locations(bc)
    ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', \
'27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8', '9', 'Gaby', \
'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
    """
    locations_list = sorted(set(book["Shelf"] for book in book_collection for _ in book))
    return locations_list


def print_valid_location(locations_list):
    """
    print the valid locations.

    :param locations_list: a list
    :precondition: locations_list must be a list
    :postcondition: print out the list with good readability.
    :return: none

    >>> ll = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', \
    '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8', \
    '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
    >>> print_valid_location(ll)
    ---------- Valid Locations ----------
    Gaby
    Island
    Lego
    Noguchi
    Reading
    Students
    Numbered Shelves:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38]
    """
    numbered_shelves = []
    named_places = []
    print("---------- Valid Locations ----------")
    for location in locations_list:
        if location.isdigit() is True:
            numbered_shelves.append(int(location))
        elif location.isdigit() is False:
            named_places.append(location)
    sorted_places = sorted(named_places)
    for place in sorted_places:
        print(f'{place}')
    sorted_shelves = sorted(numbered_shelves)
    print(f"Numbered Shelves:\n{fill(str(sorted_shelves), 32)}")


def quit_books(book_collection):
    """
    saves the file as the name 'programming.txt' and quit the program.

    :precondition: no precondition, the function can always execute
    :postcondition: the program would save the book list as a tab-separated table (to original file) and quit
    :return: none

    """
    # filename = input("Please enter the save file name of the updated tab-separated book list: ")
    # user input disabled for filename for test purpose

    filename = "books.txt"

    with open(filename, mode="w", encoding='utf-16') as file_object:
        first_line = first_line_formatting(book_collection)
        file_object.write(f'{first_line}\n')

        for book in book_collection:
            for field in book:
                file_object.write(f'{book.get(field)}\t')
            file_object.write('\n')

    quit()


def first_line_formatting(book_collection):
    """format the first line of fields before writing on the save file.

    :param book_collection: a tuple of dictionaries
    :precondition: book_collection must be a tuple of dictionaries
    :postcondition: convert to a line of string of fields separated by tab
    :return: a string of fields separated by tab

    >>> bc = books()
    >>> first_line_formatting(bc)
    'Author\\tTitle\\tPublisher\\tShelf\\tCategory\\tSubject'
    """
    field_list = []
    i = 0
    for book in book_collection:
        while i < 1:
            for field in book:
                field_list.append(field)
            i += 1
    first_line = '\t'.join(field_list)
    return first_line


def main():
    """
    Drives the program.
    """
    book_collection = books()
    menu(book_collection)


if __name__ == '__main__':
    main()
