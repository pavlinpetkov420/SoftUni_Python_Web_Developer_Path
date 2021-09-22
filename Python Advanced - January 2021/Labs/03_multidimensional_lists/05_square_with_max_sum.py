def read_matrix():

    (rows_count, columns_count) = map(int, input().split(' '))
    matrix = []
    for row_index in range(rows_count):
        row_input = list(map(int, input().split(' ')))
        matrix.append(row_input)

    return matrix


def get_sum_of_submatrix(matrix, row_index, col_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(col_index, col_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE):
    best_row_index = 0
    best_col_index = 0
    best_sum = get_sum_of_submatrix(matrix, best_row_index, best_col_index, SUBMATRIX_SIZE)

    for row_index in range(len(matrix) - SUBMATRIX_SIZE + 1):
        for col_index in range(len(matrix[row_index]) - SUBMATRIX_SIZE + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, SUBMATRIX_SIZE)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_col_index = col_index
    return (best_row_index, best_col_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    sum = 0
    for r in range(row_index, row_index + size + 1):
        row = []
        for c in range(col_index, col_index + size + 1):
            row.append(matrix[r][c])
        print(" ".join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, size))


SUBMATRIX_SIZE = 2

matrix = read_matrix()
coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
print_result(coordinates, SUBMATRIX_SIZE)
