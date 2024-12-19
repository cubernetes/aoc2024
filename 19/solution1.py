#!/usr/bin/env pypy3

def can_be_made(towel: str, patterns: list[str]) -> bool:
    if not towel:
        return True
    for pattern in patterns:
        if towel.startswith(pattern):
            if can_be_made(towel.removeprefix(pattern), patterns):
                return True
    return False

patterns, towels = open(0).read().split('\n\n')
patterns = patterns.split(', ')
towels = towels.splitlines()
t=0
for towel in towels:
    if can_be_made(towel, patterns):
        t+=1
print(t)
