#!/usr/bin/env pypy3

conns=[]
for conn in open(0):
    a,b=conn.strip().split('-')
    conns.append((a,b))
triplets=set()
def filter_a(conns,a):
    return [conn for conn in conns if conn[0]==a]
def filter_b(conns,b):
    return [conn for conn in conns if conn[1]==b]
for a,b in conns:
    for aa,bb in filter_a(conns,a):
        if (aa,bb)==(a,b): continue
        for aaa,bbb in filter_a(conns,bb):
            if (aaa,bbb)==(a,b): continue
            if (aaa,bbb)==(aa,bb): continue
            if bbb==b:
                triplets.add(tuple(sorted((a,b,bb))))
        for aaa,bbb in filter_b(conns,bb):
            if (aaa,bbb)==(a,b): continue
            if (aaa,bbb)==(aa,bb): continue
            if aaa==b:
                triplets.add(tuple(sorted((a,b,bb))))
    for aa,bb in filter_b(conns,a):
        if (aa,bb)==(a,b): continue
        for aaa,bbb in filter_a(conns,aa):
            if bbb==b:
                triplets.add(tuple(sorted((a,b,aa))))
        for aaa,bbb in filter_b(conns,aa):
            if aaa==b:
                triplets.add(tuple(sorted((a,b,aa))))
t=0
for trip in triplets:
    a,b,c=trip
    if a[0]=='t' or b[0]=='t' or c[0]=='t':
        t+=1
        print(a,b,c)
print(t)
