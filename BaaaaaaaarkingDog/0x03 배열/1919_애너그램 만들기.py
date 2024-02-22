import sys 

a = str(sys.stdin.readline().strip())
b = str(sys.stdin.readline().strip())

alphabet = [0]*26

for x in a :
    alphabet[ord(x)-97]+=1

for x in b :
    alphabet[ord(x)-97]-=1

#print(*alphabet)

ans = 0

for i in range(26) :
    if alphabet[i]!=0 :
        ans+=abs(alphabet[i])

print(ans)