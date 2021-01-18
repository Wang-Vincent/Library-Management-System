"""Unit Test"""
from unittest import TestCase
from unittest.mock import patch
from books import print_valid_location
import io


class TestPrintValidLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_valid_location_chris_list(self, mock_stdout):
        location_list = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23',
                         '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38',
                         '4', '5', '6', '7', '8', '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        print_valid_location(location_list)
        expected = "---------- Valid Locations ----------\n" \
                   "Gaby\nIsland\nLego\nNoguchi\nReading\nStudents\n" \
                   "Numbered Shelves:\n" \
                   "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\n11, 12, 13, 14, 15, 16, 17, 18,\n19, 20, 21, 22, 23, 24, 25, 26," \
                   "\n27, 28, 29, 30, 31, 32, 33, 34,\n35, 36, 37, 38]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_valid_location_random_list(self, mock_stdout):
        location_list = ['1', '10', '11', '12', '14', '15', '16', '17', '18', '19', '2', '20', '22',
                         '4', '5', '6', '7', '8', '9', 'Kitchen', 'Bedroom', 'Reading', 'Bathroom']
        print_valid_location(location_list)
        expected = "---------- Valid Locations ----------\n" \
                   "Bathroom\nBedroom\nKitchen\nReading\n" \
                   "Numbered Shelves:\n" \
                   "[1, 2, 4, 5, 6, 7, 8, 9, 10, 11,\n12, 14, 15, 16, 17, 18, 19, 20,\n22]\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
