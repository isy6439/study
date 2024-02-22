import sys

## 내장 함수 이름과 변수 이름 겹치지 않도록 주의할 것. 

# First block of code
for i in range(3):
    a, b, c, d = map(int, sys.stdin.readline().split())
    total_sum = a + b + c + d

    if total_sum == 3:
        print("A")
    elif total_sum == 2:
        print("B")
    elif total_sum == 1:
        print("C")
    elif total_sum == 0:
        print("D")
    else:
        print("E")

# Second block of code
result = ['D', 'C', 'B', 'A', 'E']

for _ in range(3):
    user_input = list(map(int, sys.stdin.readline().split()))
    print(user_input)
    total_sum = sum(user_input)

    if total_sum in range(5):
        print(result[total_sum])
    else:
        print("Invalid input")
