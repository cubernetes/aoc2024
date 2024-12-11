#!/usr/bin/env python3
from functools import lru_cache
@lru_cache(200000)
def recurse(stone: str, depth: int) -> int:
    if depth == 0:
        return 1
    elif stone == '0':
        return recurse('1', depth - 1)
    elif len(stone) % 2 == 0:
        return recurse(stone[:len(stone) // 2], depth - 1) \
            + recurse(str(int(stone[len(stone) // 2:])), depth - 1)
    else:
        return recurse(str(int(stone) * 2024), depth - 1)
print(sum(map(lambda stone: recurse(stone, 75), input().split())))
