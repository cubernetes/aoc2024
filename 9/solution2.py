#!/usr/bin/env pypy3

from copy import deepcopy

expanded = []
idx = 0
for i, c in enumerate(open(0).read().strip().splitlines()[0]):
    c = int(c)
    if i % 2 == 0:
        expanded.append([str(idx)] * c)
        idx += 1
    else:
        expanded.append(['.'] * c)
defragmented = deepcopy(expanded)
def calculate_free_space(block: list[str]) -> tuple[int, int]:
    len = 0
    max_len = 0
    max_idx = 0
    if not block:
        return -1, -1
    for i, c in enumerate(block):
        if c == '.':
            len += 1
        else:
            if len > max_len:
                max_len = len
                max_idx = i - max_len
            len = 0
    if len > max_len:
        max_len = len
        max_idx = i - max_len + 1
    return max_len, max_idx

for i, block in enumerate(expanded[::-1]):
    print(i + 1, len(expanded))
    if (len(expanded) - i - 1) % 2 == 0:
        free_idx = 0
        out_of_bounds = False
        free_space = -1
        free_subidx = -1
        while True:
            free_space, free_subidx = calculate_free_space(defragmented[free_idx])
            if free_space >= len(block):
                break
            free_idx += 1
            if free_idx >= len(defragmented) - 1:
                out_of_bounds = True
                break
        if out_of_bounds:
            continue
        if free_idx >= len(defragmented) - 1 - i:
            continue
        defragmented[free_idx][free_subidx:free_subidx + len(block)] = block
        defragmented[len(defragmented) - 1 - i] = ['.'] * (len(block))
flattened = []
for block in defragmented:
    flattened.extend(block)
t = 0
for i in range(len(flattened)):
    if flattened[i] == '.':
        continue
    else:
        t += int(flattened[i]) * i
print(t)
