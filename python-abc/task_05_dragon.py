#!/usr/bin/env python3
"""Module that demonstrates mixins."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying abilities."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
