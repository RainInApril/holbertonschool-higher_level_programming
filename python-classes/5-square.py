#!/usr/bin/python3
'''Defines a square.'''


class Square:
    '''Initialises a square.'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''Retrieves size of square.'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''Sets size of square.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Returns the current square area.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #.'''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
