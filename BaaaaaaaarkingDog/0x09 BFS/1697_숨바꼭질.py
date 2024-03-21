import sys
from collections import deque

def bfs() : 

    dx = [1, -1]

    while hide : 
        subin = hide.popleft()

        #print(road[:42])

        for i in range(2) : 
            ns = subin + dx[i]
            #print(ns)
            if 0 <= ns < 100001 :
                if road[ns] == 0 :
                    road[ns] = road[subin] + 1
                    hide.append(ns)

                elif road[ns] == -1 : 
                    return road[subin]
                
        ns = subin * 2
        #print(ns)

        if 0 <= ns < 100001 :
            if road[ns] == 0 :
                road[ns] = road[subin] + 1
                hide.append(ns)

            elif road[ns] == -1 : 
                return road[subin]

            

if __name__ == "__main__" : 

    N, K = map(int, sys.stdin.readline().split())

    num = [i for i in range(K)]

    road = [0]*100001
    road[N] = 1
    road[K] = -1

    if N == K : 
        print("0")

    else :
        hide = deque([N])
        print(bfs())

