import sys

n = int(sys.stdin.readline().strip())

numbers = []
ans = []

current = 1

top = 0

no = 0

for i in range(n) : 
    num = int(sys.stdin.readline().strip())

    #print(top)

    while True  :

        if top > num :
            no = 1
            break

        elif num == top :
           #print("!!")
           numbers.pop()
           ans.append("-")
           if len(numbers)!= 0 :
               top = numbers[-1]
           break

        elif num > top : 
            numbers.append(current)
            ans.append("+")
            current = current + 1

        else :
            if len(numbers) == 0 :
                no = 1
                break
            numbers.pop()
            ans.append("-")

        top = numbers[-1]

    #print(numbers)
    #print(ans)
        
if no == 1 :
    print("NO")

else : 

    for num in ans :
        print(num)