# closure
def d1(a, b):
    print('d1 function', a+b)
    def d2():
        return a*b
    return d2

d = d1(10, 20)
print(d())
del d1
# d1(5, 2) # NameError: name 'd1' is not defined. Did you mean: 'd'?
print(d())
