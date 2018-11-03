"""
Module problem_29 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_29


class TestMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        expected_output = "4A3B2C1D2A"

        input = "AAAABBBCCDAA"

        self.assertEqual(problem_29.run_length_encode(input), expected_output)


if __name__ == '__main__':
    unittest.main()
