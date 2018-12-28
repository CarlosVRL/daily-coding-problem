"""
Module problem_83 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_83


class TestMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        # Initialize the nodes
        a = problem_83.Node("a")
        b = problem_83.Node("b")
        c = problem_83.Node("c")

        # Initial Tree
        root = a
        root.left = b
        root.right = c

        # Inverted Tree
        expected_output = problem_83.Node("a")
        expected_output.left = c
        expected_output.right = b

        inverted = problem_83.invert_binary_tree(root)

        self.assertEqual(expected_output.val, inverted.val)
        self.assertEqual(expected_output.left.val, inverted.left.val)
        self.assertEqual(expected_output.right.val, inverted.right.val)

    def test_second_level_case_is_valid(self):
        # Initialize the nodes
        a = problem_83.Node("a")
        b = problem_83.Node("b")
        c = problem_83.Node("c")
        d = problem_83.Node("d")
        e = problem_83.Node("e")
        f = problem_83.Node("f")

        # Initial Tree
        root = a
        root.left = b
        b.left = d
        b.right = e

        root.right = c
        c.left = f

        inverted = problem_83.invert_binary_tree(root)

        # Inverted Tree
        expected_output = problem_83.Node("a")
        expected_output.left = c
        expected_output.left.right = f
        expected_output.right = b
        expected_output.right.left = e
        expected_output.right.right = d

        self.assertEqual(expected_output.val, inverted.val)
        self.assertEqual(expected_output.left.val, inverted.left.val)
        self.assertEqual(expected_output.right.val, inverted.right.val)
        self.assertEqual(expected_output.left.right.val, inverted.left.right.val)
        self.assertEqual(expected_output.right.left.val, inverted.right.left.val)
        self.assertEqual(expected_output.right.right.val, inverted.right.right.val)


if __name__ == '__main__':
    unittest.main()
