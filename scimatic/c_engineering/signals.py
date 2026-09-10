from typing import AsyncGenerator
from scimatic import flicker_module
import time
import asyncio
import random

def flick_once(
        vecbools: list[bool],
        binary: bool = False,
) -> list[bool | int]:

    output = flicker_module.flick(vecbools, binary)

    return output

async def delay(
        vecbools: list[bool],
        seconds: float,
        binary: bool = False
) -> list[bool | int]:

    start = time.perf_counter()

    output = flicker_module.flick(vecbools, binary)

    end = time.perf_counter()

    elapsed = end - start

    await asyncio.sleep(max(0, seconds - elapsed))
    return output

async def pulse(
        vecbools: list[bool],
        iterations: int,
        time_interval: float,
        binary: bool = False,
) -> AsyncGenerator[list[bool | int], None]:

    state = vecbools

    for i in range(iterations):
        state = flicker_module.flick(state, False)
        output = [int(b) for b in state] if binary else state
        yield output
        if i < iterations - 1:
            await asyncio.sleep(time_interval)
