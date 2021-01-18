"""Unit Test"""
from unittest import TestCase
from books import search_action_logic


class TestSearchActionLogic(TestCase):

    def test_search_actions_partial_keyword_uppercase_multiple_result(self):
        book_collection = (
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
             'Shelf': '2', 'Category': 'Language', 'Subject': 'English'},
            {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13', 'Category': 'Fiction',
             'Subject': 'SF'})
        actual = search_action_logic(book_collection, "ABRAMS", 1)
        expected = [{'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                     'Shelf': '2', 'Category': 'Language', 'Subject': 'English'}]
        self.assertEqual(expected, actual)

    def test_search_actions_numbered_shelf_exact_match_single_result(self):
        book_collection = (
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
             'Shelf': '2', 'Category': 'Language', 'Subject': 'English'},
            {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13', 'Category': 'Fiction',
             'Subject': 'SF'})
        actual = search_action_logic(book_collection, "1", 4)
        expected = [{'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
                     'Category': 'Fiction', 'Subject': 'SF'}]
        self.assertEqual(expected, actual)

    def test_search_actions_named_shelf_lowercase(self):
        book_collection = (
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
             'Shelf': '2', 'Category': 'Language', 'Subject': 'English'},
            {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13', 'Category': 'Fiction',
             'Subject': 'SF'})
        actual = search_action_logic(book_collection, "lego", 4)
        expected = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
                     'Category': 'Fiction', 'Subject': 'SF'}]
        self.assertEqual(expected, actual)

    def test_search_actions_publisher_missing_info(self):
        book_collection = (
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
             'Shelf': '2', 'Category': 'Language', 'Subject': 'English'},
            {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13', 'Category': 'Fiction',
             'Subject': 'SF'})
        actual = search_action_logic(book_collection, "n/a", 3)
        expected = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
                     'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
                     'Category': 'Fiction', 'Subject': 'SF'},
                    {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13', 'Category': 'Fiction',
                     'Subject': 'SF'}]
        self.assertEqual(expected, actual)
