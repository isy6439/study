#특이 케이스에 대한 고려 필요. ex) 0, 1 등
N = int(input())


for i in range(N) : 
    print(" " * (i) + "*" * (2*(N-i)-1))

for i in range(N-1) : 
    print(" " * (N-i-2) + "*" * (2*(i+1)+1))
