#!/usr/bin/env python3

import re
data = open(0).read().strip()

t = 0
for match in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', data):
    t+= eval(match.group(0).removeprefix('mul(').removesuffix(')').replace(",",'*'))

print(t)
