#  define a function that take list of string and reverse of every sting 
# using comprehenshion 

# Exmaple:
# l = ['ABC', 'XYZ', "VUT"]
# revese_string(l) ['CBA', 'ZYX', 'TUV']

def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(['ABC', 'XYZ', "VUT"]))    

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_str(['ABC', 'XYZ', "VUT"]))

# Sushant
