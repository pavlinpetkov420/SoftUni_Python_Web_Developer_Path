def read_square_matrix():
    row_cols_count = int(input())
    matrix = []
    for ri in range(row_cols_count):
        row = [x for x in input()]
        matrix.append(row)
    return matrix


def find_searched_symbol(square_matrix, searched_symbol):

    rows_cols_count = len(square_matrix)
    for row_index in range(rows_cols_count):
        row_len = len(square_matrix[row_index])
        for col_index in range(row_len):
            if square_matrix[row_index][col_index] == searched_symbol:
                return (row_index, col_index)


def print_result(result, searched_symbol):
    if result:
        print(result)
    else:
        print(f"{searched_symbol} does not occur in the matrix")


square_matrix = read_square_matrix()
searched_symbol = input()
print_result(find_searched_symbol(square_matrix, searched_symbol), searched_symbol)
