import sys

class Node :
    def __init__(self, prev, next, data) : 
        self.prev = prev
        self.next = next
        self.data = data
    

class DoubleList : 
    def __init__(self) : 
        self.head = Node(None, None, None)
        self.tail = Node(self.head, None, None)

        self.head.next = self.tail
        self.curser = self.tail

    def insert(self, curser, data) :
        new = Node(curser.prev, curser, data)

        curser.prev.next = new
        curser.prev = new
    
    def erase(self, curser) :    
        curser.prev.next= curser.next
        curser.next.prev = curser.prev
        

    def print_element(self) : 
        current = self.head
        while current.next is not None : 
            current = current.next
            if current.data is not None :
                print(current.data, end = "")
    
if __name__ == "__main__" : 

    problem = sys.stdin.readline().strip()
    editor = DoubleList()

    for i in range(len(problem)) : 
        editor.insert(editor.tail, problem[i])

    M = int(sys.stdin.readline().strip())

    for _ in range(M) : 
        command = list(map(str, sys.stdin.readline().split()))
        #print(command)
        if command[0] == "L" :
            if editor.curser.prev.prev is not None : 
                editor.curser = editor.curser.prev
            
        elif command[0] == "D" : 
            if editor.curser.next is not None : 
                editor.curser = editor.curser.next
            
        elif command[0] == "B" : 
            if editor.curser.prev.prev is not None : 
                editor.erase(editor.curser.prev) ###
        
        else : 
            editor.insert(editor.curser, command[1])

    
    editor.print_element()

