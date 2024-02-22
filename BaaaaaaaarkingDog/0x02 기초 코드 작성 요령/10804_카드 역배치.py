import sys
origin = [x for x in range (1, 21)]

for _ in range(10) :
    start, end = map(int, sys.stdin.readline().split())

    #print(origin)
    
    change = origin[start-1:end]
    change_reverse = change[::-1]

    origin[start-1:end] = change_reverse

    #print(origin)

print(*origin)