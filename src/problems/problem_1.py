"""
Module problem_1

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def check_numbers_for_sum(numbers, k):

    sum_found = False

    previous_numbers = []

    for number in numbers:

        for previous_number in previous_numbers:

            if number + previous_number == k:
                sum_found = True
                return sum_found

        previous_numbers.append(number)

    return sum_found
