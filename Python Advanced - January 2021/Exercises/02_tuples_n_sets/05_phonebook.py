def gather_data():
    phone_book = {}
    searches_count = 0
    while True:
        line = input()
        if line.isdigit():
            searches_count = int(line)
            break
        name, phone_number = line.split('-')
        phone_book[name] = phone_number

    searches = []
    for _ in range(searches_count):
        searches.append(input())

    return phone_book, searches


def search_contacts(phonebook, searches):
    for name in searches:
        if phonebook.get(name):
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"Contact {name} does not exist.")


phonebook, searches = gather_data()
search_contacts(phonebook, searches)