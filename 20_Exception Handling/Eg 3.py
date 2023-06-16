try:
    print('Before')
    i = input('Enter any number: ')
    print((int(i)))
except ValueError:
    print('ValueError: invalid literal for int() with base 10: Ten')
print('After')
