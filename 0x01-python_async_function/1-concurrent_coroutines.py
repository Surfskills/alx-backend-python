#!/usr/bin/env python3

"""

This module contains a coroutine that collects 10 random numbers using async

 comprehension over the previous async_generator, then return the 10

 random numbers

"""

import asyncio

import random

from typing import List



async_generator = __import__('0-async_generator').async_generator





async def async_comprehension() -> List[float]:

    """

    collects 10 random numbers using async comprehension using the imported

     coroutine, and return the 10 random numbers

    """

    result = [i async for i in async_generator()]

    return 
#!/usr/bin/env python3

""" The basics of async """



import asyncio

from typing import List



wait_random = __import__('0-basic_async_syntax').wait_random





async def wait_n(n: int, max_delay: int) -> List[float]:

    """

    spawn wait_random n times with the specified max_delay.

    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)
