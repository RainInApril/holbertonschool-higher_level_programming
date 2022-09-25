#!/usr/bin/python3
'''
The "0-add_integer" module, with function:

add_integer(a, b)
'''


def add_integer(a, b=98):
    '''Adds 2 int and returns a result.'''
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
