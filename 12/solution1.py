#!/usr/bin/env pypy3

e=enumerate
D=[(-1,0),(+1,0),(0,-1),(0,+1)]
g=list(map(list,open(0).read().splitlines()))
current_type=g[0][0]
regions=[[]]
def bfs(i, j, seen=set()) -> None:
    global g, D
    t=g[i][j]
    if (i,j) in seen:
        return
    seen.add((i,j))
    neighs: list[tuple[int,int]]=list()
    for d in D:
        di,dj=d
        ni,nj=i+di,j+dj
        if 0 <= ni <= len(g)-1 and 0 <= nj <= len(g[0])-1:
            nt=g[ni][nj]
            if t==nt:
                neighs.append((ni,nj))
    for n in neighs:
        ni,nj=n
        bfs(ni,nj,seen)
seen_sets: list[set[tuple[int,int]]]=[]
for i,r in e(g):
    for j,c in e(r):
        for s in seen_sets:
            if (i,j) in s:
                break
        else:
            seen_sets.append(set())
            bfs(i,j,seen_sets[-1])
def calc_price(region: set[tuple[int,int]]) -> int:
    area=0
    perimeter=0
    for i,j in region:
        area+=1
        max_perim=4
        for d in D:
            di,dj=d
            ni,nj=i+di,j+dj
            if (ni,nj) in region:
                max_perim -= 1
        perimeter += max_perim
    return area*perimeter
t=0
for s in seen_sets:
    t+=calc_price(s)
print(t)
