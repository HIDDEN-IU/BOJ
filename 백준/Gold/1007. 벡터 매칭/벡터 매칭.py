from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    N = int(input())
    Xs, Ys = 0,0
    dots = []
    for _ in range(N):
        x,y = map(int, input().split())
        dots.append((x,y))
        Xs += x
        Ys += y

    l = []
    combi = list(combinations(range(N),N//2))
    for com in combi[:len(combi)//2]:
        X,Y = 0,0
        for i in com:
            X += dots[i][0]
            Y += dots[i][1]
        l.append((Xs-2*X)**2+(Ys-2*Y)**2)
    print(min(l)**0.5)