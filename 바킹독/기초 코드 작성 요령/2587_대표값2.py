a = []

for i in range(5) :
    num = int(input())
    a.append(num)

a.sort()

print(int(sum(a)/5))
print(a[2])


# 한줄로 입력 받기

b = [int(input()) for _ in range(5)]

print(sum(b)//5)