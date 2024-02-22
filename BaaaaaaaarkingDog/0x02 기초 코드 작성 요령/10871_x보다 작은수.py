import sys

n, x = map(int, sys.stdin.readline().split()) # input()으로 입력시 시간초과 가능성 
a = list(map(int, sys.stdin.readline().split())) # list로 변환

for i in a : 
    if(i < x) : 
        print(i, end = " ") # 줄바꿈 없이












