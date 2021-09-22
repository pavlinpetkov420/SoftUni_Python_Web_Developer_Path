def read_next(*args):
    sequence = args
    for el in sequence:
        if isinstance(el, dict):
            for key in el.keys():
                yield key
        else:
            for item in el:
                yield item


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')

