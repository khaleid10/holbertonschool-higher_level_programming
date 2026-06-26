#!/usr/bin/python3
"""This module defines a function that checks subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class, otherwise False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
