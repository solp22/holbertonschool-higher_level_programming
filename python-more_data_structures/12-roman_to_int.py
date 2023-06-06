#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    convert = {'M': 1000, 'D': 500, 'C': 100,
               'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal = 0
    for letter in roman_string:
        if letter in convert.keys():
            if decimal < convert[letter]:
                decimal *= -1
            decimal += convert[letter]
        else:
            return 0
    return (decimal)
