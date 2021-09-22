"""
        TRY/EXCEPT CONSTRUCTION
            When we except error, we handle it and our code don't break is execution

        try statement - there is a code which can have exception. Try catch the exception
        and execute the block of code in except. If there isn't exception we skip it

        ORDER DOES MATTER!!!
"""

import traceback


def raise_exception(ExceptionType):
    raise ExceptionType("My Exception")


try:
    raise_exception(TypeError)
# except (TypeError, ValueError):
#     print("TypeError or ValueError")

except TypeError as err:
    print("Handled with TypeError: ", err)
    traceback.print_tb(err.__traceback__)
except Exception:
    print("Handled in Exception")
except:
    print("Handled in except")
print("It is still ALIVE!")
# try:
#     raise_exception(ValueError)
# except Exception as err:
#     if type(err) == TypeError:
#         print("Handled with TypeError: ", err)
#     elif type(err) == ValueError:
#         print("Handled with ValueError")


# try:
#     x = int(input())
#     print(x+1)
# except:
#     print("Not a number")
