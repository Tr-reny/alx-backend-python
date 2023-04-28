#!/usr/bin/env python3
"""
This module contains a function 'element_length' that takes
a list of strings or any iterable that contains sequences,
and returns a list of tuples, where each tuple contains an
element from the input list and its length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an
    element from the input list and its length.

    Args:
        lst: an iterable that contains sequences, e.g. a list of strings

    Returns:
        A list of tuples, where each tuple contains an element from lst
        and its length. Each tuple has the form (element, length), where
        element is an element from lst and length is the length of element.
    """
    return [(i, len(i)) for i in lst]
