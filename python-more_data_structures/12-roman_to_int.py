#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom = roman_string
    conv = {'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal = 0
    output = []
    for ind, letter in enumerate(rom):
        if letter in conv.keys():
            if ind != len(rom) - 1 and conv[rom[ind + 1]] > conv[letter]:
                output.append(conv[letter] * -1)
                decimal = 0
            else:
                output.append(conv[letter])
        else:
            return 0
    output.append(decimal)
    return int(sum(output))
