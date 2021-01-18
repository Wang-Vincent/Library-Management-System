"""Unit Test"""
from unittest import TestCase
from unittest.mock import patch
from books import print_menu_options
import io


class TestPrintMenuOption(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_menu_options(self, mock_stdout):
        print_menu_options()
        expected = '\n------------------------------BOOKS MANAGEMENT SYSTEM------------------------------\n\n' \
                   '1: Search Book by Author\n2: Search Book by Title\n3: Search Book by Publisher\n' \
                   '4: Search Book by Shelf/Location\n5: Search Book by Category\n6: Search Book by Subject\n' \
                   '7: Move Book\n0: Save & Quit\n\nSEARCH GUIDANCE:\nA. If you want to search for the books that ' \
                   'have no information in certain field (e.g. Publisher)\nplease enter "N/A" into the search keyword '\
                   'when it prompt.\nB. If you want to search by numbered shelf, please enter the exact number of ' \
                   'that shelf into the\nsearch keyword when it prompt.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
