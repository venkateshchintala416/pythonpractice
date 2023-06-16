# tuple
t = (1, 2, 3, 4, 5)
print(t, type(t))

t = (i for i in range(5))
print(t, type(t))
print(tuple(t), type(t))

t = tuple(i for i in range(5))
print(t, type(t))
