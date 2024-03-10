import sys

N = int(sys.stdin.readline().strip())

stack = []
ans = 0

for _ in range(N) :
    h = int(sys.stdin.readline().strip())
    
    while stack :
        if stack[-1] > h :
            #print(stack)
            ans = ans + len(stack)
            #print(h, len(stack), stack)
            break
            
        else :
            stack.pop()
    
    stack.append(h)

    #ans = ans + len(stack)

    
print(ans)