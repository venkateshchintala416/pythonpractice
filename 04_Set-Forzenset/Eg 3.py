# add()
s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90}
s1.add('NameOne')
s1.add('NameTwo')
s1.add('NameThree')
print(s1)

# remove()
s2 = {10, 20, 30, 40, 50}
s2.remove(30)
print(s2)

# discard()
s3 = {10, 20, 30, 40, 50, 60}
s3.discard(20)
print(s3)

# update()
s1 = {10, 20, 30, 40, 50, 60, 70}
s1.update([80, 90, 100])
print(s1)

s2 = {'a', 'b', 'c', 'd'}
s2.update(s1)
print(s2)