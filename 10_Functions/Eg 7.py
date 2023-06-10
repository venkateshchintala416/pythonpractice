# inner function
def d1():
    print('d1 function')
    def d2():
        print('d2 function')
    d2()

d1()

def d3(a, b):
    def d4():
        print(a+b)
    d4()

d3(10, 20)
