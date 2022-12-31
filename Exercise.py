user = {}
name = input("Entery your name: ")
age = int(input("Enter your age: "))
fav_games = input("Your Favourite game seperated by commas ").split(",")

user['name'] = name
user['age'] = age
user['fav_hames'] = fav_games

for key , value in user.items():
    print(f"{key} :  {value}")