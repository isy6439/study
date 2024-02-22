import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().strip())

print(a.count(v))
