def d1(func):
    def d2():
        return 'd1 function', func()
    return d2

@d1
def d3():
    return "d3 function"

# d = d1(d3)
# print(d)
# print(d.__name__)
# print(d())
print(d3())
