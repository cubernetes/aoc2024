#!/usr/bin/env pypy3

import sys
import re

WIDE=101
TALL=103

#WIDE=11
#TALL=7

def print_grid(robots, print_grid) -> bool:
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
        line=''.join(row)
        if print_grid:
            print(line)
        else:
            if re.search(r'\d{10,}', line):
                return True
    return False

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
lines=open(sys.argv[1]).read().splitlines() # sys.argv[1] because I tried it by hand first (with input()) lol, but only until 1000
for line in lines: # prepare robots
    p,v=line.split()
    px,py=p[2:].split(',')
    vx,vy=v[2:].split(',')
    px=int(px)
    py=int(py)
    vx=int(vx)
    vy=int(vy)
    robots.append((px,py,vx,vy))

for i in range(10_000): # guess 10_000 was enough
    new_robots=[]
    for robot in robots:
        px,py,vx,vy=robot
        px,py=update(px,py,vx,vy,1)
        new_robots.append((px,py,vx,vy))
        quad=get_quad(px,py)
        if quad==1:
            quad1+=1
        elif quad==2:
            quad2+=1
        elif quad==3:
            quad3+=1
        elif quad==4:
            quad4+=1
    robots=new_robots
    if print_grid(robots, False): # plus one because i starts at 0
        print_grid(robots, True)
        print('Found tree after', i+1, 'seconds')
        break
