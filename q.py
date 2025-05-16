
## 1. KEYWORD ARGUMENTS

# print("Hello!",end="");\
# print("PYTHON IS A GREAT LANGUAGE")


#print("HI","HELLO","PYTHON","IS","A","LANGUAGE",sep="+")

#print("HI","HELLO","PYTHON","IS","A","LANGUAGE",sep="+");\
#print("SO","IT'S","MUST","TO","LEARN", sep='*',end='@@@')

#print('Hello')
#print('python')


#print('Hello,\n python');\
#print('python')


#print('Hello',end=' ');\
#print('python')



## 2. LITERALS

 # Literals 4 Types
 # A. Integers -- a.OCTAL    b.HEXADECIMAL
 # B. Floating Point Number
 # C. String
 # D. Booleans.

# String literals are written in '' , "" quotes..

## 3. OPERATORS

#python has 7 arithmatic operators
#a. ADD +
#b. SUBTRACT -
#c. MULTIPLY *
#d. DIVISION /
#e. FLOOR DEVIDE //
#f. MODULO %
#g. EXPONENTIAL **

#print(6.//4)
# In genral 6/4 is 1.5 .. using floor devision(//) they filling nearest small value.


# 3. VARIABLES

amount_of_apples = 2
cost_of_apples = 10
#print(amount_of_apples * cost_of_apples)


# variables allows you to store values in daatabase

# 4. INPUT

#a. INTEGER INPUT
#b. FLOATING POINT INPUT

#age = int(input('HOW OLD ARE YOU?'))
#print(age)

#print(age - 10)


# 5. STRING METHOD

#print(int('22'))

#print(str(22))

#cost_of_apples = 2
#amount_of_apples = input("HOW MANY APPLES YOU WANT ?")
#total_sum = cost_of_apples * int(amount_of_apples)
# print('you have to pay:' + str(total_sum))

# 6. COMPARISION OPERATORS

# a.Equal ==
#print(2==2)

#print(22==44)

# b. Not Equal !=
#print(2!=2)

#print(22!=44)

# c.Greater then(>)
#print(2>2)

#print(5>1)

# d. Grater then or equal to(>=)
#print(4>=2)
# e. Smaller then <
# f. Smallerthen or eqaul to <=

# 7. CONTROL FLOW
#A. CONDITIONAL STATEMENTS using if and elif
#B. LOOP STATEMENTS
#C. LOOP-FOR STATEMENTS

# age = int(input("How many years ?"))
# if age >= 18:
 # print("You are an adult")
#elif age ==18:
   # print("you are exactly 18 years old")
#else:
    #    print(" you are Below 18 years old")


# using while condition
#secret_number = 3
#guess = int(input("guess a number:"))
#while guess != secret_number:
#   guess = int(input("guess a number:"))
#else:
#        print("congratulations, you got it!")


# Loop-For

#for i in range(110):
#   if(i==100):
#       break
#   print("i is:",i)


# 7. LOGIC & BIT OPERATOR
# A. Operators
age1 = 16
age2 = 16
# if(age1>= 18 and age2>= 18):
#     print("You are both adults")
#elif(age1>= 18 or age2>= 18):
#    print("One of you is an adult")
#else:
#    print("You are both children")



#Countries= ["USA","LANDON","UAE"]
#Countries[0]="UK"
#print(Countries)

#len(Countries)

#ages=[33,23,12,555,66,77]
#ages.sort()
#ages.reverse()
# print(ages)


# 8. DICTIONARIES

# These 3 are built in methods are present in dictionaries

# a. dictionary.keys()
# b. dictionary.values()
# c. dictionary.items()
#usernames= {
#    "lydia":"lydiahallie",
#    "sarah":"sarah123",
#    "max":"max_",
#    "joe":"joejoe",
#    }
#print(usernames["sarah"])
#print(usernames.keys())
#for key in usernames.keys():
#    print(key +"-" + usernames[key])

#print(usernames.values())
#print(usernames.items())
#usernames.update({"chloe":"chole123"})
#print(usernames["chloe"])
#del usernames["max"]
#for key in usernames.keys():
#    print(key +"-" + usernames[key])


#L1=[10,20,30,40,60,70,80]
#print(L1.index(10))

chr()
print(chr(65))
