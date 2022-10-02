#!/usr/bin/python3
'''The Rectangle class.'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass of BaseGeometry.'''
    def __init__(self, width, height):
        '''Initialises a rectangle with width and height.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns the area of a rectangle.'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Returns rectangle description.'''
        return f"[Rectangle] {self.__width}/{self.__height}"
