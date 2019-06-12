import unittest
from finished.c377 import (
    fit_boxes_no_rotate,
    fit_boxes_rotate_all,
    fit_boxes_3D,
)


class TestChallenge377(unittest.TestCase):

    def test_fit_boxes(self):
        self.assertEqual(fit_boxes_no_rotate(25, 18, 6, 5), 12)
        self.assertEqual(fit_boxes_no_rotate(10, 10, 1, 1), 100)
        self.assertEqual(fit_boxes_no_rotate(12, 34, 5, 6), 10)
        self.assertEqual(fit_boxes_no_rotate(12345, 678910, 1112, 1314), 5676)
        self.assertEqual(fit_boxes_no_rotate(5, 100, 6, 1), 0)

    def test_fit_boxes_rotate_all(self):
        self.assertEqual(fit_boxes_rotate_all(25, 18, 6, 5), 15)
        self.assertEqual(fit_boxes_rotate_all(12, 34, 5, 6), 12)
        self.assertEqual(fit_boxes_rotate_all(12345, 678910, 1112, 1314), 5676)
        self.assertEqual(fit_boxes_rotate_all(5, 5, 3, 2), 2)
        self.assertEqual(fit_boxes_rotate_all(5, 100, 6, 1), 80)
        self.assertEqual(fit_boxes_rotate_all(5, 5, 6, 1), 0)

    def test_fit_boxes_3D(self):
        self.assertEqual(fit_boxes_3D(10, 10, 10, 1, 1, 1), 1000)
        self.assertEqual(fit_boxes_3D(12, 34, 56, 7, 8, 9), 32)
        self.assertEqual(fit_boxes_3D(123, 456, 789, 10, 11, 12), 32604)
        self.assertEqual(fit_boxes_3D(1234567, 89101112, 13141516, 171819, 202122, 232425), 174648)
