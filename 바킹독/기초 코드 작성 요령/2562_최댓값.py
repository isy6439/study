import sys

a = [] 

for _ in range(9) :
    a.append(int(sys.stdin.readline().strip()))

#print(a)

max_value = max(a)
max_index = a.index(max_value)

print(max_value)
print(max_index+1)
