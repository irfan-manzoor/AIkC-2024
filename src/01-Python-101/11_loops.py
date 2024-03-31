# while loop
x = 0                           # loop variable
while x < 10:                   # loop condition
    print ("x = " + str(x))     # print x
    x = x + 1                   # increment x

###################################################

# for loop
for x in range(10):             # loop variable
    print ("x = " + str(x))     # print x

# for loop with range
for x in range(10):             # loop variable
    print ("x = " + str(x))     # print x

# for loop with range with step
for x in range(0, 10, 2):       # loop variable
    print ("x = " + str(x))     # print x

# for loop with range with negative step
for x in range(10, 0, -1):      # loop variable
    print ("x = " + str(x))     # print x

###################################################

# for loop with list
for x in [1, 2, 3]:             # loop variable
    print ("x = " + str(x))     # print x

# for loop with tuple
for x in (1, 2, 3):             # loop variable
    print ("x = " + str(x))     # print x

# for loop with string
for x in "hello":               # loop variable
    print ("x = " + str(x))     # print x

# for loop with set
for x in {1, 2, 3}:             # loop variable
    print ("x = " + str(x))     # print x

# for loop with dict
for x in {"a": 1, "b": 2}:      # loop variable
    print ("x = " + str(x))     # print x

# for loop with array
for x in [1, 2, 3]:             # loop variable
    print ("x = " + str(x))     # print x

###################################################

# for loop break
for x in range(10):             # loop variable
    if x == 5:                  # loop condition
        break                   # break loop
    print ("x = " + str(x))     # print x

# for loop continue
for x in range(10):             # loop variable
    if x == 5:                  # loop condition
        continue                # continue loop
    print ("x = " + str(x))     # print x

# for loop else
for x in range(10):             # loop variable
    print ("x = " + str(x))     # print x
else:                           # else
    print ("done")              # print done

# while loop else
x = 0                           # loop variable
while x < 10:                   # loop condition
    print ("x = " + str(x))     # print x
    x = x + 1                   # increment x
else:                           # else
    print ("done")              # print done

###################################################