import sys

S = sys.stdin.readline().strip()

ans = [0 for _ in range(26)]

for alpha in S :
    #print(ord(alpha)-97)
    ans[ord(alpha)-97] += 1

print(*ans)
