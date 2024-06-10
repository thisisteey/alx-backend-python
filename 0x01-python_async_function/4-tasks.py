#!/usr/bin/env python3
"""Module defined for async function task_wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns list of the wait times"""
    random_delay = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(random_delay)
