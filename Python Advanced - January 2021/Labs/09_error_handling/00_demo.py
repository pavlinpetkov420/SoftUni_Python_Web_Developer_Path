ll = [1, 2, 3, 4, 5, 6]

"""
        DEFINITION:
    
    
        
    
        COMMON ERROR TYPES:
        
            Syntax Errors - (parsing error) - error in the syntax of the programming language (easy to fix)
            print 'hello' - example
                EOF - End of file error
                
                IndexError - calling a value which is out of bounds
                
                KeyError - wrong or non-existing key
                
                TypeError - inappropriate type passed to an operation or function
                
                ValueError - inappropriate value for passed argument (wrong value -> 'xyz' for int() argument)
                
                NameError - using a variable that does not exist
        
            Exceptions -  (Run Time Error) - errors with syntactically correct programming code
        but the data or operations are incorrect. Errors detected while code parsing are called 
        Exceptions. When it is not handled it result error messages    
                
                
            
    
        
        
"""


def avg(numbers):
    return sum(numbers) / len(numbers)


print(avg(ll))

# ZeroDivision
# ll = []
# print(avg(ll))

# NameError
# print(name)

# TypeError
# print('2' + 2)

ll = [1, 2, 3]
n = len(ll)
for i in range(-n, n):
    print(ll[i])


"""
    CUSTOM EXCEPTION
    
    define a class which raise ERRORS
    and inheritance Exception/Error class
"""

#
# class ValueCannotBeNegative(Exception):
#     def __init__(self, value):
#         super().__init__(f"{value} is negative")
#
#
# for i in range(5):
#     number = int(input())
#     if number < 0:
#         raise ValueCannotBeNegative(number)


"""
        TRY/EXCEPT CONSTRUCTION
            When we except error, we handle it and our code don't break is execution
            
        try statement - there is a code which can have exception. Try catch the exception
        and execute the block of code in except. If there isn't exception we skip it
"""