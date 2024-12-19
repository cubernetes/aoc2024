#!/usr/bin/env pypy3

from functools import cache

@cache
def can_be_made(towel: str) -> int:
    global patterns
    if not towel:
        return 1
    n=0
    for pattern in patterns:
        if towel.startswith(pattern):
            n+=can_be_made(towel.removeprefix(pattern))
    return n

patterns, towels = open(0).read().split('\n\n')
patterns = patterns.split(', ')
towels = towels.splitlines()
t=0
for towel in towels:
    t+=can_be_made(towel)
print(t)
