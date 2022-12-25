# exercise
# define a function that take a number (n)
# return a dictionary contaning cube of numbers from 1 to n

# exmaple 
# cube_finder(3)
# {1:1, 2:8, 3:27}
 
x = int(input("Enter any number: "))
def cube_finder(n):
    cube = {}
    for i in range (1, n+1):
        cube[i] = i**3
    return cube
print(cube_finder(x))