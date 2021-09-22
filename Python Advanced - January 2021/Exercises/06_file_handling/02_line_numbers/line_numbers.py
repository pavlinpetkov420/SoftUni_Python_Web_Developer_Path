import re


def get_n(line):
    letter_path = r"[a-z]"
    punctuation_marks = r"[',\.\!\?-]"
    return len(re.findall(letter_path, line, re.IGNORECASE)),\
        len(re.findall(punctuation_marks, line, re.IGNORECASE))


with open("text.txt", "r+") as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letters, n_punctuation = get_n(line)
        print(f"Line {counter}: {line[:-1]} ({n_letters})({n_punctuation})")
        counter += 1