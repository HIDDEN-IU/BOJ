N = int(input())

isPrime = [False,False]+[True for _ in range(N+1)]

for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N+1, i):
            isPrime[j] = False

pl = list(filter(lambda x: isPrime[x],[i for i in range(2,N+1)]))
s, sidx, eidx, answer = 0,0,0,0
while True:
    try:
        if s > N:
            s -= pl[sidx]
            sidx +=1
        else:
            if s == N:
                answer += 1
            s += pl[eidx]
            eidx += 1
    except:
        print(answer)
        break