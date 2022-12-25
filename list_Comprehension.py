# with the help of list comprehension we cann create list in one line

# create list of square form 1 to 10
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)


# square2 = [i**2 for i in range(1,11)]
# print(square2)


negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

# comprehension
# neagtive = [-i for i in range(1,11)]
# print(negative)

names = ['Sushant', 'Kumar', 'Prashant']
# new_list = ['S', 'K' , 'P']

new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

new_list2 = [name[0] for name in names]
print(new_list2)
