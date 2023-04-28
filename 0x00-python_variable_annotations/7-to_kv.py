#!/usr/bin/env python3
"""
This module contains a function 'to_kv' that
takes a string k and an int or float v as arguments
and returns a tuple with k as its first element and
the square of v as its second element.

"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float.

    Args:
        k: a string to use as the first element of the returned tuple.
        v: an int or float to square and use as the second element of the returned tuple.

    Returns:
        A tuple containing a string and the square of the input number as a float.

    """
    return (k, v*v)
