import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T) : 

    P = sys.stdin.readline().strip()
    impossible = False

    n = int(sys.stdin.readline().strip()) # 배열 원소 수 

    input_array = sys.stdin.readline().strip()
    input_array = input_array.strip("[" "]")
    input_array = input_array.replace(",", " ", n-1)

    dq = deque(input_array.split())
    #dq = deque(input_array.strip[1:-1].split(","))
    reverse = False

    for command in P : 
        #print(dq)

        if command == "R" : 
            if reverse : # 바로 reverse 함수 사용시 시간초과 
                reverse = False
            else :
                reverse = True
        else :
            if not dq :
                impossible = True
                print("error")
                break
            if reverse : 
                dq.pop()
            else :
                dq.popleft()
            

    if reverse == True : 
        dq.reverse()
        
    if not impossible:
        if len(dq) == 0 :
            print("[]")
        else : 
            print("[", end = "") # 출력 형태 유의할 것. 
            for i in range(len(dq)-1) : 
                print(dq.popleft(), end = "")
                print(",", end = "")
            print(dq[0], end = "")
            print("]")

            # "[" + ",".join(map(str, dq)" + ]"
    
        #print(list(dq))
