#!/usr/bin/env pypy3

import heapq
from collections import defaultdict

grid=list(map(list,open(0)))
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
#class Node:
#  def __init__(self,d,parent,finished,dir,x,y):
#      self.d=float('inf') #current distance from source node
#      self.parent=None
#      self.finished=False
#      self.dir = ''
#      self.x = -1
#      self.y = -1
#def dijkstra(grid, source):
#    nodes: dict[tuple[int,int,str], Node]={}
#    queue=[(0, source)]
#    while queue:
#        d, node=heapq.heappop(queue)
#        if nodes[node].finished:
#            continue
#        nodes[node].finished=True
#        for neigh in [(), ]:
#            if nodes[neigh].finished:
#                continue
#dijkstra(grid,(r,c,dir))
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
nodes=defaultdict(lambda:[False,None,float('inf')])
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
        if new_cost<nodes[n][2]:
            nodes[n][2]=new_cost
            nodes[n][1]=(r,c,dir)
            heapq.heappush(queue,(new_cost,nr,nc,ndir))
print(sorted([nodes[(er,ec,'>')], nodes[(er,ec,'<')], nodes[(er,ec,'^')], nodes[(er,ec,'v')]], key=lambda tup: tup[2])[0])
