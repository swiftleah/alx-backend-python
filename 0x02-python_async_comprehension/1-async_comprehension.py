#!/usr/bin/env python3
''' function async_comprehension
'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' collects 10 random numbers using async comprehensing over previous
    function and returns the 10 random numbers '''
    return [Num async for Num in async_generator()]
