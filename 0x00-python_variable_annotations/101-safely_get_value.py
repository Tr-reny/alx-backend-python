#!/usr/bin/env python3
"""
This module contains a function 'safely_get_value' that safely retrieves a value from a dictionary.

The function takes a dictionary, a key to look for in the dictionary, and an optional default value to return
if the key is not found in the dictionary. The function returns the value associated with the key in the
dictionary, or the default value if the key is not present in the dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct: The dictionary to search for the key.
        key: The key to look for in the dictionary.
        default: An optional default value to return if the key is not present in the dictionary.

    Returns:
        The value associated with the key in the dictionary, or the default value if the key is not present in the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
