def d1(para1):
    return 'd1 function', para1

def d2():
    return 'd2 function'

d = d1(d2())
print(d)

def d3(para1, para2):
    return 'd3 function', para1, para2

def d4():
    return "d4 function"

def d5():
    return "d5 function"

d = d3(d4(), d5())
print(d)
