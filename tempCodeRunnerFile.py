def adder(*args):
    add = 0
    for i in args:
        add += i
    return adder
print(adder(1,2,3,4,5))