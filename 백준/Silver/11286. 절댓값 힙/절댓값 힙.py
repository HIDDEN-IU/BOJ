import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import *

db = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        if x > 0:
            heappush(db,x*2+1)
        else:
            heappush(db,(-x)*2)
    elif db:
        num = heappop(db)
        if num%2:
            print((num-1)//2)
        else:
            print(-(num//2))
    else:
        print(0)