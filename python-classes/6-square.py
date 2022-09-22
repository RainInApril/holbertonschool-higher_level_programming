#!/usr/bin/python3
'''Defines a square.'''


class Square:
    '''Blueprint of objects of class Square.'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialises a square.'''
        self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        '''Retrieves size of square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets size of square.'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''Retrieves position of square.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Sets position of square.'''
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
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
            return

        for width in range(self.__position[1]):
            print()

        for length in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end='')
            for square in range(self.__size):
                print("#", end='')
            print()
