def read_matrix():

    rows_cols_count = int(input())
    matrix = []
    for row_index in range(rows_cols_count):
        row_input = list(map(int, input().split(' ')))
        matrix.append(row_input)

    return matrix


def sum_n_print_primary_diagonal(square_matrix):
    primary_diagonal_sum = 0

    for i in range(len(square_matrix)):
        primary_diagonal_sum += square_matrix[i][i]
    return primary_diagonal_sum


def sum_below_primary_diagonal1(square_matrix):
    the_sum = 0
    size = len(square_matrix)
    for r in range(size):
        for c in range(size):
            if c <= r:  # including main diagonal
                # if c < r:   # excluding main diagional
                the_sum += square_matrix[r][c]
    return the_sum


def sum_below_primary_diagonal2(square_matrix):
    the_sum = 0
    size = len(square_matrix)
    for r in range(size):
        for c in range(size):
            if r < c:
                break  # including main diagonal
                # if r <= c:   # excluding main diagional
            the_sum += square_matrix[r][c]
    return the_sum


def sum_below_primary_diagonal3(square_matrix):
    the_sum = 0
    size = len(square_matrix)
    for r in range(size):
        for c in range(r + 1):  # including
            # for c in range(r):  # excluding
            the_sum += square_matrix[r][c]
    return the_sum


def sum_above_primary_diagonal(square_matrix):
    the_sum = 0
    size = len(square_matrix)
    for r in range(size):
        for c in range(r, size):  # including
            # for c in range(r):  # excluding
            the_sum += square_matrix[r][c]
    return the_sum


def sum_n_print_secondary_diagonal(square_matrix):
    primary_diagonal_sum = 0
    size = len(square_matrix)
    for i in range(size):
        primary_diagonal_sum += square_matrix[i][size - i - 1]
    return primary_diagonal_sum



square_matrix = read_matrix()
print(sum_n_print_primary_diagonal(square_matrix))
print(sum_below_primary_diagonal1(square_matrix))
print(sum_below_primary_diagonal2(square_matrix))
print(sum_below_primary_diagonal3(square_matrix))
print(sum_above_primary_diagonal(square_matrix))
print(sum_n_print_secondary_diagonal(square_matrix))