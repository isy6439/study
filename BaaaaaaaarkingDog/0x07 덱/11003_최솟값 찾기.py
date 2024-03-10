import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

dq = deque() 
ans = []

min_data = 1e9

for i, data in enumerate(A) : 

    print(dq)
    print(i-L+1, i)
    if i-L+1 > 0 :
        start = max(0, i-L+1)
        dq.popleft()
    
    dq.append(data)

    # if dq[-1] < min_data : 
    #     min_data = dq[-1] 
    
    ans.append(min(dq))

print(*ans)
    


    



    
