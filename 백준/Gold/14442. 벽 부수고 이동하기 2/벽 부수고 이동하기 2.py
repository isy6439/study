import sys
from collections import deque

def bfs(x, y) : 

    for i in range(K + 1) : 
        visited[x][y][i] = 1
   
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(x, y, 0, 1)])

    distance = 1e9

    while queue : 
        x, y, broken, dist = queue.popleft()

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny][broken] == 0 :
                    if ground[nx][ny] == 0 :
                        visited[nx][ny][broken] = 1
                        queue.append((nx, ny, broken, dist + 1))

                    elif ground[nx][ny] == 1: 
                        if broken < K : 
                            visited[nx][ny][broken] = 1
                            queue.append((nx, ny, broken + 1, dist + 1))
                
                if nx == N - 1 and ny == M - 1 :
                    return dist + 1

    return -1


if __name__ == "__main__" : 
    N, M, K = map(int, sys.stdin.readline().split())
    ground = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    visited = [[[0 for _ in range(K + 1)] for __ in range(M)] for ___ in range(N)]

    if N == 1 and M == 1 and ground[0][0] == 0 : 
        print(1)


    else :
        print(bfs(0,0))
