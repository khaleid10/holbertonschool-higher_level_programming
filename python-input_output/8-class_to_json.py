#!/usr/bin/python3
"""Module that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    return obj.__dict__
