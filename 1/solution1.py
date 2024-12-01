#!/usr/bin/env python3

from typing import Any

data = open(0).read().strip().splitlines()

def parse_lines(data: list[str]) -> Any:
    l = []
    r = []
    for line in data:
        line = line.split()
        l.append(line[0])
        r.append(line[1])
    return [sorted(l), sorted(r)]

l, r = parse_lines(data)

t = 0
for le, re in zip(l, r):
    d = abs(int(le) - int(re))
    t += d
print(t)
