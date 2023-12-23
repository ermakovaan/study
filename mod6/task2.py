class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        """
        Возвращает следующую пару элементов из списка.
        Если достигнут конец списка, возвращает пару с последним элементом и None.
        """
        if self.index < len(self.lst):
            pair = (
                self.lst[self.index],
                self.lst[self.index + 1] if self.index + 1 < len(self.lst) else None
            )
            self.index += 2
            return pair
        else:
            raise StopIteration

    def __iter__(self):
        """
        Возвращает самого себя в качестве итератора.
        """
        return self


if __name__ == '__main__':
    dL = DoubleElement(1, 2, 3, 4)
    for pair in dL:
        print(pair)

    dL = DoubleElement(1, 2, 3, 4, 5)
    for pair in dL:
        print(pair)
