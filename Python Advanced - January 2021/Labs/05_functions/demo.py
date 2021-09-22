"""
Functions must have one purpose
Lambda functions - anonymous function for one time execution
lambda parameter/s: expression
"""

"""
*args & **kwargs
*args(arguments) - pack tuple as argument which can be unlimited count.
with * in front of args we pack and use it in the function

**kwargs(keyword arguments) - pack dictionary as argument
double * is for packing a key->value pairs
"""


def sum_nums(a, b, *args):
    # a, b are mandatory arguments
    print(sum(args))


sum_nums(1, 2)
# if we have only args & call the the function without arguments it will return 0 -> empty tuple
sum_nums(0, 0)


def get_info(**kwargs):
    if kwargs.get("name"):
        print(kwargs["name"])
    else:
        print("No name here")


get_info(age=26, g="f", name="Pavlin")

"""
    RECURSION - process that function that calls itself
    recursive function - function that calls itself
    STRUCTURE:
    - base case - the bottom case, that will stop the recursion
    - recursive case - case that make the recursion

"""


def say_hello_n_times(times):
    if times <= 0:
        return
    print("Recursion TIME!")
    say_hello_n_times(times-1)


say_hello_n_times(6)


"""
    COMBINATIONS
    [1, 2, 3] - numbers
    combination on pairs
    
            [1, 2, 3]
    
        [1]             [2]
    [1, 2]  [1, 3]    [2, 3]
    Example at 07_chairs
"""

"""
        PERMUTATIONS
        calculates with n-factorial
                                                [A, B, C]
                                                main list
                1.swap A with A                   4.swap A with B                       7.swap A with C
                [A, B, C]                         [B, A, C]                             [C, B, A]
        
        2.swap B with B   3.swap B with C   5.swap A with A   6.swap A with C       8.swap B with B     9.swap B with A
        [A, B, C]       [A, C, B]           [B, A, C]         [B, C, A]             [C, B, A]           [C, A, B]
"""