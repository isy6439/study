import sys

a, b, c = map(int, sys.stdin.readline().split())

if a > b :
    tmp = b
    b = a
    a = tmp

if b > c :
    if a > c : 
        print(c, a, b)
    else :
        print(a, c, b)

else : 
    print(a, b, c)

# or
    
before = list(map(int, sys.stdin.readline().split()))

before.sort()