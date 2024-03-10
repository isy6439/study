import sys
from collections import deque

N = int(sys.stdin.readline().strip())

dq = deque()

for _ in range(N) : 
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "push" : 
        dq.append(command[1])

    elif command[0] == "pop" :
        print(dq.popleft() if dq else "-1")
    
    elif command[0] == "size" :
        print(len(dq))

    elif command[0] == "empty" :
        print("0" if dq else "1")
    
    elif command[0] == "front" :
        print(dq[0] if dq else "-1")
    
    else :
        print(dq[-1] if dq else "-1") 

