f = None
f1 = None
try:
    # f = open('one.txt', 'w')
    # i = input('Enter ant text: ')
    # f.write(i)
    # print('Data Inserted')

    f1 = open('one.txt', 'r')
    result = f1.read()
    print(result)
except FileNotFoundError:
    print('FileNotFoundError')
finally:
    f.close()
    print('Connection Closed')
