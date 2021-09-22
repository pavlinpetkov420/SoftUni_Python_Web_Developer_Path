import re

email = 'pavlinpetkov771@gmail.com'
pattern = r"(?P<username>[A-Za-z0-9]+)@(?P<mail>[a-z]+)\.(?P<domain>[a-z]+)"

match = re.finditer(pattern, email)
result = ()
for el in match:
    result += el.group()

print(result)
