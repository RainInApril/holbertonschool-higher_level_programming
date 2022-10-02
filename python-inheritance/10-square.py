#!/usr/bin/python3
'''The Square class.'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Constructs class Square.'''
    def __init__(self, size):
        '''Initialises a square with the given size.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Returns the area of a square.'''
        return (self.__size ** 2)
