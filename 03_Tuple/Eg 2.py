# Repetition and Addition
t1 = (10, 20, 30, 40, 50)
print(t1 * 2)

t2 = (10, 20, 30, 40, 50)
t3 = (2, 2, 2, 6, 2)
print(t2 + t3)

# ValueError: too many values to unpack (expected 4)
a, b, *c, d = (10, 20, 30, 40, 50, 60, 70, 80)
print(a)
print(b)
print(c)
print(d)