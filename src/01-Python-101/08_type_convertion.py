x = 10
y = 10.2
z = "10"

print (type(x)) # type of x
print (type(y)) # type of y
print (type(z)) # type of z

print (int(y)) # convert y to integer
print (str(x)) # convert x to string
print (float(x)) # convert x to float
print (int(z)) # convert z to integer

# Implicit type conversion
a = 10
b = 10.2
c = "10"

print (a + b) # 20.2
print (a + int(b)) # 20
print (a + float(b)) # 20.2
print (a + int(c)) # 20

# Explicit type conversion
d = 10
e = 10.2
f = "10"

print (int(d) + int(e)) # 20
print (int(d) + float(e)) # 20.2
print (int(d) + int(f)) # 20