# replace()

s1 = "Hello Hello Hello"
print(s1)

print(s1.replace('H', 'h'))
print(s1.replace('H', 'h', 1))
print(s1.replace('H', 'h', 2))
print(s1.replace('H', 'h', 3))

# split()
s1 = "Hello Java Hello Python Hello JavaScript"
print(s1.split())  # ['Hello', 'Java', 'Hello', 'Python', 'Hello', 'JavaScript']

s2 = "Hello Java and Hello Python and Hello JavaScript"
print(s2.split('and'))  # ['Hello Java ', ' Hello Python ', ' Hello JavaScript']

s3 = "Hello Java : Hello Python : Hellp JavaScript"
print(s3.split(":"))  # ['Hello Java ', ' Hello Python ', ' Hellp JavaScript']

# join()
s1 = ['Hello', 'Java', 'Hello', 'Python', 'Hello', 'JavaScript']
print(' '.join(s1))  # Hello Java Hello Python Hello JavaScript

s2 = ['Hello Java ', ' Hello Python ', ' Hello JavaScript']
print('and'.join(s2))  # Hello Java and Hello Python and Hello JavaScript
