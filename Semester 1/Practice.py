

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

number = input("Enter a number, to end, enter a negative number")
while number >= 0:
    number = input("Enter a number, to end, enter a negative number")





