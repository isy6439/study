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

        self.curser = self.tail

    def find(self, data) : 
        current = self.head

        while True :
            if current.data == data :
                break
            current = current.next
            #print(current.data)

        return current
    
    def insert(self, idx, data) : 
        new_node = Node(idx.prev, idx, data) 

        idx.prev.next = new_node
        idx.prev = new_node

    def erase(self, idx) : 
        idx.prev.next = idx.next
        idx.next.prev = idx.prev

    def print_element(self) :
        current = self.head
        for _ in range(10) : 
            print(current.data, end = " ")
            current = current.next
        print("")

    
if __name__ == "__main__"  :
    N, M = map(int, sys.stdin.readline().split())
    origin = list(map(int, sys.stdin.readline().split()))

    stations = CircleList(origin[0], origin[-1])

    for i in range(1, N-1) : 
        stations.insert(stations.tail, origin[i]) 

    #print(stations.curser.data)

    for _ in range(M) : 
        stations.print_element()

        command = list(map(str, sys.stdin.readline().split()))

        idx = stations.find(int(command[1]))

        if command[0] == "BN" : 
            print(idx.next.data)
            stations.insert(idx.next, command[2])
        
        elif command[0] == "BP" : 
            print(idx.prev.data)
            stations.insert(idx, command[2])

        elif command[0] == "CN" : 
            print(idx.next.data) 
            stations.erase(idx)
        
        else :
            print(idx.prev.data) 
            stations.erase(idx.prev)
    
