
tot = 0
my_min = 101

for _ in range(7) :
    num = int(input())
    if(num%2!=0) :
        tot = tot + num
        if(my_min > num) : 
            my_min = num

if(tot == 0) :
    print("-1")
else :
    print(tot)
    print(my_min)

# 배열로 저장하여 min, len 활용 가능
    
odd = []

for _ in range(7) :
    num = int(input())
    if(num % 2 != 0) :
        odd.append(num)

if(len(odd) == 0) :
    print("-1")
else :
    print(sum(odd))
    print(min(odd))