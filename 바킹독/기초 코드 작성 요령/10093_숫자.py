start, end = map(int, input().split())

if(start > end) :
    tmp = end
    end = start
    start = tmp

# or use max, min

numbers = [x for x in range(start + 1 , end)]

print(len(numbers)) # 두 수가 같을 경우 고려해야 함. 
print(*numbers) 

