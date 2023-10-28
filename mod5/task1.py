#task1
class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end == None:
            return None
        else:
            remov = self.end
            self.end = self.end.pref
            remov.pref = None
            return remov.data

    def push(self, val):
        if self.end == None:
            self.end = Node(val)
        else:
            new = Node(val)
            new.pref = self.end
            self.end = new

    def print(self):
        current = self.end
        if self.end == None:
            print('Стек пуст')
        else:
            while (current != None):
                print(current, end = " ")
                current = current.pref
                if current is None:
                    print('\n')