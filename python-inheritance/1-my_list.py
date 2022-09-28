#!/usr/bin/python3
'''The my_list module.'''


class MyList(list):
    '''Creates a subclass of MyList.'''
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        '''Prints a sorted list.'''
        print(sorted(self))
