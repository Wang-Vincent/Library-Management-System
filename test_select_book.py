"""Unit Test"""
from unittest import TestCase
from unittest.mock import patch
from books import select_book
import io


class TestSelectBook(TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_select_book_yes_lowercase_multiple_result(self, mock_input):
        result_list = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                            'Category': 'Fiction', 'Subject': 'SF'}),
                       (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                            'Category': 'Fiction', 'Subject': 'SF'})]
        move_selection = "2"
        actual = select_book(result_list, move_selection)
        expected = {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                    'Category': 'Fiction', 'Subject': 'SF'}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_book_no_uppercase(self, mock_stdout, mock_input):
        result_list = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                            'Category': 'Fiction', 'Subject': 'SF'}),
                       (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                            'Category': 'Fiction', 'Subject': 'SF'})]
        move_selection = "1"
        select_book(result_list, move_selection)
        expected = 'Author: Asimov\nTitle: "The Stars, Like Dust"\nPublisher: n/a\nShelf: 38\nCategory: Fiction\n' \
                   'Subject: SF\nApology if this is not the book you want to move. \n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=['y'])
    def test_select_book_yes_lowercase_single_result(self, mock_input):
        result_list = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                            'Category': 'Fiction', 'Subject': 'SF'})]
        move_selection = "1"
        actual = select_book(result_list, move_selection)
        expected = {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                    'Category': 'Fiction', 'Subject': 'SF'}
        self.assertEqual(expected, actual)
