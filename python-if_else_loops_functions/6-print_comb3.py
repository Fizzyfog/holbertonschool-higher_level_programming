#!/usr/bin/python3

for tens_digit in range(0, 10):

    for ones_digit in range(0, 10):

        if tens_digit < ones_digit and tens_digit != 8:
            print("{}{}".format(tens_digit, ones_digit), end=", ")

        elif tens_digit == 8 and ones_digit == 9:
            print("{}{}".format(tens_digit, ones_digit))
