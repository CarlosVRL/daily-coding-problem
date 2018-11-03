"""
Module problem_29

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a
single count and character.

For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string
to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def run_length_encode(input):

    print("The input is : " + input)

    encoded = ""

    character_count = 0
    current_character = ""

    for letter in input:

        if letter != current_character:

            # Flush the running count, ignore init
            if current_character != "":
                encoded += str(character_count)
                encoded += current_character

            character_count = 1
            current_character = letter

        else:
            character_count += 1

    # Flush the running count
    encoded += str(character_count)
    encoded += current_character

    return encoded
