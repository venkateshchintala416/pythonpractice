enter_number = int(input('Enter any number: '))
if enter_number % 2 == 0:
    print('Even Number: ', enter_number)
else:
    print('Odd Number: ', enter_number)

enter_number_again = int(input('Enter number: '))
if enter_number_again > 0:
    print('Positive Number')
elif enter_number_again < 0:
    print('Negative Number')
else:
    print('Zero Number')
