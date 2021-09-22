def reverse_string():
    stack = []
    text = input()

    for symbol in text:
        stack.append(symbol)

    while stack:
        print(stack.pop(), end="")

reverse_string()