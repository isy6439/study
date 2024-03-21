import sys
from collections import deque

def bfs(x, y) : 
    field[x][y] = 0
    cabbage = deque([(x,y)])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while cabbage : 
        x, y = cabbage.popleft()

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1 : 
                field[nx][ny] = 0
                cabbage.append((nx, ny))

if __name__ == "__main__" :
    T = int(sys.stdin.readline().strip())

    for _ in range(T) : 
        M, N, K = map(int, sys.stdin.readline().split())
        
        field = [[0]*M for _ in range(N)]
        
        for _ in range(K) :
            x, y = map(int, sys.stdin.readline().split())
            field[y][x] = 1

        # for i in range(N) : 
        #     for j in range(M) :
        #         print(field[i][j], end = " ")
        #     print()

        worm = 0
        for i in range(N) : 
            for j in range(M) : 
                if field[i][j] == 1 : 
                    bfs(i, j)
                    worm += 1

        print(worm)
    
    

