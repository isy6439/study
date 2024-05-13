import sys

def multiple(a, b) : 
    #print(a, b)
    if b == 1 :
        #print(a % C) 
        return a % C
    
    else : 
        v = multiple(a, b//2) 
        if b % 2 == 0 : 
            #print((v * v) % C)

            return (v * v) % C 
        
        else :
            #print((v * v * a) % C)
            return (v * v * a) % C

if __name__ == "__main__" : 
    A, B, C = map(int, sys.stdin.readline().split())

    print(multiple(A, B))

