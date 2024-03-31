# input() function with str() function
name = str(input("May I know your name please: ")) # prompt user to enter their name
# method 1
print ("Hello " + name) # print greeting message using concatenation
# method 2
print ("Hello", name) # print greeting message no concatination

################################################################################################

# input() function takes input as string
age = input("May I know your age please: ") # prompt user to enter their age
print ("Your age is " + age) # print age

# input() function with int() function
age = int(input("May I know your age please: ")) # prompt user to enter their age
print ("Your age is " + str(age)) # print age

# input() function with float() function
weight = float(input("May I know your weight please: ")) # prompt user to enter their weight
print ("Your weight is " + str(weight)) # print weight

# input() function with bool() function
married = bool(input("Are you married (y/n): ")) # prompt user to enter their marital status
print ("Marital Status: " + str(married)) # print marital status

# input() function with list() function
hobbies = list(input("Enter your hobbies (separated by comma): ").split(","))
print ("Hobbies: " + str(hobbies)) # print hobbies

# input() function with set() function
hobbies = set(input("Enter your hobbies (separated by comma): ").split(","))
print ("Hobbies: " + str(hobbies)) # print hobbies

# input() function with tuple() function
hobbies = tuple(input("Enter your hobbies (separated by comma): ").split(","))
print ("Hobbies: " + str(hobbies)) # print hobbies

# input() function with dict() function
hobbies = dict(input("Enter your hobbies (separated by comma): ").split(","))
print ("Hobbies: " + str(hobbies)) # print hobbies

################################################################################################