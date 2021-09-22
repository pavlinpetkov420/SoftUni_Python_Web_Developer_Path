def read_str_matrix(rows):
    matrix = []
    for _ in range(rows):
        row = [el for el in input().split()]
        matrix.append(row)

    return matrix


def shuffle_elements(matrix):
    END_CMD = 'END'
    while True:
        cmd = input()
        if cmd == END_CMD:
            return

        command_elements = cmd.split()
        if (command_elements[0] == "swap") and (len(command_elements) == 5):
            command_elements.pop(0)
            are_digits = digits_validation(command_elements)
            if are_digits:
                coordinates = [int(el) for el in command_elements]
                are_indices_valid = index_validation(coordinates, matrix)
                if are_indices_valid:
                    matrix = shuffle_values_on_coordinates(matrix, coordinates)
                    print_matrix(matrix)
                    continue
        print("Invalid input!")


def index_validation(coordinates, matrix):
    r1, c1, r2, c2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    if (0 <= r1 <= len(matrix)) and (0 <= c1 <= len(matrix[r1])):
        if (0 <= r2 <= len(matrix)) and (0 <= c2 <= len(matrix[r2])):
            return True
    return False


def digits_validation(command_elements):
    are_digits = False
    for el in command_elements:
        if el.isdigit():
            continue
        else:
            return are_digits
    are_digits = True
    return are_digits


def shuffle_values_on_coordinates(matrix, coordinates):
    r1, c1, r2, c2 = coordinates
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    return matrix


def print_matrix(matrix):
    for r in range(len(matrix)):
        if r != 0:
            print(end='\n')
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')
    print(end='\n')


rows, cols = (int(el) for el in input().split())
matrix = read_str_matrix(rows)
shuffle_elements(matrix)
