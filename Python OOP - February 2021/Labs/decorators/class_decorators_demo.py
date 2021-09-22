import functools

# def repeat(count):
#
#     # this is just a demo code :) from student question
#
#     class decorator:
#
#         def __init__(self, func):
#             self.func = func
#
#         def __call__(self, *args, **kwargs):
#             for _ in range(count):
#                 self.func(*args, **kwargs)
#     return decorator

#
# @repeat(10)
# def print_msg():
#     print('Some Repeatable MessaGe!')


"""
Class decorators are with lower case names!!!
They are used when we save some state
"""

class cache:

    def __init__(self, func):
        self.func = func
        self.internal_cache = {}

    def __call__(self, *args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key not in self.internal_cache:
            self.internal_cache[cache_key] = self.func(*args, **kwargs)

        return self.internal_cache[cache_key]


class uppercase:

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()


class logger:
    log_file_path = './log.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        args_str = ', '.join(args)
        kwargs_str = ', '.join(f'{key}={value}' for (key, value) in kwargs.items())
        result = self.func(*args, **kwargs)
        with open(self.log_file_path, 'a') as file:
            file.write(f'{self.func.__name__}({args_str, kwargs_str}) returned {result}\n')
        return result


@uppercase
@logger
def get_msg():
    return 'asdasda'


print(get_msg())
