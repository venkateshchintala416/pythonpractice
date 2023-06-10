# function using default value
def d1(a=10, b=20):
    print(a, b)
d1(100, 200)
d1()

# function using key value pairs
def d2(a, b):
    print(a, b)
d2(a=10, b=20)
d2(a='apple', b='ball')

# function using arbitrary *args
def d3(*names):
    print(names)
d3('NameOne', 'NameTwo', 'NameThree', 'NameFour')

# **kwargs
def d4(**colors):
    print(colors)
d4(a='red', b='brown', c='orange', d='blue', e='green', f='yellow')
