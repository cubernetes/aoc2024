#!/usr/bin/env python3

import re
import numpy as np
e=enumerate

data = open(0).read().strip().splitlines()

def find_xmas(string: str) -> int:
    return len(list(re.finditer(r'XMAS', string)))

def transpose(strings: list[str]) -> list[str]:
    return [''.join(x) for x in np.transpose(list(map(list,strings)))]

def mirror(strings: list[str]) -> list[str]:
    strs = []
    for string in strings:
        strs.append(string[::-1])
    return strs

def diag_backslash(strings: list[str]) -> list[str]:
    strs = []
    for i, string in e(strings):
        strs.append(' ' * (len(string) - i - 1) + string + ' ' * i)
    strs = transpose(strs)
    return strs

t = 0

# worst approach lol

for line in data                                 + \
            mirror(data)                         + \
            transpose(data)                      + \
            mirror(transpose(data))              + \
            diag_backslash(data)                 + \
            mirror(diag_backslash(data))         + \
            diag_backslash(mirror(data))         + \
            mirror(diag_backslash(mirror(data))):
    t += find_xmas(line)

print(t)
