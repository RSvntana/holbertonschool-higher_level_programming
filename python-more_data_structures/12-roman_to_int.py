#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_values = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    number = 0
    prev_value = 0

    for letter in roman_string:
        value = roman_values.get(letter, 0)

        if value > prev_value:
            number += value - 2 * prev_value
        else:
            number += value

        prev_value = value

    return number
