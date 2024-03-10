import sys

class Node:
    def __init__(self, prev, next, data):
        self.prev = prev
        self.next = next
        self.data = data

class CircleList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(self.head, self.head, None)

        self.head.next = self.tail
        self.head.prev = self.tail

        self.curser = self.tail
        self.num = [0] * 1000001

    def search(self, data):
        return self.num[data]

    def insert(self, idx, data):
        new_node = Node(idx.prev, idx, data)
        idx.prev.next = new_node
        idx.prev = new_node
        self.num[data] = new_node

    def erase(self, idx):
        idx.prev.next = idx.next
        idx.next.prev = idx.prev
        self.num[idx.data] = 0

    def print_element(self):
        print("!!")
        current = self.head
        while current.next != self.head:
            current = current.next
            print(current.data, end=" ")
        print("")

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    origin = list(map(int, sys.stdin.readline().split()))

    stations = CircleList()

    for i in range(N):
        stations.insert(stations.tail, origin[i])

    for _ in range(M):
        stations.print_element()

        command = list(map(str, sys.stdin.readline().split()))
        idx = stations.search(int(command[1]))

        if command[0] == "BN":
            if idx.next != stations.head:
                print(idx.next.data)
            else:
                print(idx.next.next.next.data)
            stations.insert(idx.next, int(command[2]))

        elif command[0] == "BP":
            if idx.prev != stations.head:
                print(idx.prev.data)
            else:
                print(idx.prev.prev.prev.data)
            stations.insert(idx, int(command[2]))

        elif command[0] == "CN":
            if idx.next != stations.head:
                print(idx.next.data)
            else:
                print(idx.next.next.next.data)
            stations.erase(idx)

        else:
            if idx.prev != stations.head:
                print(idx.prev.data)
            else:
                print(idx.prev.prev.prev.data)
            stations.erase(idx.prev)
