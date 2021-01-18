"""Unit Test"""
from unittest import TestCase
from books import get_valid_locations


class TestGetValidLocation(TestCase):

    def test_get_valid_locations(self):
        book_collection = (
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '1', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '2', 'Category': 'Dummy',
             'Subject': 'Dummy'},
            {'Author': 'Dummy', 'Title': 'Dummy', 'Publisher': 'Dummy', 'Shelf': '11', 'Category': 'Dummy',
             'Subject': 'Dummy'},
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
        actual = get_valid_locations(book_collection)
        expected = ['1', '11', '2', '23', '6', '8', 'Island', 'Lego', 'Reading', 'Student']
        self.assertEqual(expected, actual)
