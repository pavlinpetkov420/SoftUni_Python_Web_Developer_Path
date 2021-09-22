def read_matrix(rows, cols):

    matrix = []
    for row_index in range(rows):
        row_input = [el for el in input().split(' ')]
        matrix.append(row_input)

    return matrix


def check_equal_chars(matrix, row_index, col_index, sub_matrix_size):
    subm = []
    for ri in range(row_index, row_index + sub_matrix_size):
        for ci in range(col_index, col_index + sub_matrix_size):
            subm.append(matrix[ri][ci])

    set_len = len(set(subm))
    if set_len == 1:
        return 1
    else:
        return 0


def get_2x2_sub_matrix_coordinates(matrix, rows, cols):
    equal_sub_matrix_counter = 0
    for row_index in range(rows - 1):
        for col_index in range(cols - 1):
            equal_sub_matrix_counter += check_equal_chars(matrix, row_index, col_index, sub_matrix_size=2)
    return equal_sub_matrix_counter


rows, cols = (int(el) for el in input().split(' '))
char_matrix = read_matrix(rows, cols)
print(get_2x2_sub_matrix_coordinates(char_matrix, rows, cols))
