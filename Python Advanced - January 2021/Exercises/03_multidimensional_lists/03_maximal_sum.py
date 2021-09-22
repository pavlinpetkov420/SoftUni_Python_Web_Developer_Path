# TODO: NEED A FIX 60/100 -> -40 RUNTIME ERROR

def read_matrix(rows, cols):
    matrix = []
    for row in range(rows):
        row_input = [int(el) for el in input().split(' ')]
        matrix.append(row_input)

    return matrix


def get_sum_of_subm(row_i, col_i, matrix, size):
    subm_sum = 0
    for r in range(row_i, row_i + size):
        for c in range(col_i, col_i + size):
            subm_sum += matrix[r][c]

    return subm_sum


def get_best_subm_sum_coordinates(matrix, SUBM_SIZE):
    best_r_index, best_c_index = 0, 0
    best_sum = 0
    for ri in range(rows - 2):
        for ci in range(cols - 2):
            current_sum = get_sum_of_subm(ri, ci, matrix, SUBM_SIZE)
            if current_sum > best_sum:
                best_sum = current_sum
                best_r_index = ri
                best_c_index = ci

    return (best_r_index, best_c_index)


def print_result(best_sum_n_coordinates, size):
    row_index, col_index = best_sum_n_coordinates
    print(f"Sum = {get_sum_of_subm(row_index, col_index, matrix, SUBMATRIX_SIZE)}")
    for r in range(row_index, row_index + size):
        if r != row_index:
            print(end="\n")
        for c in range(col_index, col_index + size):
            print(matrix[r][c], end=" ")


rows, cols = (int(el) for el in input().split(' '))
matrix = read_matrix(rows, cols)

SUBMATRIX_SIZE = 3
print_result(get_best_subm_sum_coordinates(matrix, SUBMATRIX_SIZE), SUBMATRIX_SIZE)
