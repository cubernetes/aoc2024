#!/usr/bin/env pypy3
lines = list(map(lambda x:x.split(": "), open(0).read().splitlines()))
A = []
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))
for line in lines:
    res, nums = line
    res = int(res)
    nums = nums.split()
    for i in range(3 ** (len(nums) - 1)):
        ops = list(ternary(i).zfill(len(nums) - 1).replace("1", "+").replace("0", "*").replace("2", "|"))
        ops = ["+"] + ops
        s = ''
        evaled = 0
        prev_op = ''
        prev_num = 0
        for num, op in zip(nums, ops):
            num = int(num)
            if op == '+':
                evaled += num
            elif op == '*':
                evaled *= num
            elif op == '|' and prev_op == '':
                assert False
            elif op == '|':
                evaled = int(f'{evaled}{num}')
            else:
                assert False
            prev_op = op
            prev_num = num
            s += op + str(num)
        if evaled == res:
            A.append([res])
            break
s = 0
for a in A:
    s += sum(a)
print(s)
