#!/usr/bin/env pypy3

expanded = []
idx = 0
for i, c in enumerate(open(0).read().strip().splitlines()[0]):
    c = int(c)
    if i % 2 == 0:
        expanded.extend([str(idx)] * c)
        idx += 1
    else:
        expanded.extend(list(c * '.'))
defragmented = expanded[:]
print(defragmented)
free_idx = 0
for i in range(len(defragmented)):
    if defragmented[-1 - i] == '.':
        continue
    out_of_bounds = False
    while defragmented[free_idx] != '.':
        free_idx += 1
        if free_idx >= len(defragmented) - 1 or free_idx >= len(defragmented) - i - 1:
            out_of_bounds = True
            break
    if out_of_bounds:
        break
    defragmented[free_idx], defragmented[-1 - i] = defragmented[-1 - i], defragmented[free_idx]
t = 0
for i, c in enumerate(defragmented):
    if c == '.':
        break
    t += int(c) * i
print(t)
