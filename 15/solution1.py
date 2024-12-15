#!/usr/bin/env pypy3

G,M=open(0).read().strip().split('\n\n')
G=list(map(list,G.splitlines()))
M=''.join(M.splitlines())
dirs={'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}
def update(m):
    global r,c,G
    dr,dc=dirs[m]
    nr,nc=r+dr,c+dc
    if G[nr][nc]=='.':
        G[r][c]='.'
        r=nr
        c=nc
        G[r][c]='@'
    elif G[nr][nc]=='#':
        return;
    elif G[nr][nc]=='O':
        br,bc=nr,nc
        while G[br][bc]=='O':
            br+=dr
            bc+=dc
        if G[br][bc]=='.':
            G[br][bc] = 'O'
            while G[br][bc] != '@':
                br-=dr # THERE'S A BUG HERE FIX LATER
                bc-=dc
            G[br][bc] = '.'
            r=br+dr
            c=bc+dc
            G[r][c] = '@'
        elif G[br][bc]=='#':
            return;

c=r=-1
for i,r_ in enumerate(G):
    for j,c_ in enumerate(r_):
        if c_=='@':
            r=i
            c=j
            break
    else:
        continue
    break
for m in M:
    update(m)
for r_ in G:
    line=''.join(r_)
    print(line)
t=0
for i, r_ in enumerate(G):
    for j, c_ in enumerate(r_):
        if c_=='O':
            t+=i*100 + j
print(t)
