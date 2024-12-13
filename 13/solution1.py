#!/usr/bin/env pypy3

import itertools as it

machines = open(0).read().split("\n\n")

def bruh_idk_itertools(A,B):
    for a in range(A):
        for b in range(B):
            yield a,b

def min_btn_presses(bax, bay, bbx, bby, px, py):
    for a, b in sorted(bruh_idk_itertools(100, 100), key=lambda tup: sum(tup)):
        if bax * a + bbx * b == px:
            if bay * a + bby * b == py:
                return a*3 + b
    return 0

t = 0
for machine in machines:
    ba, bb, p = machine.splitlines()
    bax, bay = [int(off[2:]) for off in ba.removeprefix("Button A: ").split(", ")]
    bbx, bby = [int(off[2:]) for off in bb.removeprefix("Button B: ").split(", ")]
    px, py =  [int(pos[2:]) for pos in p.removeprefix("Prize: ").split(", ")]
    t += min_btn_presses(bax, bay, bbx, bby, px, py)
print(t)
