"""
Multidimensional lists usage:
    - when dealing with graphics (pixels on the screen are in a grid formation)
    - When working with a tabular data
    - Game development
    - When we need each item of list to be list (it can be list of list of list.. )
Matrix:
    - equal count of columns of each row
    Example:
    matrix1 = [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [23, 14, 9, 3],
    ]
Multidimensional list:
    - each row may have different count of columns
    Example: 2D list
     ml1 = [
        [1, 2, 3],
        [2, 4, 6, 8],
        [23, 14, 9, 3, 14],
    ]
"""

# creating multidimensional lists

list1 = [1, 2, 3]

matrix = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
]



print(matrix, end='\n')

# creating multidimensional list with 0s

matrix = []

rows_count = 3
cols_count = 2

for row_index in range(rows_count):
    row = []
    for col_index in range(cols_count):
        row.append(0)
    matrix.append(row)

print(matrix, end='\n')


matrix2 = [[0]*cols_count for _ in range(rows_count)]

print(matrix2, end='\n')

# creating 5x7 matrix
matrix3 = []

for i in range(6):
    matrix3.append([])
    for j in range(1, 7):
        matrix3[i].append(j)

for row in matrix3:
    print(row, end='\n')


# traversing and manipulating
