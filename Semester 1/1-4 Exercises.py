####1. Write a program which finds and prints all numbers between
####2000 and 3200 (inclusive) which are divisible by 7 and not
####a multiple of 5.

#for i in range(2000, 3201):
#   if i % 7 == 0 and  i % 5 != 0:
#         print (i)

####2. Write a program that will count how man digits (0-9) are
####in a string entered by a user.
# i = input("Please enter a string of numbers: ")
# a = 0
# for c in i:
#     if "0" <= c <= "9":
#         a += 1
# print(a)

####Improved:

# string = input("Please enter a sequence of numbers: ")
# total = 0
# for i in list(string):
#     if i.isdigit():
#         total += 1
# print(total)

####Exercise 2 TEACHER SOLUTION###
####I got the same as the teacher! ####
# s = input("Enter a string")
# number = 0
# for c in s:
#   if c.isdigit():
#      number += 1
# print(number)


####3. Extend your program from ex.2 to count how many letters
####(a-z or A-Z) are in a sentence entered by the user
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

####Improved, same as teacher! :
# string = input("Please enter a group of letters and numbers: ")
#
# lt_total = 0
# nu_total = 0
# for c in string:
#     if c.isdigit():
#         nu_total += 1
#     elif c.isalpha():
#         lt_total += 1
# print("The string: ", string, " contains: \n"
#       , lt_total, "letters \n"
#       , nu_total, "numbers")

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

#####4. Write a program to find and print the sum of digits of a
####number entered by the user.

# sum = 1
# s = input("please enter some numbers: ")
# for c in s:
#     sum = sum + int(c)
# print(sum)

####Exercise 4 Teacher Solution ####

# number = input("Please enter a number: ")
# sum = 0
# for d in number:
#     sum = sum + int(d)
# print(sum)


####5.Write a program to keep asking the user to enter positive
####numbers and terminates when a negative is entered.
####When the program finishes, print how many positives and
####negatives were entered and what was the smallest number.

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

####Extra Ex 1: Guess the number.
####Use a variable to store a secret nummber. Ask the user to guess
####the number and reply 'too high' or 'too low', keep asking
#### until the user guesses the correct number.####
####Problem with the guess count and lacking finesse

#
# import sys
# from random import randint
# ans = randint(0, 100)
# count = 5
#
# print("----")
# print("Welcome to the guessing game. ")
# print("Try to guess a number between 0 and 100")
# print("You start with 10 guesses.")
# print("----")
#
# input("Press 'enter' to start.")
#
# while count >= 1:
#     print("You have ", count, "guesses remaining")
#     guess = int(input("Take a guess: "))
#     count -= 1
#     # while guess != ans:
#     if guess > ans:
#         print("----")
#         print("That's too high. ")
#         print("You have ", count, "guesses remaining")
#         print("----")
#         guess = int(input("Take a guess: "))
#         count -= 1
#
#     elif guess < ans:
#         print("----")
#         print("That's too low.")
#         print("You have ", count, "guesses remaining")
#         print("----")
#         guess = int(input("Take a guess: "))
#         count -= 1
#
#     if guess == ans:
#         print("You got it! ")
#         print("Thanks for playing.")
#         break
#
# print("Oh no, you ran out of guesses!")
# print("The number was: ", ans)
# sys.exit()


###Extra Exercise 1#### Teacher solution?
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


####Extra Ex.2: Ask the user for a number and print all divisors
####of that number. For example 2,3,4 and 6 are divisors of 12

# num = int(input("Please enter a number to search for its divisors: "))
# div = []
# for x in range(1, num):
#     if num % x == 0:
#         div.append(x)
#
# print(div)


####Extra Ex.3 Write a program for checking the speed of drivers.
####The program should ask for user speed and do one of the
####following:
#### if speed is less than 70, print 'ok'
####if speed is more than 70: for every 5KM over it should give
####one demerit.
#### if the driver gets more than 12 points, the program should print
####'licence suspended'
#
# speed = int(input("Enter you speed: "))
# points = 0
#
# if speed <= 69:
#     print("Your speed is correct. ")
#
# elif speed >= 70:
#     for i in range(70, speed, 5):
#         points += 1
#     if points > 12:
#         print("You done messed up now m-fucker! Your licence is gone!")
#
#     else:
#         print("Your speed earned: ", points, "penalty points.")
#

