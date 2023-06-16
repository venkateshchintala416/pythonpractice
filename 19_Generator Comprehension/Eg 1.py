def d1(a, b):
    return a, b

d = d1(5, 10)
print(type(d))
print(d)

def d2(a, b):
    print(a, b)

d = d2(10, 20)
print(type(d))

def d3(a, b):
    yield a
    yield b

d = d3(10, 20)
print(type(d))  # <class 'generator'>
print(next(d))
print(next(d))
