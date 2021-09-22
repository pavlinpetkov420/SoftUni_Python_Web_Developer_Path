countries = input().split(', ')
capital_cities = input().split(', ')

country_capital = zip(countries, capital_cities)

result = {k: v for k, v in country_capital}

for k, v in result.items():
    print(f"{k} -> {v}")
