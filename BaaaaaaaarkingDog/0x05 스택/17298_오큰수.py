import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
A = A[::-1]
stack = []
NGE = []

for i, a in enumerate(A) :

    empty = False

    while stack :
        if(stack[-1] > a) : 
            NGE.append(stack[-1])
            empty = True
            break
        else :
            stack.pop()
    
    stack.append(a)
    #print(stack)
    if empty == False : 
        NGE.append(-1)
    #print(*NGE)

print(*NGE[::-1])
