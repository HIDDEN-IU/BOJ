
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

db = {}
for _ in range(N):
    site, name = input().split()
    db[site] = name

for _ in range(M):
    print(db[input()])