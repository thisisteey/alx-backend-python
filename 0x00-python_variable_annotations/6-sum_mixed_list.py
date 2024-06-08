#!/usr/bin/env python3
"""Module defined for function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """adds the sum of a list of ints and floats"""
    return float(sum(mxd_lst))
