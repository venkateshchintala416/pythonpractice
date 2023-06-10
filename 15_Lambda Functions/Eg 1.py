# without lambda function
def d1(a):
    print(a)
d1(10)

l1 = lambda a : print(a)
l1(10)

def d2(a, b):
    print(a, b)
d2(10, 20)

l2 = lambda a, b: print(a, b)
l2(10, 20)

l3 = lambda a, b, c, d: (a+b, a-b, c*d, c/d)
print(l3(10,20,30,40))

l4 = lambda a=5, b=10: print(a, b)
l4()
l4(10,20)

l1 = lambda a: lambda b: print(a, b)
l = l1(100)
print(l.__name__)
l(200)
