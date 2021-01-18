"""Unit Test"""
from unittest import TestCase
from unittest.mock import patch
from books import print_result
import io


class TestPrintResult(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_multiple_result_printout(self, mock_stdout):
        result_list = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                        'Category': 'Fiction', 'Subject': 'SF'},
                       {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                        'Category': 'Fiction', 'Subject': 'SF'}]
        print_result(result_list)
        expected = '--------------------------------------------------\n' \
                   'Result #1\nAuthor: Asimov\nTitle: "The Stars, Like Dust"\nPublisher: n/a\n' \
                   'Shelf: 38\nCategory: Fiction\nSubject: SF\n' \
                   '--------------------------------------------------\n' \
                   'Result #2\nAuthor: Norton\nTitle: Postmarked the Stars\nPublisher: Ace\nShelf: 11\n' \
                   'Category: Fiction\nSubject: SF\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_result_multiple_result_return(self):
        result_list = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                        'Category': 'Fiction', 'Subject': 'SF'},
                       {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                        'Category': 'Fiction', 'Subject': 'SF'}]
        actual = print_result(result_list)
        expected = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                         'Category': 'Fiction', 'Subject': 'SF'}),
                    (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                         'Category': 'Fiction', 'Subject': 'SF'})]
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_single_result_printout(self, mock_stdout):
        result_list = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                        'Category': 'Fiction', 'Subject': 'SF'}]
        print_result(result_list)
        expected = '--------------------------------------------------\n' \
                   'Result #1\nAuthor: Asimov\nTitle: "The Stars, Like Dust"\nPublisher: n/a\n' \
                   'Shelf: 38\nCategory: Fiction\nSubject: SF\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_result_single_result_return(self):
        result_list = [{'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                        'Category': 'Fiction', 'Subject': 'SF'}]
        actual = print_result(result_list)
        expected = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                         'Category': 'Fiction', 'Subject': 'SF'})]
        self.assertEqual(actual, expected)
