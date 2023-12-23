class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val) -> None:
        """
        Добавляет элемент в конец списка.
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index: int) -> (int, None):
        """
        Получает элемент по индексу.
        """
        if index < 0 or not self.head:
            return None

        current = self.head
        for i in range(index):
            if current.next:
                current = current.next
            else:
                return None

        return current.value

    def remove(self, index: int) -> None:
        """
        Удаляет элемент по индексу.
        """
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        for i in range(index):
            prev = current
            current = current.next
            if not current:
                return

        prev.next = current.next

    def insert(self, n: int, val) -> None:
        """
        Вставляет элемент val между элементами с номерами n-1 и n.
        """
        new_node = Node(val)

        if n <= 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(n - 1):
            if current:
                current = current.next
            else:
                return

        if not current:
            return

        new_node.next = current.next
        current.next = new_node

    def display(self) -> None:
        """
        Выводит элементы списка.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(5):
        linked_list.push(val=5)

    linked_list.display()

    linked_list.insert(n=3, val='SomeStrValue')
    linked_list.display()

    linked_list.remove(index=1)
    linked_list.display()

    print(linked_list.get(index=2))

    for el in linked_list:
        print(f'Iter element: {el}')
