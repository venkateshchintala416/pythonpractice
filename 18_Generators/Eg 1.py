# Generators are functions we can create our own iterations
def d1():
    return 10
    return 20 # This code is unreachable
    return 30 # This code is unreachable

d = d1()
print(d)
print(type(d1))
def d2():
    return 10, 20, 30
d = d2()
print(d)
print(type(d2))

# generator function
def d3():
    yield 10
    yield 20
    yield 30

d = d3()
print(d)
print(type(d3))  # <class 'function'>
print(d.__next__())
print(d.__next__())
print(d.__next__())

# In the generator function we should not use return keyword
def d4():
    yield 10
    yield 20
    return 30
    yield 40

d = d4()
print(d)
print(next(d))
print(next(d))
# print(next(d))  # StopIteration: 30

def d5(n):
    for i in range(n):
        yield i

d = d5(2)
print(next(d))
print(next(d))
