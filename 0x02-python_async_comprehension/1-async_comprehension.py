#!/usr/bin/env python3
"""Module defined for async function async_comprehension"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously collects 10 random float nums from an async generator
    and returns them as a list"""
    return [random_num async for random_num in async_generator()]
