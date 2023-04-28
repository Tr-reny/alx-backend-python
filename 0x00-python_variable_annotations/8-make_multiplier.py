#!/usr/bin/env python3
"""
This module contains a function 'make_multiplier' that
takes a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier: the float value to multiply by

    Returns:
        A function that multiplies a float by the given multiplier.
    """
    def multiply(n: float) -> float:
        """
        Multiplies the given float by the multiplier.

        Args:
            n: the float value to be multiplied

        Returns:
            The product of n and the multiplier.
        """
        return n * multiplier

    return multiply
