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

R, U = open(0).read().strip().split('\n\n')
R = R.splitlines()
U = U.splitlines()

rules = defaultdict(list)
for line in R:
    left, right = line.split('|')
    rules[left].append(right)

incorrect_updates = []
for u in U:
    u = u.split(',')
    correct = True
    breaking_rules = []
    for i, left_n in e(u):
        left_i = u.index(left_n)
        if left_n not in rules:
            continue
        for right_n in rules[left_n]:
            if right_n not in u:
                continue
            right_i = u.index(right_n)
            if left_i > right_i:
                breaking_rules.append((left_n, right_n))
                correct = False
    if not correct:
        incorrect_updates.append((u, breaking_rules))

t = 0
for u, breaking_rules in incorrect_updates:
    _sorted = False
    while not _sorted:
        _sorted = True
        for rule in R:
            rule = rule.split('|')
            if rule[0] in u and rule[1] in u:
                if u.index(rule[0]) > u.index(rule[1]):
                    print()
                    print(breaking_rules)
                    print(u)
                    print('swapping', rule[0], 'and', rule[1])
                    u[u.index(rule[0])], u[u.index(rule[1])] = u[u.index(rule[1])], u[u.index(rule[0])]
                    print(u)
                    print()
                    _sorted = False
    t += int(u[len(u) // 2])
print(t)
