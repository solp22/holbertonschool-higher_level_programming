#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = ord(str[i])
        if letter > 96 and letter < 123:
            letter -= 32
        print("{}".format(chr(letter)), end="")
    print("")
