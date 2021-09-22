n = int(input())
rows = n
columns = n
matrix = [(list(map(int, input().split(', ')))) for i in range(rows)]
first_diagonal = [matrix[i][i] for i in range(rows)]
second_diagonal = [matrix[i][n - i - 1] for i in range(rows)]
print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")