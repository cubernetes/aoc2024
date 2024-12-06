#!/usr/bin/env pypy3
import sys
from copy import deepcopy
e=enumerate
grid = list(map(list, open(sys.argv[1]).read().strip().splitlines()))
guard_turns={'^':'>','>':'v','v':'<','<':'^'}
dir_deltas={'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
def find_guard(grid: list[list[str]]) -> tuple[int, int, str]:
    for i, r in e(grid):
        for j, c in e(r):
            if c in guard_turns:
                return i, j, c
    assert False
def out_of_bounds(grid: list[list[str]], i: int, j: int) -> bool:
    if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1:
        return False
    return True
def update(grid: list[list[str]], i: int, j: int, dir: str) -> tuple[int, int, str, bool]:
    di, dj = dir_deltas[dir]
    ni = i + di
    nj = j + dj
    if out_of_bounds(grid, ni, nj):
        return 0, 0, '', True
    elif grid[ni][nj] == '#':
        grid[i][j] = guard_turns[dir]
        return i, j, guard_turns[dir], False
    elif grid[ni][nj] == '.':
        grid[i][j] = '.'
        grid[ni][nj] = dir
        return ni, nj, dir, False
    else:
        assert False
def simulation_steps(grid: list[list[str]], visited: set = set()) -> int:
    if not visited:
        visited.add(find_guard(grid))
    i, j, dir = next(iter(visited))
    while True:
        i, j, dir, bounds_error = update(grid, i, j, dir)
        if bounds_error:
            return len(set(map(lambda state: (state[0], state[1]), visited)))
        state = (i, j, dir)
        if state in visited:
            return 0
        visited.add((i, j, dir))
print(simulation_steps(grid))
