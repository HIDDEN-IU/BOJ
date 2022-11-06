def direct(c):
    if c == 'D':
        return 1,0
    elif c == 'L':
        return 0,-1
    elif c == 'R':
        return 0,1
    else:
        return -1,0

N, M = map(int,input().split())

zone = [input() for _ in range(N)]

safe = [[0]*M for _ in range(N)]
cnt = 0
answer = 0
for n in range(N):
    for m in range(M):
        if not safe[n][m]:
            x,y = n,m
            cnt += 1
            while not safe[x][y]:
                safe[x][y] = cnt
                dx,dy = direct(zone[x][y])
                x,y = x + dx, y + dy
            if safe[x][y] == cnt:
                answer += 1
print(answer)