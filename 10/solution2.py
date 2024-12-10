#!/usr/bin/env pypy3
e=enumerate
G=list(map(lambda x: [-1]+list(map(int,x))+[-1],open(0).read().splitlines()))
G=[[-1]*len(G[0])]+G+[[-1]*len(G[0])]
def dfs(i,j,h,seen9=set())->int:
    D=[(-1,0),(+1,0),(0,-1),(0,+1)]
    if h==9:
        return 1
    rating=0
    for d in D:
        di,dj=d
        if G[i+di][j+dj]==h+1:
            rating+=dfs(i+di,j+dj,h+1,seen9)
    return rating
total=0
for i in range(len(G)):
    for j in range(len(G)):
        if G[i][j]==0:
            total+=dfs(i,j,0,(s:=set()))
print(total)
