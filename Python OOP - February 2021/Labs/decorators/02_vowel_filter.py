def vowel_filter(func):

    vowels = set('aeiou').union('aeiou'.upper())

    def wrapper():

        result = func()
        return [c for c in result if c in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

@vowel_filter
def get_hello_message():
    return 'Hello I am '


@vowel_filter
def get_current_temperature():
    return '3 degrees Celsius'


print(get_hello_message())
print(get_current_temperature())

