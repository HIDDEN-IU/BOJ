import sys
from heapq import *
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

detdo = {input():1 for _ in range(N)}

dic = []

for _ in range(M):
    try:
        name = input()
        valid = detdo[name]
        heappush(dic, name)
    except:
        pass
print(len(dic))
while dic:
    print(heappop(dic))