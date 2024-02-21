import sys

N = int(input())
time = list(map(int, sys.stdin.readline().split()))

Y = 0
M = 0

for t in time :
    # print(t//29, t//59)
    Y = Y + (t//30+1)*10
    M = M + (t//60+1)*15

#print(Y, M) 

if(Y == M) :
    print("Y", "M", Y)
elif(Y < M) :
    print("Y", Y)
else :
    print("M", M)

