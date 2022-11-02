from heapq import *


class shark:
    def __init__(self,x,y):
        self.pos = (x,y)
        self.size = 2
        self.belly = 0

    def eat(self,x,y):
        self.belly += 1
        if self.size == self.belly:
            self.belly = 0
            self.size += 1
        s.pos = (x,y)

d = [(-1,0),(0,-1),(0,1),(1,0)]

N = int(input())
nrange = range(N)

sea = []

for i in nrange:
    line = [int(c) for c in input().split()]
    if 9 in line:
        j = line.index(9)
        s = shark(i,j)
        line[j] = 0
    sea.append(line)

time = 0
while True: # while there is something to eat
    visited = [[False]*N for _ in nrange]
    nv = [(0,*s.pos)]
    t = 0
    while nv: #while there is more place to explore
        v = [dot for dot in nv]
        nv = []
        while v: #for a second
            priority,x,y = heappop(v)
            if not sea[x][y] or sea[x][y] == s.size:
                for dx, dy in d:
                    X,Y = x+dx, y+dy
                    if X in nrange and Y in nrange and not visited[X][Y]:
                        visited[X][Y] = True
                        heappush(nv,(X*N+Y,X,Y))
            elif sea[x][y] <= s.size:
                s.eat(x,y)
                sea[x][y] = 0
                break
        else: #end of a second
            t += 1
            continue
        time += t
        break
    else: #explored everywhere but cannot eat something
        print(time)
        break