def multiply_nums(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply
print(multiply_nums(1,2,3,4,2))