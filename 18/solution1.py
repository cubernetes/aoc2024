#!/usr/bin/env pypy3

W=H=70
g=[['.' for _ in range(W+1)] for _ in range(H+1)]
for line in list(open(0).read().splitlines())[:1024]:
    x,y=line.split(',')
    x=int(x)
    y=int(y)
    g[y][x]='#'
def bfs(x,y,ex,ey,seen=set()):
    f=[(x,y,0)]
    while f:
        x,y,d=f.pop(0)
        for dx,dy in [(-1,0),(+1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if (nx,ny) in seen or not (0 <= ny < len(g) and 0 <= nx < len(g[0])):
                continue
            elif g[ny][nx] == '#':
                continue
            seen[(nx,ny)] = (x,y,d+1)
            if (nx,ny) == (ex,ey):
                return d+1
            f.append((nx,ny,d+1))
    return -1
print(bfs(0,0,W,H))
