import sys

while True : 
    command = list(map(int, sys.stdin.readline().split()))
    if command == [0, 0, 0] : 
        break
    command.sort()

    a, b, c = command 

    if a + b <= c : 
        print("Invalid")

    else : 
        if a == b and b == c and c == a : 
            print("Equilateral")
        elif a!=b and b!=c and c!=a : 
            print("Scalene")
        else :
            print("Isosceles")
