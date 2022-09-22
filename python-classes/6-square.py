#!/usr/bin/python3
'''Defines a square.'''


class Square:
    '''Initialises a square.'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''Retrieves position of square.'''
        return(self.__position)

    @position.setter
    def position(self, value):
        '''Sets position of square.'''
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''Returns the current square area.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #.'''
        if self.__size == 0:
            print()

        for width in range(self.__position[1]):
            print()

        for length in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end='')
            for square in range(self.__size):
                print("#", end='')
            print()
