def input_lines(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_usernames(unique_usernames):
    for username in unique_usernames:
        print(username)


def find_unique(users):
    unique_usernames = set(users)
    print_usernames(unique_usernames)


usernames = input_lines(int(input()))
find_unique(usernames)


