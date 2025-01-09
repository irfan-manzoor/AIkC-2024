# Data Structures

# list - Mutable
l = [1, 2, 3, 4, 5]
print("list:", l)

# tuple - Immutable
t = (1, 2, 3, 4, 5)
print("tuple:", t)

# set - Mutable
s = {1, 2, 3, 4, 5}
print("set:", s)

# dict - Mutable
d = {"a": 1, "b": 2, "c": 3}
print("dict:", d)

# indexing
print("list:", l[0])
print("tuple:", t[0])
# print(s[0])
print("dict:", d["a"])

# slicing
print("list:", l[0:3])
print("tuple:", t[0:3])
# print(s[0:3])
# print(d["a":"c"])

# length
print("list:", len(l))
print("tuple:", len(t))
print("set:", len(s))
print("dict:", len(d))

# membership
print("list:", 1 in l)
print("tuple:", 1 in t)
print("set:", 1 in s)
print("dict:", 1 in d)

# concatenation
print("list:", l + l)
print("tuple:", t + t)
# print(s + s)
# print(d + d)

# repetition
print("list:", l * 3)
print("tuple:", t * 3)
# print(s * 3)
# print(d * 3)