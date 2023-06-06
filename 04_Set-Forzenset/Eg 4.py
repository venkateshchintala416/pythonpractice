# index call and slicing
# s1 = {10, 20, 30, 40, 50}
# print(s1[0])  # TypeError: 'set' object is not subscriptable

# repetition and addition
s2 = {10, 20, 30, 40, 50}
# print(s2 * 2)  # TypeError: unsupported operand type(s) for *: 'set' and 'int'

s3 = {2, 2, 2, 2, 2}
# print(s2 + s3)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# ValueError: too many values to unpack (expected 4)
a, b, c, *d = {10, 20, 30, 40, 50, 60, 70, 80}
print(a)
print(b)
print(c)
print(d)

# swap
a, b, c, d = {100, 200, 300, 400}
print(c, d, a, b)

s4 = {10, 20, 30, 40, 50}
print(s4.copy())

s4.clear()
print(s4)