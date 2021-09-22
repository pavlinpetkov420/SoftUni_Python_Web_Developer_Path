words = [w for w in input().split(', ')]
result = [f"{w} -> {len(w)}" for w in words]
print(", ".join(result))
