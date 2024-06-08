#!/usr/bin/env python3
"""Module defined for function safe_first_element"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Gets and returns the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
