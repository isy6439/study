import sys

N, M = map(int, sys.stdin.readline().split())

A = list(int(sys.stdin.readline().strip()) for _ in range(N))

A.sort()
a = 0; b = 0   
answer = 1e11
while b < N and a < N: 
    minus = abs(A[a] - A[b])
    if minus < M :
        b += 1
    else : 
        a += 1

    if minus >= M :
        answer = min(answer, minus)

print(answer)