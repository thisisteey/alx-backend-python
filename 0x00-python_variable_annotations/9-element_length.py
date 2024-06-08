#!/usr/bin/env python3
"""Module defined for function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """adds the length of a list of sequence"""
    return [(i, len(i)) for i in lst]
