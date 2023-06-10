# variables
# variable holds the value and stores the value
# global variable and local variable
a = 10
print(a)

def d1():
    print('GV inside the function', a)
d1()
print('GV outside the function', a)

# local variable
def d2():
    b = 20
    print('LV inside the function: ', b)
d2()
# print('LV outside the function: ', b)
