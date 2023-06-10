# membership operators in , not in
l1 = [10, 20, 30, 40, 50]
print(10 in l1)
print(60 in l1)
print(30 not in l1)
print(60 not in l1)

# OUTPUT
# TRUE
# FALSE
# FALSE
# TRUE


# identity operators is(content), == (ref)
a = 10
b = 10
print(a is b)
print(a == b)
# OUTPUT
# TRUE
# TRUE


l1 = [10, 20, 30, 40, 50]
l2 = l1
print(l1 is l2)
print(l1 == l1)
# OUTPUT
# TRUE
# TRUE


l3 = [10, 20, 30, 40, 50]
print(l1 is l3)
print(l1 == l3)

# OUTPUT
# FALSE
# TRUE