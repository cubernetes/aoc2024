#!/usr/bin/env pypy3

g=list(map(list,open(0).read().splitlines()))

i=j=-1
for i,r in enumerate(g):
    for j,c in enumerate(r):
        if c=='S':
            break
    else:
        continue
    break
assert i!=-1
assert j!=-1

def bfs_flood(i,j,seen):
    queue=[(i,j,0)]
    seen[(i,j)] = 0
    while queue:
        i,j,d = queue.pop(0)
        for di,dj in [(-1,0), (+1,0), (0,1), (0,-1)]:
            ni,nj=i+di,j+dj
            if not (0 <= ni < len(g) and 0 <= nj < len(g[0])):
                continue
            elif g[ni][nj] == '#':
                continue
            elif (ni,nj) in seen:
                continue
            seen[(ni,nj)] = d+1
            queue.append((ni,nj,d+1))

def cheat_20(i,j,legit_time,seen,seen_external,cheats):
    for (si, sj), d in seen.items():
        if (si, sj) not in seen_external:
            taxicab=abs(i-si) + abs(j-sj)
            if taxicab <= 20:
                cheats[((i,j),(si,sj))] = d - legit_time - taxicab

def bfs_20(i,j,seen,cheats,seen_internal={}):
    queue=[(i,j,0)]
    seen_internal[(i,j)] = 0
    idx=-1
    while queue:
        idx += 1
        print(idx, len(seen))
        i,j,d = queue.pop(0)
        if g[i][j]=='E':
            return
        cheat_20(i,j,d,seen,seen_internal,cheats)
        for di,dj in [(-1,0), (+1,0), (0,1), (0,-1)]:
            ni,nj=i+di,j+dj
            if not (0 <= ni < len(g) and 0 <= nj < len(g[0])):
                continue
            if g[ni][nj] == '#':
                continue
            elif (ni,nj) in seen_internal:
                continue
            seen_internal[(ni,nj)] = d+1
            queue.append((ni,nj,d+1))

seen={}
bfs_flood(i,j,seen)

cheats={}
bfs_20(i,j,seen,cheats)

print("Sorting (takes a bit)")
cheats=dict(sorted(cheats.items(), key=lambda tup: tup[1]))
t=0
print("Counting savings")
for cheat, savings in cheats.items():
    if savings >= 100:
        t+=1
print(t)
