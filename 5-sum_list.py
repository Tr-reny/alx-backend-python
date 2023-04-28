#!/usr/bin/env python3
"""
This module contains a function 'sum_list' that
takes a list of floats as argument and returns their sum.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all the floats in the input list.

    Args:
        input_list: the list of floats to sum

    Returns:
        The sum of all the floats in the input list.
    """
    return sum(input_list)
