# we can create new list from the existing list
# list, set, dict, tuple/generator
l1 = [i for i in range(10)]
print(l1)
    #output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


l2 = [i for i in range(20) if i % 2 == 0]
print(l2)
    #output [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


s1 = {i for i in range(10)}
print(s1)
    #output {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


d1 = {i: i*i for i in range(10)}
print(d1)

    #output {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

t1 = (i for i in range(10))
print(t1)
    #output <generator object <genexpr> at 0x000002BC06D04380>
