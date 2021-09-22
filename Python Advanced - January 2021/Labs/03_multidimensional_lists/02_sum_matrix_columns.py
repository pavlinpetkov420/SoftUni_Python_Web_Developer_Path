def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row_input = [int(x) for x in input().split(' ')]
        matrix.append(row_input)
    return matrix


def get_columns_sums(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    sums = []
    for column_index in range(columns_count):
        sums.append(0)
        for row_index in range(rows_count):
            sums[-1] += matrix[row_index][column_index]
    # sums = [0] * columns_count
    # for row_index in range(rows_count):
    #     for column_index in range(columns_count):
    #         sums[column_index] += matrix[row_index][column_index]

    return sums


def print_results(values):
    [print(x) for x in values]


matrix = read_matrix()
result = get_columns_sums(matrix)
print_results(result)
