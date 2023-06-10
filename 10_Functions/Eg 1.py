# functions
# function are used for reuse-ability
# we can declare function in python using def keyword

# function without args
def d1():
    print('d1 function 01')
    print('d1 function 02')

d1()

# function with args
def d2(a, b):
    print(a, b)

d2(10, 20)
d2(30, 40)

# function using return keyword
def d3(a, b):
    return print(a, b)

d3(50, 60)

def d4(a, b):
    return a+b

print(d4(10, 20))
