import sys

bracket = sys.stdin.readline().strip()
stack = []
ans = 0

for i in range(len(bracket)) : 
    if len(stack) == 0 :
        #print("empty")
        stack.append(bracket[i]) 
    
    else :
        if stack[-1] == "(" and bracket[i] == ")" : # laser
            #print(stack)
            stack.pop()
            if bracket[i-1] != ")" : 
                ans = ans + len(stack)
            else : 
                ans = ans + 1
           
        else :
            stack.append(bracket[i])

print(ans)