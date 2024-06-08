#!/usr/bin/env python3
"""Module defined for function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts key and value to a tuple of the key and square of the value"""
    return (k, float(v**2))
