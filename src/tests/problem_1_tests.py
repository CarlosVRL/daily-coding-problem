"""
Module problem_1 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_1


class TestStringMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        numbers = [1, 2]
        k = 3
        self.assertEqual(problem_1.check_numbers_for_sum(numbers, k), True)

    def test_simple_case_is_not_valid(self):
        numbers = [1, 2]
        k = 4
        self.assertEqual(problem_1.check_numbers_for_sum(numbers, k), False)

    def test_medium_array_locates_sum(self):
        numbers = [6, 2, 19, 12, 4, 2]
        k = 14
        self.assertEqual(problem_1.check_numbers_for_sum(numbers, k), True)

    def test_medium_array_locates_sum_not(self):
        numbers = [6, 2, 19, 12, 4, 2]
        k = 3
        self.assertEqual(problem_1.check_numbers_for_sum(numbers, k), False)


if __name__ == '__main__':
    unittest.main()
