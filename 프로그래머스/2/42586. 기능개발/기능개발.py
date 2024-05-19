def solution(progresses, speeds):
    answer = []
    stack = [( 100 - progresses[0] - 1 )// speeds[0] + 1]
    max_day = stack[0]
    
    for i in range(1, len(speeds)) : 
        remain = (100 - progresses[i] - 1) // speeds[i] + 1
        print(stack)
        
        if stack[-1] >= remain or remain <= max_day : 
            stack.append(remain)
        
        else :
            answer.append(len(stack))
            stack = [remain]
            
        max_day = max(remain, max_day)
            
    answer.append(len(stack))
            
    return answer