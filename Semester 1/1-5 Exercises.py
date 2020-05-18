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

####Lab 5 EXERCISE 1####
# string = "This is my practice string"
# print(string)


# ####Lab EXERCISE 2####
# count = 0
# string = "This is my practice string"
# for x in string:
#     if x.isalpha():
#         count += 1
# print(count)

#
# ####Lab EXERCISE 3####
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

####Lab 5 EXERCISE 4####
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

####Lab 5 Exercise 5####

# new_string = ""
# string = input("Please enter a string: ")
# for c in string:
#     new_string = new_string + chr(ord(c) + 1)
# print(new_string)


####Lab 5 Exercise 6####




####Lab 5 Extra Exercise 1 ####
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


####Lab 5 Extra Exercise 2####

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


