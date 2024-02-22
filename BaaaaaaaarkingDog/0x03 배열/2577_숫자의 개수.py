import sys

tot = 1

for _ in range(3) : 
    num = int(sys.stdin.readline().strip()) # 줄바꿈 여러개
    tot*=num

string_tot = str(tot)
ans = [0 for _ in range(10)]

for alpha in string_tot : 
    #print(ord(alpha)-48) # 숫자 48, 소문자 97
    ans[ord(alpha)-48]+=1

for x in ans :
    print(x)

# or
    
for i in range(10) :
    print(string_tot.count(str(i))) # string_tot에 i가 몇개인지 세주는 함수




