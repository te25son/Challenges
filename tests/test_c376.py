import unittest
from c376 import num_of_leap_years


class TestChallenge376(unittest.TestCase):

    def test_num_of_leap_years(self):
        self.assertEqual(num_of_leap_years(2016, 2017), 1)
        self.assertEqual(num_of_leap_years(2019, 2020), 0)
        self.assertEqual(num_of_leap_years(1900, 1901), 0)
        self.assertEqual(num_of_leap_years(2000, 2001), 1)
        self.assertEqual(num_of_leap_years(2800, 2801), 0)
        self.assertEqual(num_of_leap_years(123456, 123456), 0)
        self.assertEqual(num_of_leap_years(1234, 5678), 1077)
        # self.assertEqual(num_of_leap_years(123456, 7891011), 1881475)
        # self.assertEqual(num_of_leap_years(123456789101112, 1314151617181920), 288412747246240)
