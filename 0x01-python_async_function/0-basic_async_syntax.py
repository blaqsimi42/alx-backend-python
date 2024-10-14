#!/usr/bin/env python3

"""
basics of 
using the asyncio library in python
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    couroutine waits for a random number of seconds
C
    and returns the total number of seconds waited
    """
    if not isinstance(max_delay, int):
        raise TypeError('Max wait should be an int')
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
