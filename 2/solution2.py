#!/usr/bin/env python3

e=enumerate

data = open(0).read().strip().splitlines()
t = 0
for line in data:
    nums = list(map(int, line.split()))
    for i, num in e([-1] + nums):
        nums_copy = nums[:]
        if num != -1:
            nums_copy.pop(i - 1)
        prev = -1
        inc = True
        diff = 0
        first = True
        safe = True
        for num in nums_copy:
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
            break
    if safe:
        t += 1
print(t)
