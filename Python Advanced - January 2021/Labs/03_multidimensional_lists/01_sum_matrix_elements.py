def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row_input = list(map(int, input().split(', ')))
        matrix.append(row_input)

    return matrix


matrix = read_matrix()
matrix_sum = 0

for r_index in range(len(matrix)):
    row = matrix[r_index]
    row_sum = 0
    for c_index in range(len(row)):
        el = row[c_index]
        row_sum += el
    matrix_sum += row_sum

print(matrix_sum)
print(matrix)

# there are more than 3 ways to solve it
