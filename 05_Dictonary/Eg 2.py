# Assigning the position to list and dict
# l1 = [10, 20, 30, 40, 50]
# l1[5] = 50
# print(l1) # IndexError: list assignment index out of range

d1 = {1: 10,2: 20,3: 30,4: 40,5: 50}
d1[6] = 60
print(d1)

# update()
d2 = {'a': 'apple', 'b': 'banana'}
d2.update(d1)
print(d2)

d3 = {}
d3.update({'a': 10, 'b': 20})
print(d3)