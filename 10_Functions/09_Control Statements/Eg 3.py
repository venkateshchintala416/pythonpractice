user_name = input('Enter username: ')
pass_word = input('Enter pass_word: ')
if user_name == 'Admin' and pass_word == 'Admin':
    print('Login Success')
else:
    print('Login Failed')
