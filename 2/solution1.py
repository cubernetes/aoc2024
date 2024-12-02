#!/usr/bin/env python3

e=enumerate

data = open(0).read().strip().splitlines()
t = 0
for line in data:
    nums = list(map(int, line.split()))
    prev = -1
    inc = True
    diff = 0
    safe = True
    first = True
    for num in nums:
        if prev != -1:
            if num - prev > 0:
                if first:
                    inc = True
                elif inc == False:
                    safe = False
                    break
                first = False
                diff = num - prev
                if diff not in [1, 2, 3]:
                    safe = False
                    break
            else:
                if first:
                    inc = False
                elif inc == True:
                    safe = False
                    break
                first = False
                diff = prev - num
                if diff not in [1, 2, 3]:
                    safe = False
                    break
        prev = num
    if safe:
        t += 1
print(t)
