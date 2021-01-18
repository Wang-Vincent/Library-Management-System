"""Unit Test"""
from unittest import TestCase
from books import select_book_logic


class TestSelectBookLogic(TestCase):
    def test_select_book_logic_multiple_result(self):
        result_list = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                            'Category': 'Fiction', 'Subject': 'SF'}),
                       (2, {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                            'Category': 'Fiction', 'Subject': 'SF'})]
        move_selection = "2"
        actual = select_book_logic(move_selection, result_list)
        expected = {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
                    'Category': 'Fiction', 'Subject': 'SF'}
        self.assertEqual(expected, actual)

    def test_select_book_logic_single_result(self):
        result_list = [(1, {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                            'Category': 'Fiction', 'Subject': 'SF'})]
        move_selection = "1"
        actual = select_book_logic(move_selection, result_list)
        expected = {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
                    'Category': 'Fiction', 'Subject': 'SF'}
        self.assertEqual(expected, actual)
