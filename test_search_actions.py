"""Unit Test"""

from unittest import TestCase
from unittest.mock import patch
from books import search_actions
import io


class TestSearchActions(TestCase):

    @patch('builtins.input', side_effect=['abrams'])
    def test_search_actions_partial_keyword_lowercase_multiple_result(self, mock_input):
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
        actual = search_actions(1, book_collection)
        expected = [(1, {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'}),
                    (2, {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'}),
                    (3, {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6',
                     'Publisher': 'Abramson', 'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'}),
                    (4, {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
                     'Shelf': '2', 'Category': 'Language', 'Subject': 'English'})]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_search_actions_numbered_shelf_exact_match_single_result(self, mock_input):
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
        actual = search_actions(4, book_collection)
        expected = [(1, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '1',
                         'Category': 'Fiction', 'Subject': 'SF'})]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['LEGO'])
    def test_search_actions_named_shelf_uppercase(self, mock_input):
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
        actual = search_actions(4, book_collection)
        expected = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
                         'Category': 'Fiction', 'Subject': 'SF'})]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['n/a'])
    def test_search_actions_publisher_missing_info(self, mock_input):
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
        actual = search_actions(3, book_collection)
        expected = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': 'Lego',
                         'Category': 'Fiction', 'Subject': 'SF'}),
                    (2, {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
                         'Category': 'Fiction', 'Subject': 'SF'}),
                    (3, {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '13',
                         'Category': 'Fiction', 'Subject': 'SF'})]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Thrall'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_actions_no_match(self, mock_stdout, mock_input):
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
        search_actions(1, book_collection)
        expected = "Apologies(in Spencer's tone), Your search did not match any book in the collection. \n"
        self.assertEqual(expected, mock_stdout.getvalue())
