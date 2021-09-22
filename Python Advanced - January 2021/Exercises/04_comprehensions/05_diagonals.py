def read_matrix():
    rows = int(input())
    matrix = [list(map(int, input().split(', '))) for n in range(rows) for _ in range(n)]
    return matrix


def find_diagonals(matrix):
    diagonal_sum = 0
    anti_diagonal_sum = 0
    matrix_size = len(matrix)

    primary_diagonal, anti_diagonal = [], []
    # sum of primary diagonal elements and anti diagonal
    col_index = matrix_size - 1
    for index in range(matrix_size):

        primary_diagonal.append(matrix[index][index])
        anti_diagonal.append(matrix[index][col_index])
        col_index -= 1

    return primary_diagonal, anti_diagonal


def print_result(fist_diagonal, second_diagonal):
    fd_output, ad_output = "First diagonal: ", "Second diagonal: "
    for index in range(len(first_diagonal)):
        if index == len(fist_diagonal) - 1:
            fd_output += f"{first_diagonal[index]}. "
            ad_output += f"{second_diagonal[index]}. "
            break
        fd_output += f"{first_diagonal[index]}, "
        ad_output += f"{second_diagonal[index]}, "

    fd_output += f"Sum: {sum(fist_diagonal)}"
    ad_output += f"Sum: {sum(second_diagonal)}"

    print(fd_output)
    print(ad_output)


matrix = read_matrix()
first_diagonal, second_diagonal = find_diagonals(matrix)
print_result(first_diagonal, second_diagonal)
