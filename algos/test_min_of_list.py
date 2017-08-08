import unittest
import algos.list_math_utils as utils

class MinOfListTestCase(unittest.TestCase):
    def test_emptylist(self):
        self.assertEqual(None, utils.min_of_list([]))

    def test_positive_numbers(self):
        self.assertEqual(1, utils.min_of_list([22, 3, 1, 90, 7]))

    def test_negative_numbers(self):
        self.assertEqual(-888, utils.min_of_list([-2, -66, -11, -7, -222, -888]))

    def test_list_with_zero(self):
        self.assertEqual(0, utils.min_of_list([22, 3, 1, 90, 0, 7]))

    def test_double_values_in_list(self):
        self.assertEqual(-100.23,utils.min_of_list([22, 44, 12, 5, 9, -10, 22.34, -99.21, -100.23]))


if __name__ == '__main__':
    unittest.main()
