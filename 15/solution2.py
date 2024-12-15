#!/usr/bin/env pypy3

import sys

G__,M=open(0).read().strip().split('\n\n')
G_=list(map(list,G__.splitlines()))
G=[]
def print_warehouse():
    global G
    for r_ in G:
        line=''.join(r_)
        print(line)
for r_ in range(len(G_)):
    G.append([])
    for c_ in range(len(G_[r_])):
        if G_[r_][c_] == '.':
            G[-1].append('.')
            G[-1].append('.')
        elif G_[r_][c_] == '#':
            G[-1].append('#')
            G[-1].append('#')
        elif G_[r_][c_] == 'O':
            G[-1].append('[')
            G[-1].append(']')
        elif G_[r_][c_] == '@':
            G[-1].append('@')
            G[-1].append('.')
        else:
            assert False
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
    elif dr==0: # going sideways
        if G[nr][nc] in '[]':
            is_left_bracket=G[nr][nc]=='\x5b'
            br,bc=nr,nc
            while G[br][bc] in '[]':
                br+=dr
                bc+=dc
            if G[br][bc]=='.':
                G[br][bc] = '\x5d' if is_left_bracket else '\x5b' # escaping needed to calm down my editor
                idx=0
                while True:
                    br-=dr
                    bc-=dc
                    if G[br][bc] == '@':
                        break
                    if idx%2==0:
                        G[br][bc]='\x5b' if is_left_bracket else '\x5d'
                    else:
                        G[br][bc]='\x5d' if is_left_bracket else '\x5b' # this wrongly places a '['/']' on the last iter
                    idx+=1
                G[br][bc] = '.'
                r=br+dr
                c=bc+dc
                G[r][c] = '@' # this overwrites the wrongly placed '['/']'
            elif G[br][bc]=='#':
                return;
        else:
            assert False
    elif dc==0: # going up
        if G[nr][nc] in '[]':
            if G[nr][nc] == '[':
                frontier=[(nr,nc),(nr,nc+1)]
            elif G[nr][nc] == ']':
                frontier=[(nr,nc),(nr,nc-1)]
            else:
                assert False
            idx=0
            while idx<len(frontier):
                first=frontier[idx]
                idx+=1
                br,bc=first
                if G[br+dr][bc+dc]=='.': # this front does not move other boxes
                    continue
                elif G[br+dr][bc+dc] == '[' and (br+dr,bc+dc) not in frontier:
                    frontier.append((br+dr,bc+dc))
                    frontier.append((br+dr,bc+dc+1))
                elif G[br+dr][bc+dc] == ']' and (br+dr,bc+dc) not in frontier:
                    frontier.append((br+dr,bc+dc))
                    frontier.append((br+dr,bc+dc-1))
                elif G[br+dr][bc+dc]=='#':
                    break # this way, we will not go into the while's else clause, effectively doing nothing
            else:
                for front in frontier[::-1]:
                    br,bc=front
                    G[br+dr][bc+dc]=G[br][bc]
                    G[br][bc]='.'
                G[r+dr][c+dc]='@'
                G[r][c]='.'
                r+=dr
                c+=dc
        else:
            assert False
    else:
        assert False

r=-1
c=-1
for i,r_ in enumerate(G):
    for j,c_ in enumerate(r_):
        if c_=='@':
            r=i
            c=j
            break
    else:
        continue
    break
for i,m in enumerate(M):
    update(m)
t=0
for i, r_ in enumerate(G):
    for j, c_ in enumerate(r_):
        if c_=='\x5b':
            t+=i*100 + j
print_warehouse()
print(t)
