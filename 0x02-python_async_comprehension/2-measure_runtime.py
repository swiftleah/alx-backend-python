#!/usr/bin/env python3
''' function measure_runtime
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' executes async_comprehension 4 times in parallel using
    ayncio.gather and measures total run time
    returns total run time in float form'''
    starttime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    totaltime = time.time() - starttime
    return totaltime
