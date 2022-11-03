import sys
input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())

db1 = {}
db2 = {}

for i in range(N):
    name, num = input(), i + 1
    db1[num] = name
    db2[name] = num

for _ in range(M):
    s = input()
    if s.isdigit():
        print(db1[int(s)])
    else:
        print(db2[s])