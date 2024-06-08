#!/usr/bin/env python3
"""Module defined for function safely_get_value"""
from typing import Any, Mapping, Union, TypeVar


TypV = TypeVar('T')
Resd = Union[Any, TypV]
Defd = Union[TypV, None]


def safely_get_value(dct: Mapping, key: Any, default: Defd = None) -> Resd:
    """gets and returns the value of a dict using a specific key"""
    if key in dct:
        return dct[key]
    else:
        return default
