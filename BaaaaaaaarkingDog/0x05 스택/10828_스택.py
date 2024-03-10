#FILO
import sys

class Stack :
    def __init__(self) : 
        self.stack = []
    
    def push(self, data) :
        self.stack.append(data)
    
    def pop(self) :

        if len(self.stack) == 0 : 
            print(-1)
        
        else :
            popped = self.stack.pop()
            print(popped)

        print(self.stack.pop() if self.stack else -1)
    
    def size(self) :
        print(len(self.stack))

    def empty(self) :
        if len(self.stack) == 0 :
            print(1)
        else :
            print(0)
    
    def top(self) :
        if len(self.stack) == 0 : 
            print(-1)
        else :
            print(self.stack[-1])


if __name__ == "__main__" : 

    #a = []
    #print(a[-1])

    N = int(sys.stdin.readline().strip())

    stack = Stack()

    for _ in range(N) :
        command = list(map(str, sys.stdin.readline().split()))

        if command[0] == "push" :
            stack.push(command[1])

        elif command[0] == "pop" :
            stack.pop()
        
        elif command[0] == "size" : 
            stack.size()

        elif command[0] == "empty" : 
            stack.empty()

        elif command[0] == "top" : 
            stack.top()

        
