def find_min(numbers_stack):
    min_number = 110
    for el in numbers_stack:
        if el < min_number:
            min_number = el
    if min_number != 110:
        print(min_number)


def find_max(numbers_stack):
    max_number = 0
    for el in numbers_stack:
        if el > max_number:
            max_number = el
    if max_number != 0:
        print(max_number)


def main():
    number_of_commands = int(input())
    numbers_stack = []
    PUSH_COMMAND = 1
    DELETE_COMMAND = 2
    PRINT_MAX = 3
    PRINT_MIN = 4
    for count in range(number_of_commands):
        user_command = input().split()
        cmd = int(user_command[0])

        if cmd == PUSH_COMMAND:
            # push/append element into the stack
            number = int(user_command[1])
            numbers_stack.append(number)
        elif cmd == DELETE_COMMAND:
            # delete/pop element from the stack
            if numbers_stack:
                numbers_stack.pop()
        elif cmd == PRINT_MAX:
            # find max number and print it
            find_max(numbers_stack)
        else:
            # find min number and print it
            find_min(numbers_stack)

    while numbers_stack:
        if len(numbers_stack) == 1:
            print(numbers_stack.pop())
            break
        print(numbers_stack.pop(), end=', ')


main()
