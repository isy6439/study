# 6, 9 테스트 확인.

N = input()

max_num = 0
six_nine = 0

for i in range(10) :
    if(i == 6 or i == 9) :
        six_nine += N.count(str(i))
    else :
        max_num = max(max_num, N.count(str(i)))

if(six_nine < max_num or (six_nine+1)//2 < max_num) : 
    print(max_num)

else :
    print((six_nine+1)//2)