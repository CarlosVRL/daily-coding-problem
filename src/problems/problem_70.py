"""
Module problem_70

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def find_perfect_number(n):
    values_as_string = list(str(n))
    total = find_sum_from_string(values_as_string)
    perfect = 10
    remainder = perfect - total
    return int(str(n) + str(remainder))


def find_sum_from_string(values_as_string):
    total = 0
    for value_as_string in values_as_string:
        total += int(value_as_string)
    return total
