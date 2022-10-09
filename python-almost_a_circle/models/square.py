#!/usr/bin/python3
"""The Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Constructs a Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialises a Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieves a Square's size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets a Square's value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes to a Square."""
        if args is not None and len(args) > 0:
            attributes = ("id", "size", "x", "y")
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, str(key), value)
