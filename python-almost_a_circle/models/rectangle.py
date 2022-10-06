#!/usr/bin/python3
"""The Rectangle class."""


from models.base import Base


class Rectangle(Base):
    """Constructs a Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns a Rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes the value of a Retangle's width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns a Rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes the value of a Retangle's height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns a Rectangle's x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Changes the value of a Retangle's x."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns a Rectangle's y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Changes the value of a Retangle's y."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns a Rectangle's area."""
        return self.width * self.height
