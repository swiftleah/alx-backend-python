#!/usr/bin/env python3
''' async routine
'''
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' function spawns wait_random n times with specified delay
    also returns list of delays in ascending order '''
    
