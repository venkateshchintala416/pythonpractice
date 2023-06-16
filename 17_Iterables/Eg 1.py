# a = 10
# for i in a:
#     print(a)  # TypeError: 'int' object is not iterable

# b = 20.0
# for i in b:
#     print(i)  # TypeError: 'float' object is not iterable

# all the sequences are iterables
s1 = "sai kiran"
for i in s1:
    print(i)

# list
l1 = [10, 20, 30, 40, 50]
for i in l1:
    print(i)

# tuple, set, dict

# iterator
# iterator is an object, this object contains two methods iter(), next()
l1 = []
print(dir(l1))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
# '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
# 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(l1.__iter__())  # <list_iterator object at 0x102f87a00>
