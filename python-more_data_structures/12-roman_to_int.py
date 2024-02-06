#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    prev_value = 0

    for char in roman_string:
        value = roman_numbers[char]
        if prev_value < value:
            roman_int += value - prev_value * 2
        else:
            roman_int += value
        prev_value = value
    return roman_int
