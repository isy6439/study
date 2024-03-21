import sys
from collections import deque

def bfs(graph, x,y) : 
    queue = deque([(x,y)])

    graph[x][y] = 0 # 방문 기록

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0] # 대각선 제외 갈 수 있는 위치

    area = 1

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m : 
                continue
            
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx,ny))

                area += 1

    return area

if __name__ == "__main__" : 

    cnt = 0
    ans = 0
    
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    for i in range(n) : 
        for j in range(m) :
            if graph[i][j] == 1 :
                cnt += 1
                ans = max(bfs(graph, i, j), ans)

    
    print(cnt)
    print(ans)