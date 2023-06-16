print('Before')
try:
    a = 10
    b = 20
    c = 0
    print(a / b)
    # print(a / c)

    l1 = [10, 20, 30, 40, 50]
    print(l1[0])
    print(l1[4])
    # print(l1[6])

    s1 = {10, 20, 30, 40, 50}
    print(s1)
    s1.remove(60)
    print(s1)
    s1.discard(30)
    print(s1)

except BaseException:
    print('BaseException')

print('After')
