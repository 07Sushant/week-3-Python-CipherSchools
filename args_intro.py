# make flexiable functions
# operator 
# args

# def total(a,b):
#     return a+b
# print(total(2,3))


# def all_toral(*args):
#     print(args)

# all_toral(1,2,3,4,5,65)


def totals(*args):
    totals = 0
    for num in args:
        totals += num
    return totals
print(totals(1,2,3,4))