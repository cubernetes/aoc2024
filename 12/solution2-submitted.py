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
def calc_price(region: set[tuple[int,int]]) -> int:
    area=0
    sides={}
    for d in D:
        sides[d]=[]
    for i,j in region:
        area+=1
        for d in D:
            sides[d].append((i,j))
    remove_facing_faces(sides)
    n_sides = 0
    for side,faces in sides.items():
        side_local=0
        line_regions=[]
        prev=-1
        vertical=side in [(-1,0), (+1,0)]
        for i,j in sorted(faces, key=lambda tup: tup[0] if vertical else tup[1]):
            if (i if vertical else j) != prev:
                prev = (i if vertical else j)
                line_regions.append([])
            line_regions[-1].append((i,j))
        for line_region in line_regions:
            prev = -2
            local=0
            for i,j in sorted(line_region, key=lambda tup: tup[1] if vertical else tup[0]):
                if (j if vertical else i) > prev + 1:
                    local += 1
                prev = j if vertical else i
            side_local += local
        n_sides += side_local
    return area*n_sides
t=0
for s in seen_sets:
    t+=calc_price(s)
print(t)
