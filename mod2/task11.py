cycle = input("Введите цифры (через пробел): ")
mark = False
for i in range(len(cycle)):
    for j in range(i + 1, len(cycle)):
        if cycle[i] == cycle[j] and cycle[i] != ' ':
            mark = True
            break
    if mark:
        break
print(mark)