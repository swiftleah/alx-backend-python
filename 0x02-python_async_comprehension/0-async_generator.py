#!/usr/bin/env python3
''' function async_generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' takes no arguments
    coroutine loops 10 times, each time waits 1 second
    & yield number between 0-10 using random'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
