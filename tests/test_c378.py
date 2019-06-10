import unittest
from finished.c378 import (
    remove_zeros,
    sort_descending,
    number_greater_than_length_of_sequence,
    subtract_one_from_first_n_number_of_items,
    havel_hakimi_algorithm,
)


class TestChallenge378(unittest.TestCase):

    def test_remove_zeros(self):
        self.assertEqual(remove_zeros([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), [5, 3, 2, 6, 2, 7, 2, 5])
        self.assertEqual(remove_zeros([4, 0, 0, 1, 3]), [4, 1, 3])
        self.assertEqual(remove_zeros([1, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_zeros([0, 0, 0]), [])
        self.assertEqual(remove_zeros([]), [])

    def test_sort_descending(self):
        self.assertEqual(sort_descending([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), [7, 6, 5, 5, 3, 2, 2, 2, 0, 0])
        self.assertEqual(sort_descending([4, 0, 0, 1, 3]), [4, 3, 1, 0, 0])
        self.assertEqual(sort_descending([1, 2, 3]), [3, 2, 1])
        self.assertEqual(sort_descending([0, 0, 0]), [0, 0, 0])
        self.assertEqual(sort_descending([]), [])

    def test_number_greater_than_length_of_sequence(self):
        self.assertEqual(number_greater_than_length_of_sequence(7, [6, 5, 5, 3, 2, 2, 2]), False)
        self.assertEqual(number_greater_than_length_of_sequence(5, [5, 5, 5, 5, 5]), False)
        self.assertEqual(number_greater_than_length_of_sequence(5, [5, 5, 5, 5]), True)
        self.assertEqual(number_greater_than_length_of_sequence(3, [1, 1]), True)
        self.assertEqual(number_greater_than_length_of_sequence(1, []), True)
        self.assertEqual(number_greater_than_length_of_sequence(0, []), False)

    def test_subtract_one_from_first_n_number_of_items(self):
        self.assertEqual(subtract_one_from_first_n_number_of_items(4, [5, 4, 3, 2, 1]), [4, 3, 2, 1, 1])
        self.assertEqual(subtract_one_from_first_n_number_of_items(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]), [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2])
        self.assertEqual(subtract_one_from_first_n_number_of_items(1, [10, 10, 10]), [9, 10, 10])
        self.assertEqual(subtract_one_from_first_n_number_of_items(3, [10, 10, 10]), [9, 9, 9])
        self.assertEqual(subtract_one_from_first_n_number_of_items(1, [1]), [0])

    def test_havel_hakimi_algorithm(self):
        self.assertEqual(havel_hakimi_algorithm([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), False)
        self.assertEqual(havel_hakimi_algorithm([4, 2, 0, 1, 5, 0]), False)
        self.assertEqual(havel_hakimi_algorithm([3, 1, 2, 3, 1, 0]), True)
        self.assertEqual(havel_hakimi_algorithm([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]), True)
        self.assertEqual(havel_hakimi_algorithm([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]), True)
        self.assertEqual(havel_hakimi_algorithm([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]), False)
        self.assertEqual(havel_hakimi_algorithm([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]), False)
        self.assertEqual(havel_hakimi_algorithm([2, 2, 0]), False)
        self.assertEqual(havel_hakimi_algorithm([3, 2, 1]), False)
        self.assertEqual(havel_hakimi_algorithm([1, 1]), True)
        self.assertEqual(havel_hakimi_algorithm([1]), False)
        self.assertEqual(havel_hakimi_algorithm([]), True)


if __name__ == '__main__':
    unittest.main()
