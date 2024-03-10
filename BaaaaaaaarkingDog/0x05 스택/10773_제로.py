import sys

if __name__ == "__main__" : 
    numbers = []

    K = int(sys.stdin.readline().strip())

    for _ in range(K) :
        num = int(sys.stdin.readline().strip())

        if num == 0 :
            numbers.pop()
        else :
            numbers.append(num)
    
    answer = 0
    for x in numbers :
        answer = answer + x

    print(answer)