#!/usr/bin/env pypy3
# not using gcd lol still works thanks eric
import itertools
full_grid=list(map(list,open(0).read().splitlines()))
distincts=set()
def iter_all(full_grid):
    for _, r in enumerate(full_grid):
        for _, c in enumerate(r):
            yield c
for c in iter_all(full_grid):
    distincts.add(c)
distincts.remove('.')
grids=[]
for d in distincts:
    grids.append(([], d))
    for i, r in enumerate(full_grid):
        grids[-1][0].append([])
        for j, c in enumerate(r):
            if c in '.' + d:
                grids[-1][0][-1].append(c)
            else:
                grids[-1][0][-1].append('.')
def count_antinodes(grid, d) -> set[tuple[int, int]]:
    positions = []
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == d:
                positions.append((i, j))
    antis = set()
    for a1, a2 in itertools.combinations(positions, 2):
        di = a2[0] - a1[0]
        dj = a2[1] - a1[1]
        anti1i = a2[0] - di
        anti1j = a2[1] - dj
        while True:
            anti1i += di
            anti1j += dj
            if 0 <= anti1i <= len(grid) - 1 and 0 <= anti1j <= len(grid[0]) - 1:
                antis.add((anti1i, anti1j))
            else:
                break
        anti2i = a1[0] + di
        anti2j = a1[1] + dj
        while True:
            anti2i -= di
            anti2j -= dj
            if 0 <= anti2i <= len(grid) - 1 and 0 <= anti2j <= len(grid[0]) - 1:
                antis.add((anti2i, anti2j))
            else:
                break
    return antis
# anti_positions = [(x[0], x[1]) for x in all_antis]
# for i, r in enumerate(full_grid):
#     for j, c in enumerate(r):
#         if (i, j) in anti_positions:
#             print(end='#')
#         else:
#             print(end=c)
#     print()
all_antis = set()
for grid_pair in grids:
    grid, d = grid_pair
    antis = count_antinodes(grid, d)
    all_antis = all_antis | antis
print(len(all_antis))
