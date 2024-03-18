#!/usr/bin/env python3
''' function measure_time
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' function measures total execution time for wait_n function
    '''
    startingTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - startingTime) / n)
