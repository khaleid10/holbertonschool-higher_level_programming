#!/usr/bin/python3
"""Module for reading UTF-8 text files."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
