import sys
from collections import deque

def BFS() : 

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while tomatoes :
        x, y = tomatoes.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < M and 0 <= ny < N and a[nx][ny] == 0 :
                #print("!!")
                a[nx][ny] = a[x][y] + 1
                tomatoes.append((nx, ny)) 
            
if __name__ == "__main__" : 
    N, M = map(int, sys.stdin.readline().split())
    a = []

    for _ in range(M) : 
        a.append(list(map(int, sys.stdin.readline().split())))

    tomatoes = deque()

    for i in range(M) : 
        for j in range(N) :
            if a[i][j] == 1 :
                tomatoes.append((i,j))
    
    BFS()

    #print()

    error = False

    for i in range(M) : 
        for j in range(N) :
            if a[i][j] == 0 : 
                print("-1")
                error = True
                exit() # 2개 반복문 동시 탈출을 위해서는 break가 아니라 exit()
            #print(a[i][j], end = " ")
        #print("")        

    if not error :
        print(max(map(max, a))-1)