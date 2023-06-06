# list is a datatype, and it is an object
# we can create list using square brackets and object
# In list all the elements maintains insertion order/ ordered elements
# list allow duplicates and allows different data types
l1 = []
print(l1)

# append(element) adds the element at the end of the list
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
print(l1)

l2 = [10, 20, 30, 40, 50]
l2.append(60)
l2.append(70)
print(l2)

l3 = ['apple', 'mango', 'grapes', 'goa']
l4 = ['red', 'blue']
l3.append(l4)
print(l3)

l5 = [10, 20, 40, 'a', 'b', 10, 20, 'c']
l5.append(30)
print(l5)
