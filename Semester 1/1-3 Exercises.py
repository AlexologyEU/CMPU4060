# Lecture notes
# x = 0
# while x < 10:
#  print (x)
#   x = x + 1
# print ("Final value of x: ", x)

# for i in range(1,21):
#    if i%2 == 0:
#        print(i)

# s = int(input("Keep entering numbers. Enter 0  to end. Enter a number here: \n"))

# while s!=0:
#  print ("You've entered ", s)
#   s = int(input("Enter next number: "))
# print("Goodbye!")
#
#### 1. Write while loop that prints number 1 to 10 on the screen
# x = 0
# while x < 10:
#    print (x)
#    x = x + 1
# print("the final value of x = ", x)

#### 2. Write a for loop that prints number 1 to 10 on screen
#
# for number in range (1,11):
#   print(number)

####3. Write for loop that iterates from 0 to 20. For each iteration it checks if
####number is even or odd and prints: 1 is odd, 2 is even

# for number in range (0,21):
#    if number % 2 == 0:
#        print(number, "The number is even")
#    elif number % 1 == 1:
#        print("The number is odd")
#    else:
#        print(number, "The number is odd")

####Improved:
# list_even = []
# list_odd = []
# for n in range(1, 21):
#     if n % 2 == 0:
#         list_even.append(n)
#     elif n % 2 == 1:
#         list_odd.append(n)
# print("These are the even numbers: \n",
#       list_even)
# print("These are the odd numbers: \n",
#       list_odd)

####4. Write a for loop that iterates from 0 to 10. For each iteration it will
#### multiply by 9 and print: 2 * 9 = 18

# for number in range (1,11):
#    print(number, "*9 =", number*9)

####5. Program that asks for a number and prints the sum of all numbers from 1
#### to the number they enter.
# sum = 0
# number = int(input("Please enter a number: "))
# for i in range (1, number+1):
#    sum =  sum + i
#    print(sum)

#### 6. Write a program to calculate and print the factorial of a number using a
#### for loop. EG. factorial of 4: 4*3*2*1 = 24
# product = 1
# number = int(input("Please enter a number: "))
# for multiple in range (1, number+1):
#    product = product*multiple
#    print(product)

#### 7. Program to ask for a number and print it on the screen. Keep asking until
#### a negative is given.
# number = int(input("Please enter a number between number 1 and 10, the game will end when you enter a negative: "))
# while number % 2 == 0:
#     print("Your number is ", number)
#     if (number <1) or (number > 10):
#         print("The number you selected is outside the range, please select another")
#     number = int(input("Would you like to add another number? "))
# print("Goodbye")

####Improved
# number = int(input("Enter a number: "))
# while number % 2 != 1:
#     number = int(input("Enter another number: "))
# else:
#     print("The number", number, "is odd")

#### 8. Write a program that uses loops to print the triangle below:
#   *
#   **
#   ***
#   ****
#   *****

####9. Write a program that uses loops to print the triangle below:
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5



