#!/usr/bin/env python3
"""Module that defines function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by a float multiplier"""
    return lambda i: i * multiplier
