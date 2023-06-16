# Exception
# An unwanted exception that disturbs the normal flow of program is called Exception Handling
# try, expect, finally, raise
try:
    a = 10
    b = 20
    c = 0
    print('Before')
    print(a / b)
    print(a / c)
except ZeroDivisionError:
    print('ZeroDivisionError: division by zero')
print('After')