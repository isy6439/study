import sys

N, K = map(int, sys.stdin.readline().split())
student = [[0 for year in range(6)] for sex in range(2)]

#print(student)

for i in range(N) :
    s, y = map(int, sys.stdin.readline().split())
    student[s][y-1]+=1

#print(student)

room = 0

for sex in range(2) :
    for year in range(6) :
        if(student[sex][year]!=0) :
            room+=(student[sex][year]+K-1)//K

print(room)