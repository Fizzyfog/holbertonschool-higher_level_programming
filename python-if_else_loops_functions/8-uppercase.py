#!/usr/bin/python3

def uppercase(input_string):

    for character in input_string:
        if ord(character) >= 97 and ord(character) <= 122:
            character = chr(ord(character) - 32)

        print("{}".format(character), end="")
    print("")
