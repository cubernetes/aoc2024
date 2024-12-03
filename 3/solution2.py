#!/usr/bin/env python3

import re
data = open(0).read().strip()

t = 0
flag = True
for match in re.finditer(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|don\'t\(\)', data):
    m = match.group(0)
    if m == "don't()":
        flag = False
    if m == "do()":
        flag = True
    if m.startswith("mul(") and flag:
        t += eval(match.group(0).removeprefix('mul(').removesuffix(')').replace(",",'*'))
print(t)
