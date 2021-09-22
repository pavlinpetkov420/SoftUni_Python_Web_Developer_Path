def input_lines(count):
    lines = []
    for _ in range(count):
        ch_elements = input().split()
        if len(ch_elements) > 1:
            for el in ch_elements:
                lines.append(el)
        else:
            lines.append(ch_elements[0])

    return lines


def filter_n_print_unique_elements(chemical_elements):
    unique_elements = sorted(set(chemical_elements))
    for el in unique_elements:
        print(el)


chemical_elements = input_lines(int(input()))
filter_n_print_unique_elements(chemical_elements)