#!/usr/bin/env python3
"""
This module contains a function 'safe_first_element' that returns the first element
of a list or None if the list is empty. The function is duck-typed.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list or None if the list is empty.

    Args:
        lst: The list to get the first element from.

    Returns:
        The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
