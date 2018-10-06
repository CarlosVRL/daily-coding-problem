"""
Module problem_1

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def check_numbers_for_sum(numbers, k):

    sum_found = False

    for i, outer_number in enumerate(numbers):

        a = outer_number

        for j, inner_number in enumerate(numbers):
            if i == j:
                continue
            b = inner_number
            if (a + b) == k:
                sum_found = True
                return sum_found

    return sum_found
