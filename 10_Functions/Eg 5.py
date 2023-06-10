name = "Sai Kiran"
def d1():
    print('Before: ', name)
    globals()['name'] = 'Sai Ram'
    print('After: ', name)
d1()

def d2():
    name = "Abhi"
    print('Before: ', name)
    locals()['name'] = 'Anu'
    print('After: ', name)
d2()
locals()['name'] = 'Anvesh'
print('Outside the function: ', name)

# globals() and locals()
f1 = globals()
f2 = locals()
print(f1 == f2)

a, b, c = 10, 20, 30
print(a, b, c)
def d3():
    print('Globals: ', a, b, c)
d3()

f1 = globals()
print(f1)

def d4():
    x, y, z = 10, 20, 30
    print('Locals: ', x, y, z)
d4()

f2 = locals()
print(f2)
