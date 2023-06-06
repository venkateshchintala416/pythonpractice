# Frozenset
# list is mutable
# tuple is immutable

# set is mutable
# frozenset is immutable
f1 = frozenset()
print(f1, type(f1))

f2 = frozenset({10, 20, 30, 40, 50})
print(f2)
# f2.add(100)  # AttributeError: 'frozenset' object has no attribute 'add'

s1 = {10, 20, 30, 40, 50}
s1.add(f2)
print(s1)

s1.remove(f2)
print(s1)