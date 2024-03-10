import sys

N = int(sys.stdin.readline().strip())

stack = []
idx = []
ans = 0
cn = 0

max_idx = 0
max_height = 0

for i in range(N) :
    h = int(sys.stdin.readline().strip())

    if h > max_height :
        max_height = h
        max_idx = i
    
    while stack :
        if stack[-1][0] >= h :
            #print(stack)
            #ans = ans + abs(i - max_idx)
            #print(h, max_idx, "maxs", i, i - max_idx)
            #print(h, len(stack), stack)
            break
            
        else :
            #ans = ans + 1
            cn = cn + 1
            print("<", stack[-1][0], h, ">")
            stack.pop()
            #idx.pop()

    if stack : 
        print("1", "<", stack[-1], h, ">")
        cn += 1
    
    #idx.append(i)
    stack.append((h, cn))

    print(stack)

    #ans = ans + len(stack)

    
print(ans)
print(cn)