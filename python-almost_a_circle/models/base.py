#!/usr/bin/python3
'''The Base class.'''


class Base:
    '''Constructs a Base class.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialises a Base.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
