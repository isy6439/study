import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

## sol 1. 

total = [0 for _ in range(2000001)]

a.sort() # 내림차순 reverse = True
ans = 0

for i in a : 

    if(total[x-i] == 1) :
        ans+=1
        total[x-i] = 0

    total[i]+=1

print(ans)

# sol 2. 포인터 두개
left = 0
right = len(a)-1

answer = 0

while(left!=right) :

    if(a[left]+a[right] == x) : 
        answer+=1

    elif(a[left]+a[right] > x) :
        right-=1
    
    else :
        left+=1

print(answer)