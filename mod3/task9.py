N = int(input())
with open('output9.txt', 'w') as file:
    size = 1
    c = 0
    x = y = 0
    dx, dy = -1, 0
    directions = {
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0)
    }
    for _ in range(N):
        x += dx
        y += dy
        c += 1
        if c == size:
            dx, dy = directions[(dx, dy)]
            c = 0
            if (dx, dy) == (1, 0) or (dx, dy) == (-1, 0):
                size += 1
    file.write(f'{x} {y}')
