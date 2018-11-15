"""
Module problem_41 tests
"""
import unittest
import sys
sys.path.append("../problems")
import problem_41


class TestMethods(unittest.TestCase):

    def test_simple_case_is_valid(self):
        expected_output = ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

        start = 'YUL'
        flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]

        self.assertEqual(expected_output, problem_41.compute_itinerary(flights, start))

    def test_second_case_is_valid(self):
        expected_output =  ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

        start = 'YUL'
        flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]

        self.assertEqual(expected_output, problem_41.compute_itinerary(flights, start))

    def test_simple_case_is_not_valid(self):
        expected_output = None

        start = 'COM'
        flights = [('SFO', 'COM'), ('COM', 'YYZ')]

        self.assertEqual(expected_output, problem_41.compute_itinerary(flights, start))

    # def test_lexicographical_example(self):
    #     expected_output = ['A', 'B', 'C', 'A', 'C']
    #
    #     start = 'A'
    #     flights = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    #
    #     self.assertEqual(expected_output, problem_41.compute_itinerary(flights, start))


if __name__ == '__main__':
    unittest.main()
