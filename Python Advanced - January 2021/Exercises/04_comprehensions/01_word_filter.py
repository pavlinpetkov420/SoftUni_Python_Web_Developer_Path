words = [w for w in input().split()]
even_len_words = [x for x in words if len(x) % 2 == 0]
print("\n".join(even_len_words))