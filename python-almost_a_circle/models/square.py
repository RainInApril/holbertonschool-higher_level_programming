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
