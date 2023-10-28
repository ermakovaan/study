#task2
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        else:
            remove = self.start.nref
            self.start = self.start.nref
            self.start.pref = None
            return remove

    def push(self, val):
        if self.end is None:
            self.start = Node(val)
            self.end = self.start
        else:
            self.end.nref = Node(val)
            self.end.nref.pref = self.end
            self.end = self.end.nref

    def insert(self, n, val):
        if n > self.length():
            return "Недопустимый индекс"
        ind = 0
        current = self.start
        while (ind != n-1):
            current = current.nref
            ind += 1
        inserte = Node(val)
        inserte.pref = current
        inserte.nref = current.nref
        current.nref.pref = inserte
        current.nref = inserte

    def length(self):
        current = self.start
        length = 0
        while current is not None:
            length = length + 1
            current = current.nref
        return length

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
            if current is None:
                print('\n')