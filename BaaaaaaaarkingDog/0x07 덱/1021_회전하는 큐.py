import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
popping = list(map(int, sys.stdin.readline().split())) # 여기 없는 수는 pop할 수 없음. 

dq = deque([x for x in range(1, N+1)])
ans = 0
cn = 0 

for idx in popping : 
    while dq : 
        if dq[0] == idx : 
            dq.popleft()
            break
        else : 
            if dq.index(idx) < len(dq) / 2 : 
                dq.append(dq.popleft())
                ans+=1
            else : 
                dq.appendleft(dq.pop())
                ans+=1



print(ans)
    
