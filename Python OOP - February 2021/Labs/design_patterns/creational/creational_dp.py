def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


class JsonParser:

    def parse(self, obj):
        return f'json: {str(obj)}'


@singleton
class JsonParser2:

    def parse(self, obj):
        return f'json: {str(obj)}'


print(JsonParser())
print(id(JsonParser()))

print(JsonParser2())
print(id(JsonParser2()))
