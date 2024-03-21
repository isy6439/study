import sys
from collections import deque 

def bfs(graph, i, j, c) : 

    graph[i][j] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    color = deque([(i, j)])

    while color :
        x, y = color.popleft()

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == c : 
                graph[nx][ny] = 0
                color.append((nx, ny))


if __name__ == "__main__" : 
    N = int(sys.stdin.readline().strip())
    picture = [ list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
    blind = [['R' if data == "G" else data for data in row] for row in picture]

    origin = 0
    blindc = 0

    for i in range(N) : 
        for j in range(N) :
            if picture[i][j] != 0 : 
                bfs(picture, i,j, picture[i][j])
                origin += 1

            if blind[i][j] != 0 :
                bfs(blind, i, j, blind[i][j])
                blindc += 1

    print(origin, blindc)

                

