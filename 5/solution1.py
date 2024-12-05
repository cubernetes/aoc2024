#!/usr/bin/env python3

print()

import os
import re
import sys
import math
import multiprocessing as mp
from copy import copy, deepcopy
from typing import Any
import numpy as np
import more_itertools as miter
from functools import cache, lru_cache, reduce
from collections import deque, defaultdict, Counter
from itertools import (
    repeat, cycle, combinations, combinations_with_replacement,
    permutations, tee, pairwise, zip_longest, islice, takewhile,
    filterfalse, starmap
)
e=enumerate

O, U = open(0).read().strip().split('\n\n')
O = O.splitlines()
U = U.splitlines()

rules = defaultdict(list)
for line in O:
    left, right = line.split('|')
    rules[left].append(right)

correct_updates = []
for u in U:
    u = u.split(',')
    correct = True
    for i, left_n in e(u):
        left_i = u.index(left_n)
        if left_n not in rules:
            # correct = False
            continue
        for right_n in rules[left_n]:
            if right_n not in u:
                # correct = False
                continue
            right_i = u.index(right_n)
            if left_i > right_i:
                correct = False
    if correct:
        correct_updates.append(u)

t = 0
for u in correct_updates:
    t += int(u[len(u) // 2])
print(t)
