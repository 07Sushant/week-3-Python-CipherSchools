user_info ={
    'name' : 'sushant',
    'age' : 24,
    'list1' : ['S' ,'U','S','H','A','N','T'],
}

# checking if keyword exist in dict or not

# if 'name' in user_info:
#     print("present")
# else:
#     print("Not present")


# check if value exist in dict or not 
# if 'sushant1' in user_info.values():  #//false krdiya so age print krdegi meri 
#     print("Present")
# else:                                    #values method
#     print("Your age is 17")

#loop in dictionary
# for i in user_info.values():
#     print(i)

# values method 
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))


# keys method
# user_info_keys = user_info.values()
# print(user_info_keys)
# print(type(user_info_keys))


# item method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

#why items method
for key, value in user_info.items():
    print(f"keys is {key} and value is {value}")





