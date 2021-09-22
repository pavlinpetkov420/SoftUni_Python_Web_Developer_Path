text = input().lower()
VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)
result = [x for x in text if x not in VOWELS]
print("".join(result))