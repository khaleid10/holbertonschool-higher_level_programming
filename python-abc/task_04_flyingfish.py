#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print flying behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print habitat."""
        print("The flying fish lives both in water and the sky!")
