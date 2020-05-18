####1. User inputs a mark between 0 and 100. Print 'pass' if the mark is 40 or over,
####or 'fail' if the mark is below 40
#
# mark = input("Please enter your mark: ")
# if int(mark) < 40:
#     print("Sorry that is not a passing grade")
#
# if 40 <= int(mark) <= 74:
#     print("Congratulations, you passed")
#
# elif int(mark) >= 75:
#     print("Congratulations, you passed and earned a high grade! ")

####2. User inputs number, check if number is even or odd. (Use % to get remainder of division)

# number = int(input("Please enter a number: "))
# if number % 2 == 1:
#     print("That number is odd.")
#
# elif number % 2 == 0:
#     print("That number is even.")

####3. User enters 2 integers. Output if first is larger, smaller or equal to the second. (USe if-elif-ese)

# number_1 = int(input("Please enter the first number: "))
# number_2 = int(input("Please enter the second number: "))
#
# if number_1 > number_2:
#     print("Number 1 is larger.")
#
# elif number_1 < number_2:
#     print("Number 2 is larger.")
#
# elif number_1 == number_2:
#     print("Those numbers are equal")

####4. It costs 1 euro to post to Ireland, 1.70 to post to Europe and 2 to post to the rest of the world.
# write a program that asks a user where they want to post and prints the cost.
#
# print("Choose your destintation from the following: ")
# print("-----")
# print("Ireland: \u20ac1")
# print("Europe: \u20ac1.70")
# print("The rest of the World: \u20ac")
# print("-----")
# place = input("Destination:  ")
#
# if place == str("Ireland"):
#     print("Your fee is \u20ac1")
# elif place == str("Europe"):
#     print("Your fee is \u20ac1.70")
# elif place == str("Rest of the world"):
#     print("Your fee is \u20ac2")

####5. Parking costs 2/hour with the first 2 hours free. Ask the user
# how long they would like to park and calculate the cost
#
# time = int(input("Please enter the length of your stay: "))
# if time <= 2:
#     print("Stays under 2 hours are free.")
#
# elif time > 2:
#     total = (time - 2) * 2.
#     print("Your total is: \u20ac", total, "for a stay of ", time, "hours")

####6 Write a calculator program. User enters two numbers and an operation
####(=, -, *, /) and print the result
#
# print("Welcome to the Calculator")
# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# op = input("Choose from the following operators (+, -, *, /): ")
#
# if op == str("+"):
#     total = num_1 + num_2
#     print(total)
#
# elif op == str("-"):
#     total = num_1 - num_2
#     print((total))
#
# elif op == str("*"):
#     total = num_1 * num_2
#     print(total)
#
# elif op == str("/"):
#     total = num_1 / num_2
#     print(total)
#
# else:
#     print("Something went wrong. ")

####7. Calculate a dog's age. For the first two years, a dog year is equal to 10.5
# human years, after that they are equal to 4 years.
# Expected output:
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73
#
# age = int(input("Enter the dog's age: "))
# if age <= 2:
#     total = age * 10.5
#     print("Your dog's age is dog years is: ", total)
#
# elif age > 2:
#     total = ((age - 2) * 4) + 21
#     print("Your dog's age in dog years is: ", total)