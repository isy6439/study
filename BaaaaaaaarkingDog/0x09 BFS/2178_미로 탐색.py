import sys
from collections import deque

def bfs(x, y) : 
    queue = deque([(x, y)])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    a[x][y] = 0

    while queue : 
        x, y = queue.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i] 

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
        
            if a[nx][ny] == 1 :
                #print(x, y)
                a[nx][ny] = a[x][y] + 1
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist[N-1][M-1]

if __name__ == "__main__" : 
    N, M = map(int, sys.stdin.readline().split())
    
    a = []
    for _ in range(N) :
        a.append(list(map(int, sys.stdin.readline().strip())))

    dist = [[0]*M for _ in range(N)]

    #print(a)

    # print(dist)

    print(bfs(0, 0) + 1)
    # print(a[N-1][M-1])

    # for i in range(N) :
    #     print(a[i])
    #     print(dist[i])

    #     print()



    