def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


# func(first_name = 'Sushant', last_name = 'Kumar')

# unpacking dictionary
d = {'name': 'Sushant' , 'age' : 17 }
func(**d)