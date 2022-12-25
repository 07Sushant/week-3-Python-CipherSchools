# formkeys
# d = {'name': 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name','age','height'], 'unknown')
# print(d)

#  get method(useful)
d ={'name':'Sushant', 'age': 17}
print(d['name'])

print(d.get('name')) #none if no exist


if 'name' in d:
    print("Present")
else:
    print("Not Present")

if d.get('name'):
    print("Present")
else:
    print("Not Present")

# d.clear()
# print(d)

d1 = d.copy()
print(d1)