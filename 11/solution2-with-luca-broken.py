#!/usr/bin/env pypy3

import json
from copy import deepcopy

stones=input().split()

cache: dict[tuple[str,int], list[str]]={}

def blink(stone: str) -> list[str]:
    if stone=="0":
        expanded=['1']
    elif len(stone)%2==0:
        expanded=[stone[:len(stone)//2], str(int(stone[len(stone)//2:]))]
    else:
        expanded=[str(int(stone) * 2024)]
    return expanded

def get_max_blink(blink_stone: tuple[str, int], N: int) -> list[tuple[str, int]]:
    global cache
    stone, level = blink_stone
    for i in range(N - blink_stone[1], 1, -1):
        # print(f'{stone=}, {i=}, {blink_stone=}')
        if (stone, i) in cache:
            # print(f"FOUND IN CACHE {cache[(stone, i)]=}, {stone=}, {i=}, {blink_stone=}")
            return [(stone, i + level) for stone in cache[(stone, i)]]
    # print()
    stones = blink(stone)

    cache_add={}
    for (s, l), ss in cache.items():
        if ss == [stone]:
            cache_add[(s, l+1)] = stones
            #break?
    cache |= cache_add

    if (stone, level) in cache:
        cache[(stone, level + 1)] = stones
    else:
        cache[(stone, 1)] = stones
    # print('cache', cache)
    return [(s, level + 1) for s in stones]

def cache_update() -> None:
    global cache
    cache_add={}
    for (stone, level), stones in cache.items():
        tmp_stones=[]
        for s in stones:
            if (s, 1) not in cache:
                break
            tmp_stones.extend(cache[(s, 1)])
        else:
            cache_add[(stone, level+1)] = tmp_stones
    cache |= cache_add

def blink_n(blink_stones: list[tuple[str, int]], N: int) -> list[str]:
    i = 0
    while True:
        new_blink_stones=[]
        # print(blink_stones)
        for blink_stone in blink_stones:
            if blink_stone[1] >= N:
                new_blink_stones.append(blink_stone)
                continue
            new_blink_stones.extend(get_max_blink(blink_stone, N))
        # print()
        cache_update()
        blink_stones=new_blink_stones
        # print(blink_stones)
        if all([level==N for _, level in blink_stones]):
            return [stone for stone, _ in blink_stones]
        print(sorted(cache, key=lambda tup: tup[1])[-1])
        print(len(cache))
        print(i, len(blink_stones))
        i+=1

print(len(blink_n([('0', 0)], 50)))

# GOAL: 10
#0#[0:0]
#1#[1:1]             | (0,1):[1]
#2#[2024:2]          | (0,1):[1], (0,2):[2024], (1,1):[2024]
#3#[20:3 24:3]       | (0,1):[1], (0,2):[2024], (0,3):[20 24], (1,1):[2024]
#4#[2:4 0:4 2:4 4:4] | (0,1):[1], (0,2):[2024], (0,3):[20 24], (20,1):[2 0], (24,1):[2 4]
