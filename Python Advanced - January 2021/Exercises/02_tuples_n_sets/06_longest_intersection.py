n = int(input())

intersections = []

# 1st solution
# for _ in range(n):
#     data = input()
#     first_seq_data, second_seq_data = data.split('-')
#     start, stop = [int(el) for el in first_seq_data.split(',')]
#     first_sequence = range(start, stop + 1)
#     start, stop = [int(el) for el in second_seq_data.split(',')]
#     second_sequence = range(start, stop + 1)
#
#     intersection = set(first_sequence).intersection(second_sequence)
#     intersections.append(intersection)

# 2nd solution
for _ in range(n):
    data = input()
    first_seq_data, second_seq_data = data.split('-')
    start_1, stop_1 = [int(el) for el in first_seq_data.split(',')]
    start_2, stop_2 = [int(el) for el in second_seq_data.split(',')]

    intersection = range(max(start_1, start_2), min(stop_1 + 1, stop_2 + 1))
    intersections.append(intersection)


longest = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest)} with length {len(longest)}")


