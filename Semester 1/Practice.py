

####1. Write a program which finds and prints all numbers between
####2000 and 3200 (inclusive) which are divisible by 7 and not
####a multiple of 5.

# complete = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         complete.append(i)
# print(complete, sep="\n")


####2. Write a program that will count how man digits (0-9) are
####in a string entered by a user.

# test = input("Please enter a sting of numbers: ")
# total = 0
# for i in list(test):
#     if i.isdigit():
#         total += 1
# print("There are ", total, "digits in the string: ", test)

####3. Extend your program from ex.2 to count how many letters
####(a-z or A-Z) are in a sentence entered by the user

# test = input("Please enter some chars and digits to be counted: ")
# num_total = 0
# char_total = 0
# for i in test:
#     if i.isdigit():
#         num_total += 1
#     elif i.isalpha():
#         char_total += 1
# print("There are ", num_total, "Digits and ", char_total, "Chars in the string:", test)

#####4. Write a program to find and print the sum of digits of a
####number entered by the user.

# sum = 1
# test = input("Please enter some digits to be summed.")
# for s in test:
#     sum = sum + int(s)
# print(sum)

####5.Write a program to keep asking the user to enter positive
####numbers and terminates when a negative is entered.
####When the program finishes, print how many positives and
####negatives were entered and what was the smallest number.

# number = int(input("Enter a number, to end, enter a negative number: "))
# low = number
# total = 0
# while number > 0:
#     if number < low:
#         low = number
#         number = int(input("Enter a number, to end, enter a negative number: "))
#     else:
#         number = int(input("Enter a number, to end, enter a negative number: "))
#     total += 1
# if number < 0:
#     print("The total number of positives: ", total)
#     print("The lowest number was: ", low)


####Extra Ex 1: Guess the number.
####Use a variable to store a secret nummber. Ask the user to guess
####the number and reply 'too high' or 'too low', keep asking
#### until the user guesses the correct number.

import sys
from random import randint
ans = randint(0, 10)
count = 10

print("----")
print("Welcome to the guessing game. ")
print("Try to guess a number between 0 and 100")
print("You start with 10 guesses.")
print("----")

input("Press 'enter' to start.")

while count > 0:
    print("You have ", count, "guesses remaining")
    guess = int(input("Take a guess: "))
    count -= 1
    while guess != ans:
        if guess > ans:
            print("----")
            print("That's too high. ")
            print("You have ", count, "guesses remaining")
            print("----")
            guess = int(input("Take a guess: "))
            count -= 1
        elif guess < ans:
            print("----")
            print("That's too low.")
            print("You have ", count, "guesses remaining")
            print("----")
            guess = int(input("Take a guess: "))
            count -= 1

    if guess == ans:
        print("You got it! ")
        print("Thanks for playing.")
        break

if count == 0:
    print("Oh no, you ran out of guesses!")
    sys.exit()









