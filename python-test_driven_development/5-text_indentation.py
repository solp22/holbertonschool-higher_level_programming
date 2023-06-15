#!/usr/bin/python3
'''text indentation module'''


def text_indentation(text):
    '''prints a text with 2 new lines after each of these characters: ., ? and :'''
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    for chars in range(len(text)):
        if text[chars] == "." or text[chars] =="?" or text[chars] == ":":
            print(text[chars])
            print()
            flag = 1
        if flag == 1:
            if text[chars + 1] == " ":
                continue
            flag = 0
        else:
            print(text[chars], end="")
