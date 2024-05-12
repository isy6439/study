def solution(array):
    answer = 0
    
    while len(array)!=0 : 
        for idx, value in enumerate(set(array)) : 
            array.remove(value)
        if idx == 0 : 
            return value
    return -1