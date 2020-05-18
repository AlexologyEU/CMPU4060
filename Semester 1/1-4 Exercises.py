####Exercise 1 ####
#for i in range(2000, 3201):
#   if i % 7 == 0 and  i % 5 != 0:
#         print (i)

###Exercise 2####
# i = input("Please enter a string of numbers: ")
# a = 0
# for c in i:
#     if "0" <= c <= "9":
#         a += 1
# print(a)

####Exercise 2 TEACHER SOLUTION###
# s = input("Enter a string")
# number = 0
# for c in s:
#   if c.isdigit():
#      number += 1
# print(number)

#  print(c, c.isdigit())
      #####REMEMER .####

####Exercise 3####
# s = input("Please enter a string")
# a = 0
# b = 0
# d = 0
# for c in s:
#    if c >= "0" and c<="9":
#       a = a + 1
#    if c >="a" and c<="z":
#       b = b + 1
#    if c >= "A" and c<= "Z":
#       d=d+1
#
# print(a)
# print(b)
# print(d)

####EXERCISE 3 Teacher solution ####
# s = input("Enter a string")
# number_digits = 0
# number_letter = 0
# for c in s:
#    if c.isdigit():
#       number_digits +=1
#    if c.isalpha():
#       number_letter +=1
# print("digits: ", number_digits)
# print("letters: ", number_letter)

#####Exercise 4####

# sum = 1
# s = input("please enter some numbers: ")
# for c in s:
#     sum = sum * int(c)
# print(sum)

####Exercise 14 Teacher Solution ####

# number = input("Please enter a number: ")
# sum = 0
# for d in number:
#     sum = sum + int(d)
# print(sum)


####Exercise 15 TEACHER SOLTION BETTER####

# n = int(input("Please enter a number, the game terminates when you add a negative: "))
# min = n
# while n > 0:
#     if n < min:
#         min = n
#     n = int(input("Please enter a number: "))
# print(min)

####Exercise 15 TEACHER SOLUTION###

# count = 0
# x = int(input("Please enter a number: "))
# count = count + 1
# min = x
# while x >= 0:
#     if x < min:
#         min = x
#     x = int(input("Please enter a number: "))
#     count = count + 1
# print("Total number of numbers entered: ", count - 1)
# print("The smallest number entered: ", min)


###Extra Exercise 1####
# from random import randint
# x = randint(1, 10)
# print(x)
# guess = int(input("Please enter a guess between 0 - 10: "))
# while guess != x:
#     if guess < x:
#         print("Your number is too low")
#         guess = int(input("Please enter a guess between 0 - 10: "))
#     if guess > x:
#         print("Your number is too high")
#         guess = int(input("Please enter a guess between 0 - 10: "))
#     if guess == x:
#         print("You got it!")




