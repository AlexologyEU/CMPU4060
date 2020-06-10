# hello = "Hello World"
#
# print(hello[0:11:2])
#
# new_hello = hello[:]
# print(len(new_hello))
# new_string = new_hello + " " + new_hello * 2
# print(new_string)
#
# new_new_string = new_string * 3
# print(new_new_string)
#
#
# ord(66)
# print(ord)

####1. Write a program to print each char from a str on a
#### single line

# string = "This is my practice string"
# print(string)


####2. Write a program that will calculte the length of a str.
# count = 0
# string = "This is my practice string"
# for x in string:
#     if x.isalpha():
#         count += 1
# print(count)

####Shortened simple version:
# print(len(input("Enter a string: ")))

####improved answer:
# string = str(input("Please enter a string to be measured: "))
# count = 0
# for i in string:
#     if i.isdigit():
#         print("Only characters can be counted, not digits. ")
#         break
#
#     elif i.lower().isalpha() or i.isspace():
#         count += 1
# print(count)


####3. Write a program that reads a string and prints a string
####that is made up of the first and last two chars.
#### if str lenght is less than 4 ask for a new input
#### example "hello there" will produce: "here"

# string = input("Please enter some letters: ")
# if len(string) < 4:
#     print("That string is too short, dickhead!! ")
# string_1 = (string[0:2])
# string_2 = (string[-2:])
# print(string_1 + string_2)


# string = str(input("Please enter some letters: "))
# if len(string) < 4:
#     print("That string is to short")
# elif len(string) > 4:
#     new_str = string[2:4] + string[-4:-2]
# print(new_str)

####Improved Version
# string = str(input("Enter a string: "))
# complete = False
#
# while complete is False:
#
#     if len(string) <= 4:
#         print("That string is too short. ")
#         string = str(input("Enter a string: "))
#         continue
#
#     elif len(string) > 4:
#         final = string[0:2] + string[-2:]
#         print(final)
#         complete = True

####4. Write a program that will reverse a string (using a loop)
# string = "Hello World"
# new_str = ""
# for i in range(len(string)-1, -1, -1):
#     new_str = new_str + string[i]
# print(new_str)


# s = "hello"
# new_str = ""
# for c in s:
#     new_str = new_str + c
#     ####OR####
#     # new_str = c + new_str
# print(new_str)

# s = "hello"
# i = len(s) - 1
# new_str = ""
# while i >= 0:
#     new_str = new_str + s[i]
#     i = i - 1
# print(new_str)

####5. Write a program that will 'encrypt' a string. Add 1 to the
####ASCII code ('a' becomes 'b')
####use ord + chr

# new_string = ""
# string = input("Please enter a string: ")
# for c in string:
#     new_string = new_string + chr(ord(c) + 1)
# print(new_string)


####6. Write a program that will swap 2 random letters in a string
#### Hint random means random index




####Extra 1. Check if a string is a valid password. It should contain
#### one upper, one lower, one special (+-%$!@) and be between
#### 6 and 10 chars long

# pwd = input ("Input password:")
#
# import re
# flag = 0
# while True:
#     if (len(pwd) < 6):
#         flag = -1
#         break
#     elif (len(pwd) > 10):
#         flag = -1
#         break
#     elif not re.search("[a-z]", pwd):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", pwd):
#         flag = -1
#         break
#     elif not re.search("[0-9]", pwd):
#         flag = -1
#         break
#     elif not re.search("[_@$]", pwd):
#         flag = -1
#         break
#     elif re.search("\s", pwd):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
#
# if flag == -1:
#     print("Not a Valid Password")


####Extra 2. Write a program that counts how many times the string
####'hi' is contained in another string for example:
#### 'hi there, the sky is high, but the moon is higher' should
#### print 3.

# mystring = "Hi there, the sky is high, but the moon is higher"
# substring = "hi"
# count = mystring.count(substring)
#
# for i in mystring:
#     if i == str('hi'):
#         count = count + 1
#
# print("Count of", substring, "in your string is : "
#       + str(count))


