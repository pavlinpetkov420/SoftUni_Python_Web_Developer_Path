class dictionary_iter:

    def __init__(self, dic_object):
        self.dic_object = dic_object
        self.dict_keys = list(self.dic_object)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict_keys):
            raise StopIteration
        key = self.dict_keys[self.index]
        value = self.dic_object[self.dict_keys[self.index]]
        self.index += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
