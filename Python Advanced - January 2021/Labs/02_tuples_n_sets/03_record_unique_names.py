inputs_count = int(input())

names = []
for _ in range(inputs_count):
    names.append(input())

unique_names = set(names)

print("\n".join(unique_names))
