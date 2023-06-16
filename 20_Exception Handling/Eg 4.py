try:
    s1 = {10, 20, 30, 40, 50}
    print('Before')
    print(s1)
    s1.remove(60)
    print(s1)
    s1.discard(30)
    print(s1)
except KeyError:
    print('KeyError:')

print('After')
