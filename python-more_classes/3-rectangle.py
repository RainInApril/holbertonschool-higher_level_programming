#!/usr/bin/python3
'''Defines a rectangle.'''


class Rectangle:
    '''Provides a blue print of class Square.'''
    def __init__(self, width=0, height=0):
        '''Initialises a rectangle.'''
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        '''Retrieves width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets width of rectangle.'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieves height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets height of rectangle.'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of retangle.'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter of rectangle.'''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        '''Prints rectangle with #.'''
        rect_str = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                for j in range(self.width):
                    rect_str = rect_str + "#"
                if i != self.height - 1:
                    rect_str = rect_str + "\n"
        return rect_str
