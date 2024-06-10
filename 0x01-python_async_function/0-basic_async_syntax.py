#!/usr/bin/env python3
"""Module defined for async function wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random amount of time up to max_delay"""
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
