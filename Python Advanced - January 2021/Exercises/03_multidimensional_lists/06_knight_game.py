# TODO UNDERSTAND THE LOGIC !!! :))


def read_matrix(board_size):
    matrix = []
    for _ in range(board_size):
        matrix.append(list(input()))

    return matrix


def is_valid_bound(row, col):
    if (0 <= row <= square_size - 1) and (0 <= col <= square_size - 1):
        return True
    return False


def calculate_kills(board, row_index, col_index):
    kills = 0
    # rows & cols lists are possible moves of knights
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]

    for index in range(len(rows)):
        potential_row = row_index + rows[index]
        potential_col = col_index + cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = board[potential_row][potential_col]
            if potential_position == "K":
                kills += 1

    return kills


def find_the_horse(board):

    size = len(board)

    removed_counter = 0
    while True:
        max_kills = 0
        killer_position = []

        for row_index in range(size):
            for col_index in range(len(board[row_index])):
                if board[row_index][col_index] == "K":
                    kills_count = calculate_kills(board, row_index, col_index)
                    if kills_count > max_kills:
                        max_kills = kills_count
                        killer_position = [row_index, col_index]

        if killer_position:
            board[killer_position[0]][killer_position[1]] = "0"
            removed_counter += 1
        else:
            break

    print(removed_counter)


square_size = int(input())
game_board = read_matrix(square_size)
find_the_horse(game_board)
