class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        node_new = Node(val)
        if self.head is None:
            self.head = node_new
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = node_new

    def get(self, index):
        if self.head is None:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.value \
            if current else None

    def remove(self, index):
        if index == 0:
            self.head = self.head.next if self.head else None
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        if current and current.next:
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(n - 1):
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


linked = LinkedList()
linked.push("A")
linked.push("B")
linked.push("C")
print(linked.get(1))
linked.remove(1)
print(linked.get(1))
linked.insert(1, "B")

for i in linked:
    print(i, end=" ")
