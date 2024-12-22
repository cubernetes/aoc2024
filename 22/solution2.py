#!/usr/bin/env pypy3

import numpy as np
from collections import defaultdict

def next_sn_n(s, n):
    yield s
    for _ in range(n):
        s1 = s * 64
        s = s ^ s1 % 2**24
        s1 = s // 32
        s = s ^ s1 % s**24
        s1 = s * 2048
        s = s ^ s1 % 2**24
        yield s

monkey=defaultdict(int)
lines=open(0).read().splitlines()
for idx,sn in enumerate(lines):
    print(idx+1, len(lines))
    s = list(next_sn_n(int(sn), 2000))
    d = [int(n) for n in np.diff(list(map(lambda x:x%10, s)))]
    i = 0
    seen=set()
    while i+4<len(s):
        t=tuple(d[i:i+4])
        if t in seen:
            i+=1
            continue
        seen.add(t)
        monkey[t] += s[i+4] % 10
        i+=1
print(sorted(monkey.items(), key=lambda tup:tup[1],reverse=True)[0])
