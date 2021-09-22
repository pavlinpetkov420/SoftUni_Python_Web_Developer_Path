def reverse_text(text):

    for index in range(len(text) - 1, -1, -1):
        yield text[index]


for char in reverse_text("step"):
    print(char, end='')
