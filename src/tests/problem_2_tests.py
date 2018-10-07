"""
Module problem_1 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_2


class TestStringMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        expected_numbers = [2, 3, 6]

        numbers = [3, 2, 1]

        self.assertEqual(problem_2.product_of_numbers_without_index(numbers), expected_numbers)

    def test_scenario_case_is_valid(self):
        expected_numbers = [120, 60, 40, 30, 24]

        numbers = [1, 2, 3, 4, 5]

        self.assertEqual(problem_2.product_of_numbers_without_index(numbers), expected_numbers)


if __name__ == '__main__':
    unittest.main()
