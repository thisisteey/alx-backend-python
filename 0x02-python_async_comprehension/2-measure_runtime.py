#!/usr/bin/env python3
"""Module defined for async function measure_runtime"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynchronously executes the async_comprehension coroutine 4 times
    in parallel and measures the total execution time"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time
