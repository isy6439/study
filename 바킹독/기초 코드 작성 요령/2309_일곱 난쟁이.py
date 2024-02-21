# sol1. total 합에서 2개를 -, 100이 되는 지 확인. 

import sys

height = [int(input()) for _ in range(9)]

height.sort()
total_height = sum(height)

for i in range(9) :
    test = total_height
    answer = []
    find = 0

    test = test-height[i]
    
    for j in range(i+1, 9) :
        test = test-height[j]
        if(test == 100) : 
            for k in range(9) :
                if(k!=i and k!=j) : # or height.remow(height[i])
                    answer.append(height[k]) # 정확하게 고려할 것.
                    find = 1

        else :
            test = test + height[j]

        if(find == 1) :
            break
    
    if(find == 1) :
        break

# print(answer)
# print(sum(answer))

for ans in answer :
    print(ans)

# sol.2 combination, 중복없이 7게 뽑아 합 계산 

import itertools 

h = [int(sys.stdin.readline().strip() for _ in range(9))]

for i in itertools.combinations(h, 7) :
    tot = sum(i)
    if(tot == 100) :
        for result in sorted(i) : 
            print(result)
    break

    
