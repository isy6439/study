import math # math.gcd(denom, numer)

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2 
    numer = numer1 * denom2 + numer2 * denom1
    
    a = max(denom, numer)
    b = min(denom, numer)
    
    while b!=0 : 
        n = a%b
        a = b
        b = n
    
    answer = [numer/a, denom/a]
    return answer