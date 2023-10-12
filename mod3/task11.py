def decide_winner(field):
    k = len(field)
    for row in field:
        if len(set(row)) == 1 and row[0] != '_':
            return row[0]
    for j in range(k):
        if len({field[i][j] for i in range(k)}) == 1 and field[0][j] != '_':
            return field[0][j]
    if len({field[i][i] for i in range(k)}) == 1 and field[0][0] != '_':
        return field[0][0]
    if len({field[i][-i - 1] for i in range(k)}) == 1 and field[0][-1] != '_':
        return field[0][-1]
    return '_'
with open('input11.txt') as file:
    field = [line.strip() for line in file]
    print(decide_winner(field))
