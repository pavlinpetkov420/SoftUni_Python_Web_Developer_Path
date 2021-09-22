def print_result(symbol_count_dict):
    symbol_count_dict = dict(sorted(symbol_count_dict.items(), key=lambda x: x[0]))
    for symbol, count in symbol_count_dict.items():
        print(f"{symbol}: {count} time/s")


def count_chars():
    text = input()
    chars_tuple = tuple(text)

    symbol_count_dict = {}
    for ch in chars_tuple:
        if ch not in symbol_count_dict.keys():
            symbol_count_dict[ch] = chars_tuple.count(ch)

    print_result(symbol_count_dict)


count_chars()