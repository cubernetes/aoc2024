#!/usr/bin/env pypy3

import sys

WIDE=101
TALL=103

#WIDE=11
#TALL=7

def print_grid(robots) -> None:
    grid=[['.' for _ in range(WIDE)] for _ in range(TALL)]
    for robot in robots:
        x,y,_,_=robot
        if grid[y][x] == '.':
            grid[y][x]='1'
        else:
            if int(int(grid[y][x])+1) > 9:
                grid[y][x]=0 # means more than 9
            else:
                grid[y][x]=str(int(grid[y][x])+1)
    for row in grid:
        print(''.join(row))

def get_quad(px,py) -> int:
    if px<WIDE//2:
        if py<TALL//2:
            return 2
        elif py>TALL//2:
            return 3
    elif px>WIDE//2:
        if py<TALL//2:
            return 1
        elif py>TALL//2:
            return 4
    return 0

def update(px,py,vx,vy,n) -> tuple[int,int]:
    px+=vx*n
    py+=vy*n
    px%=WIDE
    py%=TALL
    return px,py

quad1=quad2=quad3=quad4=0
robots=[]
for line in open(0):
    p,v=line.split()
    px,py=p[2:].split(',')
    vx,vy=v[2:].split(',')
    px=int(px)
    py=int(py)
    vx=int(vx)
    vy=int(vy)
    robots.append((px,py,vx,vy))
    px,py=update(px,py,vx,vy,1)
    quad=get_quad(px,py)
    if quad==1:
        quad1+=1
    elif quad==2:
        quad2+=1
    elif quad==3:
        quad3+=1
    elif quad==4:
        quad4+=1
print_grid(robots)
print(quad1*quad2*quad3*quad4)
