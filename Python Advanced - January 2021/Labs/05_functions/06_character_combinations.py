from itertools import permutations
# returns iter object


def permute(text, current_index=0):
    if current_index == len(text):
        print("".join(text))
        return

    for index in range(current_index, len(text)):
        text[current_index], text[index] = text[index], text[current_index]
        permute(text, current_index+1)
        text[current_index], text[index] = text[index], text[current_index]


text = list(input())
permute(text)

print([f'{"".join(el)}' for el in list(permutations(text))])