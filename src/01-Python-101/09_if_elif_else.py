# if-elif-else conditionals
x = 10
y = 20

if x > y:                               # if x is greater than y
    print ("x is greater than y")       # print x is greater than y
elif x < y:                             # if x is less than y
    print ("x is less than y")          # print x is less than y
else:                                   # if x is equal to y
    print ("x is equal to y")           # print x is equal to y

# Nested if-elif-else conditionals
x = 10
y = 20
z = 30

if x > y:                               # if x is greater than y
    if x > z:                           # if x is greater than z
        print ("x is greater than y and z") # print x is greater than y and z
    else:                               # if x is not greater than z
        print ("x is greater than y but not z") # print x is greater than y but not z
elif x < y:                             # if x is less than y
    if x < z:                           # if x is less than z
        print ("x is less than y and z") # print x is less than y and z
    else:                               # if x is not less than z
        print ("x is less than y but not z") # print x is less than y but not z
else:                                   # if x is equal to y
    if x == z:                          # if x is equal to z
        print ("x is equal to y and z") # print x is equal to y and z
    else:                               # if x is not equal to z
        print ("x is equal to y but not z") # print x is equal to y but not z