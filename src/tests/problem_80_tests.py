"""
Module problem_80 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_80


class TestMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        expected_output = "d"

        # Initialize the nodes
        a = problem_80.Node("a")
        b = problem_80.Node("b")
        c = problem_80.Node("c")
        d = problem_80.Node("d")

        a.left = b
        a.right = c
        b.left = d

        root = a
        max_level = 0
        res = 0

        self.assertEqual(expected_output, problem_80.find_deepest(root, 0, max_level, res))


if __name__ == '__main__':
    unittest.main()
