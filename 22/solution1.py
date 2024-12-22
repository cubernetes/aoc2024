#!/usr/bin/env pypy3

def next_sn_n(s, n):
    for _ in range(n):
        s1 = s * 64
        s = s ^ s1 % 2**24
        s1 = s // 32
        s = s ^ s1 % s**24
        s1 = s * 2048
        s = s ^ s1 % 2**24
    return s

t=0
for sn in open(0).read().splitlines():
    s = next_sn_n(int(sn), 2000)
    t+=s
print(t)
