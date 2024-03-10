import sys

stack = []

while True :
    string = sys.stdin.readline().rstrip()

    #print(string)
    
    if string[0] == "." :
        break
    
    for word in string : 
        #print(stack)
        if word == "["  or word == "("  :
            stack.append(word)
        
        if word == "]" :
            if len(stack) > 0 and stack[-1] == "["  : 
                stack.pop()
            else :
                stack.append(word)
                break
        elif word == ")" :
            if len(stack) > 0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(word)
                break
    
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
    
    stack = []

