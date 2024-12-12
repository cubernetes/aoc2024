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
reverse_dir={(-1,0):(+1,0),(+1,0):(-1,0),(0,-1):(0,+1),(0,+1):(0,-1)}
def adjust(face: tuple[int,int], side: tuple[int,int]) -> tuple[int,int]:
    i,j=face
    if side == (-1,0):
        return i-1,j
    elif side == (+1,0):
        return i+1,j
    elif side == (0,-1):
        return i,j-1
    elif side == (0,+1):
        return i,j+1
    else:
        assert False
def remove_facing_faces(sides: dict[tuple[int,int], list[tuple[int,int]]]):
    for _ in D:
        for side in D:
            faces=sides[side]
            for face in faces:
                aface = adjust(face, side)
                if aface in sides[reverse_dir[side]]:
                    sides[side].remove(face)
                    sides[reverse_dir[side]].remove(aface)
turn_clock_wise={(-1,0):(0,1), (0,1):(+1,0), (+1,0):(0,-1), (0,-1):(-1,0)}
def calc_price(region: set[tuple[int,int]]) -> int:
    area=0
    n_sides=0
    for i,j in region:
        area+=1
        for d in D:
            di,dj=d
            ni,nj=i+di,j+dj
            cdi,cdj=turn_clock_wise[(di,dj)]
            cni,cnj=i+cdi,j+cdj
            if (ni,nj) not in region and (cni,cnj) not in region:
                n_sides += 1
            elif (ni,nj) in region and (cni,cnj) in region and (ni+cdi,nj+cdj) not in region:
                n_sides += 1
    return area*n_sides
t=0
for s in list(seen_sets):
    t+=calc_price(s)
print(t)
