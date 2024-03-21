import sys
from collections import deque

impossible = False

def bfs() : 

    global impossible

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    while jihoon_fire : 
        x, y = jihoon_fire.popleft()

        if maze[x][y] < 0 :
            id = -1
        else :
            id = 1

        # print(x ,y)
        # for i in range(R) : 
        #     for j in range(C) : 
        #         print(maze[i][j], end = " ")
        #     print()

        # print("!!")

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C :
                if maze[x][y] > 0 :
                    return 

            elif 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != "#":
                if maze[nx][ny] == 0 : 

                    maze[nx][ny] = maze[x][y] + id
                    jihoon_fire.append((nx, ny))

                elif maze[nx][ny] > 0 and maze[x][y] < 0 :
                    
                    maze[nx][ny] = maze[x][y] + id
                    jihoon_fire.append((nx, ny))
                

if __name__ == "__main__" : 
    R, C = map(int, sys.stdin.readline().split())
    maze = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

    jihoon_fire = deque()
    for i in range(R) : 
        for j in range(C) :
            if maze[i][j] == "J" : 
                jihoon_fire.appendleft((i,j))
                maze[i][j] = 1
            elif maze[i][j] == "F" : 
                jihoon_fire.append((i,j))
                maze[i][j] = -1
            elif maze[i][j] == "." : 
                maze[i][j] = 0

    bfs()

    # print()

    time = 1e9
    for i in range(R) : 
        for j in range(C) : 
            # print(maze[i][j], end = " ")
            if i == R-1 or i == 0 or j == C-1 or j == 0: 
                if maze[i][j] == "#" : 
                    continue
                elif maze[i][j] > 0 :
                    time = min(time, maze[i][j]) # 가장자리에서 최솟값을 구해야함. not max
        # print()

    if time == 1e9 :
        print("IMPOSSIBLE")
    
    else :
        print(time)

    