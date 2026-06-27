#!/usr/bin/python3
"""This module defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
