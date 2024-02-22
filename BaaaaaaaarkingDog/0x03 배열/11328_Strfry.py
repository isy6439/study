import sys
import itertools

# 문자열의 길이가 동일해야함. 
N = int(input())

alphabet = [0]*26

for i in range(N) :
    impossible = 0

    origin, transform = map(str, sys.stdin.readline().split())

    for s in origin : 
        alphabet[ord(s)-97]+=1

    #print(alphabet)
    
    for s in transform :
        alphabet[ord(s)-97]-=1

    if alphabet.count(0) == 26 :
        print("Possible")
    else : 
        print("Impossible")

    #print(alphabet.count(0))
    
    alphabet = [0]*26

'''
for i in range(N) :
    possible = 0

    origin, transform = map(str, sys.stdin.readline().split())

    #print(len(transform))

    for trans in itertools.permutations(origin, len(transform)) :

        plus = list(trans)

        compare = ''.join(s for s in plus)
        #print(compare)

        if(compare == transform) :
            print("Possible")
            possible = 1
            break
        
    if(possible == 0) :
        print("Impossible")

'''
