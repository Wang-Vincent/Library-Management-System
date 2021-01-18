"""Unit Test"""
from unittest import TestCase
from books import move_actions
from unittest.mock import patch
import io


class TestMoveActions(TestCase):

    def test_move_actions_named_location(self):
        book_collection = (
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '1', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '2', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Target', 'Title': 'Target', 'Publisher': 'Target', 'Shelf': '11', 'Category': 'Target',
             'Subject': 'Target'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '8', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '23', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '6', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Island', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Reading', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Student', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Lego', 'Category': 'Dummy',
             'Subject': 'Dummy'},
        )
        selected_book = book_collection[2]
        new_location = 'Island'
        move_actions(selected_book, new_location, book_collection)
        self.assertEqual(new_location, book_collection[2]['Shelf'])

    def test_move_actions_numbered_shelf(self):
        book_collection = (
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '1', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '2', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Target', 'Title': 'Target', 'Publisher': 'Target', 'Shelf': '11', 'Category': 'Target',
             'Subject': 'Target'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '8', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '23', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '6', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Island', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Reading', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Student', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Lego', 'Category': 'Dummy',
             'Subject': 'Dummy'},
        )
        selected_book = book_collection[2]
        new_location = '2'
        move_actions(selected_book, new_location, book_collection)
        self.assertEqual(new_location, book_collection[2]['Shelf'])

    @patch('builtins.input', side_effect=['9'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_actions_invalid_place(self, mock_stdout, mock_input):
        book_collection = (
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '1', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '2', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Target', 'Title': 'Target', 'Publisher': 'Target', 'Shelf': '11', 'Category': 'Target',
             'Subject': 'Target'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '8', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '23', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '6', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Island', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Reading', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Student', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': 'Lego', 'Category': 'Dummy',
             'Subject': 'Dummy'},
        )
        selected_book = book_collection[2]
        new_location = 'Stormwind'
        move_actions(selected_book, new_location, book_collection)
        expected = "Sorry, you did not entered a valid location. I can not move the book over there.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
