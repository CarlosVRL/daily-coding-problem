"""
Module problem_70 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_70


class TestMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        expected_output = 19

        n = 1

        self.assertEqual(expected_output, problem_70.find_perfect_number(n))

    def test_simple_case_2_is_valid(self):
        expected_output = 28

        n = 2

        self.assertEqual(expected_output, problem_70.find_perfect_number(n))

    def test_multi_case_is_valid(self):
        expected_output = 154

        n = 15

        self.assertEqual(expected_output, problem_70.find_perfect_number(n))


if __name__ == '__main__':
    unittest.main()
