#!/usr/bin/env pypy3
lines = list(map(lambda x:x.split(": "), open(0).read().splitlines()))
A = []
for line in lines:
    res, nums = line
    res = int(res)
    nums = nums.split()
    for i in range(2 ** (len(nums) - 1)):
        ops = list(bin(i)[2:].zfill(len(nums) - 1).replace("1", "+").replace("0", "*"))
        ops = ["+"] + ops
        s = ''
        evaled = 0
        for num, op in zip(nums, ops):
            num = int(num)
            if op == '+':
                evaled += num
            elif op == '*':
                evaled *= num
            else:
                assert False
            s += op + str(num)
        if evaled == res:
            A.append([res])
            break
s = 0
for a in A:
    s += sum(a)
print(s)
