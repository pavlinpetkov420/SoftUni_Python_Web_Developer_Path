def age_assignment(*args, **kwargs):
    name_age_dict = {}
    for el in args:
        if el not in name_age_dict.keys():
            name_age_dict[el] = 0

    for letter, age in kwargs.items():
        for key in name_age_dict.keys():
            if key.startswith(letter):
                name_age_dict[key] = age
    return name_age_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))