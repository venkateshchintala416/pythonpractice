l1 = [i for i in range(50) if i % 2 == 0 if i % 5 == 0]
print(l1)
    #output [0, 10, 20, 30, 40]

names = ['admin', 'admin', 'admins', 'admin']
l1 = [i if i == "admin" else "not admin" for i in names]
print(l1)
    #output ['admin', 'admin', 'not admin', 'admin']