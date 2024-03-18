#!/usr/bin/env python3
''' Asynchronous coroutine
'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''function takes int argument with default value
    waits for random delay between 0 and int argument
    returns float value of delay'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
