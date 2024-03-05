import sys

class Node : 
    def __init__(self, prev, next, data) :
        self.prev = prev
        self.next = next
        self.data = data

class CircleList :
    def __init__(self, head, tail) :
        self.head = Node(None, None, head)
        self.tail = Node(self.head, self.head, tail)
        self.head.next = self.tail
        self.head.prev = self.tail

        self.curser = self.head
    
        self.answer = []

    def erase(self, idx) :
        
        idx.next.prev = idx.prev
        idx.prev.next = idx.next

        #print("커서", idx.data, idx.next.prev.data ,"이전", idx.prev.data, idx.prev.next.data, "이후", idx.next.data)

        self.answer.append(self.curser.data)

    def insert(self, idx, data) :
        new = Node(idx.prev, idx, data)

        idx.prev.next = new
        idx.prev = new

    def print_element(self, N) :

        current_node = self.head

        for i in range(100) :
            print(current_node.data, end = "")
            current_node = current_node.next

if __name__ == "__main__" : 
    N, K = map(int, sys.stdin.readline().split())

    Yo = CircleList(1, N)

    for i in range(2, N) :
        Yo.insert(Yo.tail, i)

    #print(Yo.print_element())

    for i in range(K-1) :
        Yo.curser = Yo.curser.next
    
    Yo.erase(Yo.curser)

    #print(Yo.curser.data)

    cn = N
    
    while cn-1:
        
        # print(Yo.print_element(N))
        # print(Yo.curser.data)

        for i in range(K) :
            Yo.curser = Yo.curser.next

        Yo.erase(Yo.curser)
        
        cn = cn-1
    
    # print(Yo.print_element(N))
        

    print("<", end = "")

    for i in range(len(Yo.answer)-1) :
        print(Yo.answer[i], end=", ")

    print(Yo.answer[-1], end = "")
    print(">")

    