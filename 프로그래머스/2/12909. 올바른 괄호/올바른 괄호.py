def solution(s):
    answer = True
    stack = []
    
    for bracket in s : 
        
        if stack and stack[-1] == "(" and bracket == ")" : 
            stack.pop()
            
        else : 
            stack.append(bracket)
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    if stack : 
        return False
    else :
        return True

    return True