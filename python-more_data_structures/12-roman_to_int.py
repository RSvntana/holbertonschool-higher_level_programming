#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letter = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]

    number = 0
    last = 0
    for letter in roman_string:
        for elm in roman_letter:
            if letter == elm[0]:
                if last == 0 or last >= elm[1]:
                    number += elm[1]
                elif last < elm[1]:
                    num += elm[1] - (last * 2)

                last = number

    return number
