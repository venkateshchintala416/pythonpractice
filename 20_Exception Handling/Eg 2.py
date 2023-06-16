try:
    l1 = [10, 20, 30, 40, 50]
    print('Before')
    print(l1[0])
    print(l1[4])
    print(l1[6])
except IndexError:
    print("IndexError: list index out of range")

print('After')
