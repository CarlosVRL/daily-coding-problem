"""
Module problem_2

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_numbers_without_index(numbers):

    res = []

    for outer_number in numbers:

        running_product = 1
        element_found = False

        for inner_number in numbers:

            # Skip the accumulation for first instance of value at index
            if inner_number == outer_number and not element_found:
                element_found = True
                continue

            if outer_number != inner_number:
                running_product = running_product * inner_number

        res.append(running_product)

    return res
