"""Unit Test"""
from unittest import TestCase
from books import first_line_formatting


class TestFirstLineFormatting(TestCase):

    def test_first_line_formatting(self):
        book_collection = (
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine July 1976', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 12', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abramson', 'Title': 'Galaxy Science Fiction Magazine Number 6', 'Publisher': 'Abramson',
             'Shelf': '18', 'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Abrams', 'Title': 'A Glossary of Literary Terms 7e', 'Publisher': 'Harcourt Brace',
             'Shelf': '2', 'Category': 'Language', 'Subject': 'English'},
            {'Author': 'Asimov', 'Title': '"The Stars, Like Dust"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Norton', 'Title': 'Postmarked the Stars', 'Publisher': 'Ace', 'Shelf': '11',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Asimov', 'Title': '"The Currents of Space"', 'Publisher': 'n/a', 'Shelf': '38',
             'Category': 'Fiction', 'Subject': 'SF'},
            {'Author': 'Brin', 'Title': 'Sundiver', 'Publisher': 'n/a', 'Shelf': '33', 'Category': 'Fiction',
             'Subject': 'SF'})
        actual = first_line_formatting(book_collection)
        expected = "Author\tTitle\tPublisher\tShelf\tCategory\tSubject"
        self.assertEqual(expected, actual)
