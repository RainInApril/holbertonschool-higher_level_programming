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
