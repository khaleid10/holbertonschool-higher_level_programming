#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
