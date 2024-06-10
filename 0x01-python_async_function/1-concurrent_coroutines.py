#!/usr/bin/env python3
"""Module defined for async function wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times and returns a list of the wait times"""
    random_delay = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(random_delay)
