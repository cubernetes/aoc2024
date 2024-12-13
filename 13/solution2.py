#!/usr/bin/env pypy3

#I 94 * a + 22 * b == 8400
#II 34 * a + 67 * b == 5400

# Solve II for a
# 34 * a == 5400 - 67 * b
#III a == (5400 - 67 * b) / 34

# Substitute a in I and solve for b
# 94 * (5400 - 67 * b) / 34 + 22 * b == 8400
# (94 * 5400 - 94 * 67 * b) / 34 + 22 * b == 8400
# 94 * 5400 - 94 * 67 * b + 22 * b * 34 == 8400 * 34
# -94 * 67 * b + 22 * b * 34 == 8400 * 34 - 94 * 5400
# b * (-94 * 67 + 22 * 34) == 8400 * 34 - 94 * 5400
# b == 8400 * 34 - 94 * 5400 / (-94 * 67 + 22 * 34)
# b == px * bay - bax * py / (-bax * bby + bbx * bay)

# Substitue b in III
# a == (5400 - 67 * b) / 34

def min_btn_presses(bax, bay, bbx, bby, px, py):
    px += 10000000000000
    py += 10000000000000
    denom = -bax * bby + bbx * bay
    if denom == 0:
        return 0
    b = (px * bay - bax * py) / denom
    a = (py - bby * b) / bay
    if int(a) == a and int(b) == b: # this IS the minimum, since it's the only solution
        return int(a*3+b)
    return 0

machines = open(0).read().split("\n\n")
t = 0
for machine in machines:
    ba, bb, p = machine.splitlines()
    bax, bay = [int(off[2:]) for off in ba.removeprefix("Button A: ").split(", ")]
    bbx, bby = [int(off[2:]) for off in bb.removeprefix("Button B: ").split(", ")]
    px, py =  [int(pos[2:]) for pos in p.removeprefix("Prize: ").split(", ")]
    t += min_btn_presses(bax, bay, bbx, bby, px, py)
print(t)
