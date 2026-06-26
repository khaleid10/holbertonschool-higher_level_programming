#!/usr/bin/python3
"""This module defines a BaseGeometry class."""


class BaseGeometry:
    """This class represents the base geometry."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
