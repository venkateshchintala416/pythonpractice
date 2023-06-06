# set
# we can create set using two ways
# syntax : set()
# syntax : {element, element....}
# in set insertion order is not maintained / unordered elements
# set will not allow duplicates
# set is immutable


s1 = set()
print(s1, type(s1))

s2 = {10}
print(s2, type(s2))

s3 = {10, 20, 30, 40, 50, 10, 20}
print(s3)

s4 = {10.0, 10, 20, 20.0, 10}
print(s4)

s5 = {10.5, 10.7, 10.9, 10.7}
print(s5)