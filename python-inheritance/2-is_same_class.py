#!/usr/bin/python3
"""This module defines a function that checks the exact class of an object."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

Otherwise, return False.
"""
    return type(obj) is a_class
