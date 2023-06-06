# we can create in two ways, tere are like using syntax : () and object syntax tuple()
# we can store duplicate value in tuple, it maintains insertion order / ordered elements
# we are not hacing methods to modify the tuple data
# Note: Tuple is safe


t1 = ()
print(t1, type(t1))

t2 = tuple()
print(t2, type(t2))

t3 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 10)
#      0   1   2  3    4   5   6   7   8   9  10, 11
print(t3)
print(t3.count(20))

# index(element, start, end)
print(t3.index(10, 10))

# tuple is safe and list is unsafe
print(len(t3))
#t3[11] = 30
# print(t3) # TypeError: 'tuple' object does not support item assignment
l1 = [10, 20]
l1[0] = 100
print(l1)