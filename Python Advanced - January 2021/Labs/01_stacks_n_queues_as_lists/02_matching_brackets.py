def extract_subexpressions(expression):
    stack = []
    for index in range(len(expression)):
        if expression[index] == "(":
            stack.append(index)
        elif expression[index] == ")":
            start_index = stack.pop()
            end_index = index + 1
            print(expression[start_index: end_index])


expression = input()

extract_subexpressions(expression)