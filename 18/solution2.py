#!/usr/bin/env pypy3

W=H=70
g=[['.' for _ in range(W+1)] for _ in range(H+1)]
bytes_=list(open(0).read().splitlines())
def make_em_fall(n) -> tuple[int,int]:
    for _ in range(n):
        line=bytes_.pop(0)
        x,y=line.split(',')
        x=int(x)
        y=int(y)
        g[y][x]='#'
    return x,y
def print_path(seen:dict[tuple[int,int], tuple[int,int,int]]) -> None:
    path=set()
    parent=seen[(W,H)]
    path.add((W,H))
    while True:
        path.add((parent[0],parent[1]))
        if (parent[0],parent[1]) in seen and (parent[0],parent[1]) != (0,0):
            parent=seen[(parent[0],parent[1])]
        else:
            break
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if (x,y) in path:
                print(end=f'\x1b\x5b41;30mO\x1b\x5bm')
            else:
                print(end=c)
        print()
def bfs(x:int,y:int,ex:int,ey:int,seen:dict[tuple[int,int], tuple[int,int,int]]) -> int:
    frontier: list[tuple[int,int,int]]=[(x,y,0)]
    while frontier:
        x,y,d=frontier.pop(0)
        for dx,dy in [(-1,0),(+1,0),(0,1),(0,-1)]:
            if (x+dx,y+dy) in seen or not (0 <= y+dy < len(g) and 0 <= x+dx < len(g[0])):
                continue
            elif g[y+dy][x+dx] == '#':
                continue
            seen[(x+dx,y+dy)] = (x,y,d+1)
            if (x+dx,y+dy) == (ex,ey):
                return d+1
            frontier.append((x+dx,y+dy,d+1))
    return -1
make_em_fall(1024)
while bfs(0,0,W,H,(seen:={})) != -1:
    x,y=make_em_fall(1)
print(x,y)
