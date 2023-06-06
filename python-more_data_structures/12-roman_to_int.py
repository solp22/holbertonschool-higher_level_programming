#!/usr/bin/python3
def roman_to_int(roman_string):
    convert = {'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1 }
    decimal = 0
    for letter in roman_string:
        if convert.get(letter):
            if decimal < convert[letter]:
                decimal *= -1
            decimal += convert[letter]
    return (decimal)
