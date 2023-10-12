def transpose_matrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=', ')


size = int(input())
matrix = [list(range(1, size + 1)) for _ in range(size)]
print_matrix(matrix)
transpose_matrix(matrix)
print()
print_matrix(matrix)
