import sys
from collections import deque

N = int(sys.stdin.readline().strip())

dq = deque([x for x in range(1, N+1)])

while len(dq)!=1 : 
    dq.popleft()
    dq.append(dq.popleft())

print(*dq)