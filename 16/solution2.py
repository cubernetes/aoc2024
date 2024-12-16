#!/usr/bin/env pypy3

import heapq
from collections import defaultdict, deque

grid=list(map(list,open(0).read().splitlines()))
r=c=-1
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            break
    else:
        continue
    break
er=ec=-1
for er, row in enumerate(grid):
    for ec, cell in enumerate(row):
        if cell == 'E':
            break
    else:
        continue
    break
if r==-1 or c==-1:
    assert False
dir='>'
turn_left={'>':'^', '^':'<', '<':'v', 'v':'>'}
turn_right={'>':'v', 'v':'<', '<':'^', '^':'>'}
forward={'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
def get_neighbors(grid:list[list[str]],r:int,c:int,dir:str) -> list[tuple[int,int,int,str]]:
    ret = [
        (1000,r,c,turn_left[dir]),
        (1000,r,c,turn_right[dir]),
        (2000,r,c,turn_right[turn_right[dir]])
    ]
    if grid[r+forward[dir][0]][c+forward[dir][1]] != '#':
        ret.append((1,r+forward[dir][0],c+forward[dir][1],dir))
    return ret
queue=[(0,r,c,dir)]
nodes=defaultdict(lambda:[False,[],float('inf')])
while queue:
    d,r,c,dir=heapq.heappop(queue)
    if nodes[(r,c,dir)][0]:
        continue
    nodes[(r,c,dir)][0] = True
    for neigh in get_neighbors(grid,r,c,dir):
        cost,nr,nc,ndir=neigh
        n=(nr,nc,ndir)
        if nodes[n][0]:
            continue
        new_cost=d+cost
        if new_cost<=nodes[n][2]:
            nodes[n][2]=new_cost
            nodes[n][1].append((r,c,dir))
            heapq.heappush(queue,(new_cost,nr,nc,ndir))
def print_path(grid, nodes, end):
    node=nodes[end]
    best_path_nodes=set()
    best_path_nodes.add((end[0], end[1]))
    parents=deque(node[1][:])
    while parents:
        parent=parents.popleft()
        best_path_nodes.add((parent[0], parent[1]))
        parents += nodes[parent][1]
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if (i,j) in best_path_nodes:
                print(end='O')
            else:
                print(end=c)
        print()
    print(len(best_path_nodes))

shortest_path_end=sorted((((er,ec,dir),nodes[(er,ec,dir)]) for dir in forward), key=lambda tup: tup[1][2])[0]
print_path(grid, nodes, shortest_path_end[0])
