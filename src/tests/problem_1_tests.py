"""
Module problem_1 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_1


class TestStringMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        numbers = [1, 2];
        k = 3;
        self.assertEqual(problem_1.check_numbers_for_sum(numbers, k), True)


if __name__ == '__main__':
    unittest.main()
