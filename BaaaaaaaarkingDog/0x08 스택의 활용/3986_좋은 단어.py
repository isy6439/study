import sys

N = int(sys.stdin.readline().strip())

stack = [] 
ans = 0
for _ in range(N) : 
    string = sys.stdin.readline().strip()

    for word in string :
        if len(stack) == 0 :
            stack.append(word)
        
        else : 
            if stack[-1] == word : 
                stack.pop()
            else :
                stack.append(word)
    
    if len(stack) == 0 : 
        ans = ans + 1
    
    stack = []

print(ans)


