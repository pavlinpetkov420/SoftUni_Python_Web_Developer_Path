def make_empty_matrix():
    rows, cols = (int(el) for el in input().split(' '))
    matrix = []
    for _ in range(rows):
        row = [" "] * cols
        matrix.append(row)

    return matrix


def fulfill_matrix(matrix, snake_string):
    row_size = len(matrix)
    last_snake_index = len(snake_string) - 1
    last_str_i = -1
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            if last_str_i == last_snake_index:
                last_str_i = -1
            for str_i in range(last_str_i + 1, len(snake_string)):
                last_str_i = str_i
                matrix[row_i][col_i] = snake_string[str_i]
                break

    for rows in range(len(matrix)):
        if (rows % 2 != 0) and (rows != 0):
            matrix[rows].reverse()

    return matrix


def print_result(snake_matrix):
    for ri in range(len(snake_matrix)):
        print(end='\n')
        for ci in range(len(snake_matrix[ri])):
            print(snake_matrix[ri][ci], end="")


empty_matrix = make_empty_matrix()
snake_string = input()
matrix = fulfill_matrix(empty_matrix, snake_string)
print_result(matrix)