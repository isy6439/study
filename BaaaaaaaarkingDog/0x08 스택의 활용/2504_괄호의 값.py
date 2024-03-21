# (()

import sys

brackets = sys.stdin.readline().strip()
stack = []
ans = 0

step = 1

for bracket in brackets : 
    #print(stack)
    if len(stack) == 0 : 
        #print("empty", bracket)
        stack.append(bracket) 
    
    else : 

        if bracket == ")" :

            num = 0
            b = 0

            while stack :
                    top = stack[-1]
                    if top == "(" : 
                        #print("1")
                        stack.pop()
                        stack.append(2 if num == 0 else 2*num)
                        b = 1
                        break

                    elif isinstance(top, int):
                        #print("2", bracket)
                        stack.pop()
                        b = 2
                        num = num + top

                    else :
                        #print("3")
                        #print("!!")
                        break
                    
            if b == 2 :
                stack.append(num)
                stack.append(bracket)
            
            if b == 0 : 
                stack.append(bracket)

        elif bracket == "]" :

            num = 0
            b = 0

            while stack :
                    top = stack[-1]
                    if top == "[" : 
                        #print("1")
                        stack.pop()
                        stack.append(3 if num == 0 else 3*num)
                        b = 1
                        break

                    elif isinstance(top, int):
                        #print("2", bracket)
                        stack.pop()
                        b = 2
                        num = num + top

                    else :
                        #print("3")
                        #print("!!")
                        break
                    
            if b == 2 :
                stack.append(num)
                stack.append(bracket)

            if b == 0 : 
                stack.append(bracket)

        else : 
            stack.append(bracket) 

#print(stack)
#print(ans)

error = True

for x in stack : 
    if isinstance(x, int) : 
        error = False
    else :
        error = True 
        break

print(sum(stack) if not error else "0")