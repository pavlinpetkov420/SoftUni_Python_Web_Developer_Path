import re


def take_even_lines():

    with open("text.txt", "r") as file:
        lines = file.readlines()
        for row_number in range(len(lines)):
            if row_number % 2 == 0:
                replaced = replace_special_symbols(lines[row_number]).split()
                print(*[el for el in replaced[::-1]])


def replace_special_symbols(line):
    return re.sub(r"[?!,.-]", "@", line)


take_even_lines()
