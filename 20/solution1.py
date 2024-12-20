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

def bfs(i,j,seen):
    queue=[(i,j,0)]
    seen[(i,j)] = 0
    while queue:
        i,j,d = queue.pop(0)
        if g[i][j]=='E':
            return d
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

def get_savings(_i,_j,seen,legit_time,seen_internal={}):
    queue=[(_i,_j,0)]
    seen_internal[(_i,_j)] = 0
    while queue:
        i,j,d = queue.pop(0)
        if (i,j) in seen:
            # if (_i,_j) == (9,2):
            #     print(f'seen[(i,j)] == {seen[(i,j)]}')
            #     print(f'legit_time == {legit_time}')
            return seen[(i,j)]-legit_time-2 # + 1
        assert g[i][j]!='E' # E position should be in seen
        for di,dj in [(-1,0), (+1,0), (0,1), (0,-1)]:
            ni,nj=i+di,j+dj
            if not (0 <= ni < len(g) and 0 <= nj < len(g[0])):
                continue
            elif g[ni][nj] == '#':
                continue
            elif (ni,nj) in seen_internal:
                continue
            seen_internal[(ni,nj)] = d+1
            queue.append((ni,nj,d+1))

def find_cheats(i,j,seen,cheats,seen_internal={}):
    queue=[(i,j,0)]
    seen_internal[(i,j)] = 0
    while queue:
        i,j,d = queue.pop(0)
        if g[i][j]=='E':
            return
        for di,dj in [(-1,0), (+1,0), (0,1), (0,-1)]:
            ni,nj=i+di,j+dj
            if not (0 <= ni < len(g) and 0 <= nj < len(g[0])):
                continue
            if g[ni][nj] == '#':
                if 0 <= ni+di < len(g) and 0 <= nj+dj < len(g[0]):
                    if g[ni+di][nj+dj] in '.E' and (ni+di,nj+dj) not in seen_internal: # technically not correct, you can also go in diagonals
                        cheats[((ni,nj),(ni+di,nj+dj))] = get_savings(ni+di,nj+dj,seen,seen[(i,j)])
                continue
            elif (ni,nj) in seen_internal:
                continue
            seen_internal[(ni,nj)] = d+1
            queue.append((ni,nj,d+1))

def print_cheat(cheat,d):
    print(d)
    for i,r in enumerate(g):
        for j,c in enumerate(r):
            if (i,j) == cheat[0]:
                print(end=f'\x1b\x5b42;30m1\x1b\x5bm')
            elif (i,j) == cheat[1]:
                print(end=f'\x1b\x5b41;30m2\x1b\x5bm')
            else:
                print(end=c)
        print()

def print_cheats(cheats):
    for cheat,d in cheats.items():
        print_cheat(cheat,d)

seen={}
min_legit_time = bfs(i,j,seen)

cheats={}
find_cheats(i,j,seen,cheats)

cheats=dict(sorted(cheats.items(), key=lambda tup: tup[1]))
# print(cheats)
# print_cheats(cheats)

t=0
for cheat,savings in cheats.items():
    if savings >= 100:
        # print(cheat, savings)
        t+=1
print(t)
