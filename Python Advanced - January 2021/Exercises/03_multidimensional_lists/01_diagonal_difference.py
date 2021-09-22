def read_square_matrix():
    matrix_size = int(input())
    matrix = []

    for r in range(matrix_size):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


def get_sum_of_primary_diagonal_and_anti_diagonal(matrix):
    diagonal_sum = 0
    anti_diagonal_sum = 0
    matrix_size = len(matrix)

    # sum of primary diagonal elements and anti diagional
    col_index = matrix_size - 1
    for index in range(matrix_size):
        diagonal_sum += matrix[index][index]
        anti_diagonal_sum += matrix[index][col_index]
        col_index -= 1

    return abs(diagonal_sum - anti_diagonal_sum)


print(get_sum_of_primary_diagonal_and_anti_diagonal(read_square_matrix()))
