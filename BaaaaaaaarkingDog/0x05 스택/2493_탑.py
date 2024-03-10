import sys

N = int(sys.stdin.readline().strip())
top = list(map(int, sys.stdin.readline().split()))

stack = []
num = []

signal = []

for i in range(N) : # for i, tower in emurate(top)

    if not stack :
        #print("empty", top[i])
        signal.append(0)
        
    else :
        while True :
            if stack[-1] > top[i] :
                signal.append(num[-1])
                #print(top[i], num[-1])
                break
            else :
                stack.pop()
                num.pop()
                #num = num - 1
                if not stack :
                    #print(top[i], 0)
                    signal.append(0) 
                    break

    stack.append(top[i])
    num.append(i+1)
    #num = num + 1

    #print(stack, num)


print(*signal)
