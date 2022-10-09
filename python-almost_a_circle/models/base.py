#!/usr/bin/python3
'''The Base class.'''


import json
from os.path import exists


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == '':
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        objs_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for obj in list_objs:
                objs_list.append(obj.to_dictionary())

        with open(filename, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(objs_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
