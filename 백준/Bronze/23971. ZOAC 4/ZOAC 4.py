import sys

H, W, N, M = map(int, sys.stdin.readline().split())

h = (H-1) // (N+1) + 1 
w = (W-1) // (M+1) + 1

#print(h, w)

print(h*w)
