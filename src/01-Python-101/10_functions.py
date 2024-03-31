# - Defining a function
def add(x, y):
    return x + y

# - Calling a function
add (1, 2)
print (add (1, 2))

# - Passing arguments
print (add ("Irfan", "Manzoor"))

# - Returning values
def add(x, y):
    return x + y

# - Local scope
def add(x, y):
    x = x + 1
    y = y + x
    return x + y

print (add(3, 6))

# - Global scope
global x
def add(x, y):
    x = x + 1
    y = y + x
    return x + y

print (add(6, 9))

# Age calculator function with user input
def age_calculator():
    year = int(input("Enter your year of birth: "))
    age = 2022 - year
    print ("Your age is: " + str(age))

print (age_calculator())

# Birth year predictor function with user input
def age_predictor():
    age = int(input("Enter your age: "))
    year = 2022 - age
    print ("Your year of birth is: " + str(year))

print (age_predictor())

# lambda function
add = lambda x, y: x + y
print (add(1, 2))

# lambda function with multiple arguments
add = lambda x, y, z: x + y + z
print (add(1, 2, 3))