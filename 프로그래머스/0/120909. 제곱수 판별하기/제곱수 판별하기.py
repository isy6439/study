import math
def solution(n):
    root = math.sqrt(n)
    if root.is_integer() : 
        return 1
    return 2