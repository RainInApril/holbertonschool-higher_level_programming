#!/usr/bin/python3
'''The BaseGeometry class.'''


class BaseGeometry:
    '''A class with a public instance method area.'''
    def area(self):
        '''Raises an exception for area.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value.'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
