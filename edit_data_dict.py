user_info ={
    'name' : 'sushant',
    'age' : 24,
    'list1' : ['S' ,'U','S','H','A','N','T'],
}



#  how to add  data
# user_info['fav_game'] = ['warzone', 'NFS']
# print(user_info)

# pop method in 
# poped_item = user_info.pop('age')
# print(f"poped_item is {poped_item}")
# print(user_info)


# popitem method
poped_item = user_info.popitem()
print(user_info)
print(type(poped_item))