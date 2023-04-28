#!/usr/bin/env python3
"""
This module contains a function 'sum_mixed_list' that
takes a list of integers and floats as argument and returns their sum as a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the integers and floats in the input list as a float.

    Args:
        mxd_lst: A list of integers and floats.

    Returns:
        The sum of the integers and floats in the list as a float.
    """
    return sum(mxd_lst)
