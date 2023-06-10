a, b, c = 10, 20, 30
def d1():
    return globals()

print(d1())

def d2():
    x, y, z = 100, 200, 300
    return locals()

d = d2()
print(d)
