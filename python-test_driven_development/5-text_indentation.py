#!/usr/bin/python3
'''
The "5-text_indentation" module, with function:

text_indentation(text)
'''


def text_indentation(text):
    '''prints a text with 2 new lines after . ? and :.'''
    if type(text) != str:
        raise TypeError("text must be a string")

    flag = 0

    for char in text:
        if flag == 0:
            if char == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if char == "." or char == "?" or char == ":":
                print(char)
                print()
                flag = 0
            else:
                print(char, end='')
