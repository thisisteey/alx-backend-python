#!/usr/bin/env python3
"""Module defined for async function async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously gets a sequence of 10 random float num btw 0 & 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
