# Higher Order Function
# The function that takes an argument or returns a function
def d1():
    print('d1 function')
    def d2():
        print('d2 function')
    return d2

d = d1()
d()

def d3(a, b):
    def d4():
        return a, b
    return d4
d = d3(10, 20)
print(d())


