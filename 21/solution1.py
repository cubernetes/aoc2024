numpad=[7,8,9,4,5,6,1,2,3,-1,0,10]
dirpad=[-1,0,10,3,2,1]
numpaths={}
dirpaths={}
for keypad,padpaths in ((numpad,numpaths),(dirpad,dirpaths)):
    bi=keypad.index(-1)
    for s in keypad:
        q=[s]
        padpaths[s,s]=[()]
        while q:
            c=q.pop(0)
            i=keypad.index(c)
            for dir,dir2 in ((3,2),(-3,0),(1,1),(-1,3)):
                ni=i+dir
                if ((abs(dir)==3 and 0<=ni<len(keypad)) or (ni//3==i//3)) and ni!=bi:
                    nc=keypad[ni]
                    if (s,nc) in padpaths and len(padpaths[s,nc][0])<len(padpaths[s,c][0])+1:
                        continue
                    if (s,nc) not in padpaths:
                        padpaths[s,nc]=[]
                    for p in padpaths[s,c]:
                        if p+(dir2,) not in padpaths[s,nc]:
                            padpaths[s,nc].append(p+(dir2,))
                    q.append(nc)
def robo(c,n,d=-1,cache={}):
    if d==-1: d=n
    if (c,d) in cache: return cache[c,d]
    cache[c,d]=len(c) if d==0 else sum(min(robo(p+(10,),n,d-1,cache) for p in (numpaths if d==n else dirpaths)[s,e]) for s,e in zip((10,)+c,c))
    return cache[c,d]
print(sum(int(c[:-2]) * robo(tuple(int(x,16) for x in c[:-1]),3) for c in open(0)))
