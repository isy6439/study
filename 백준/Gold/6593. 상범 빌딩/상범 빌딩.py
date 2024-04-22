import sys
from collections import deque

def bfs(building, x, y, z) :

    building[x][y][z] = 1
    queue = deque([(x, y, z)])

    dx = [0, 0, 0, 0, 1, -1]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 1, -1, 0, 0]

    while queue : 
        x, y, z = queue.popleft()

        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C : 
                if building[nx][ny][nz] == "." : 
                    building[nx][ny][nz] = building[x][y][z] + 1 
                    queue.append((nx, ny, nz))

                elif building[nx][ny][nz] == "E" : 
                    print("Escaped in", building[x][y][z], "minute(s).")
                    return
                
    #print(building)

    print("Trapped!")
    return 



if __name__ == "__main__" : 

    while True : 
        L, R, C = map(int, sys.stdin.readline().split())

        if L == 0 and R == 0 and C == 0 :
            break
        
        building = []
        for x in range(L) : 
            floor = []
            for y in range(R+1) : 
                row = list(map(str, sys.stdin.readline().strip()))
                if row == [] : 
                    break
                floor.append(row)

            building.append(floor)

        
        # building = [[list(map(str, sys.stdin.readline().strip())) for x in range(R)] for y in range(L)]
        # print(building)
        for x in range(L) : 
            for y in range(R) : 
                for z in range(C) :
                    # print(building[x][y][z], end = " ")
                    
                    if building[x][y][z] == "S" : 
                        bfs(building, x,y,z)
                        break

            #print()

        