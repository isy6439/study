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

    def insert(self, idx, data) :
        new = Node(idx.prev, idx, data)
        
        idx.prev.next = new
        idx.prev = new

        #self.curser = self.curser.next
        
    def erase(self, idx) :
        idx.prev.next = idx.next
        idx.next.prev = idx.prev

        #self.curser = self.curser.prev

    def print_element(self) :
        current_node = self.head
        while current_node.next is not None :
            current_node = current_node.next
            if current_node.next is not None : 
                print(current_node.data, end="")
            

if __name__ == "__main__" : 
    N = int(sys.stdin.readline().strip())

    for _ in range(N) : 

        user_input = sys.stdin.readline().strip()
        password = DoubleList()
        #print(user_input)

        for word in user_input : 
            #print(word)
            if word == "<" : 
                if password.curser.prev.prev is not None :
                    password.curser = password.curser.prev
            elif word == ">" :
                if password.curser.next is not None:
                    password.curser = password.curser.next
            elif word == "-" :
                if password.curser.prev.prev is not None :
                    password.erase(password.curser.prev)
            else : 
                password.insert(password.curser, word)
                
        password.print_element()

        print("")

