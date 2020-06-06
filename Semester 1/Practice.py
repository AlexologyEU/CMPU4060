
#### 1. Write while loop that prints number 1 to 10 on the screen

# num_list = []
# number = 1
# while number < 11:
#     num_list.append(number)
#     number += 1
# print(num_list)

#### 2. Write a for loop that prints number 1 to 10 on screen

# list = []
# for i in range(1, 11):
#     list.append(i)
# print(list)

####3. Write for loop that iterates from 0 to 20. For each iteration it checks if
####number is even or odd and prints: 1 is odd, 2 is even

# for n in range(0, 21):
#     if n % 2 == 0:
#         print(n, "is even")
#     elif n % 2 == 1:
#         print(n, "is odd")

####4. Write a for loop that iterates from 0 to 10. For each iteration it will
#### multiply by 9 and print: 2 * 9 = 18
#
# for i in range(0, 11):
#     print(i, "multiplied by 9 equals: ", i * 9)

####5. Program that asks for a number and prints the sum of all numbers from 1
#### to the number they enter.

# number = int(input("Please enter a number: "))
# total = 0
# for i in range(0, number):
#     total += i
# print(total)

#### 6. Write a program to calculate and print the factorial of a number using a
#### for loop. EG. factorial of 4: 4*3*2*1 = 24

# total = 1
# number = int(input("Please enter a number: "))
# for i in range(1, number + 1):
#     total = total * i
# print(total)

#### 7. Program to ask for a number and print it on the screen. Keep asking until
#### a negative is given.

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

#
# for i in range(0, 5):
#     for j in range(0, (i+1)):
#         print("*", end="")
#     print(" ")

for i in range(0, 5):
    for j in range(0, (i+1)):
        print("*", end="")
    # print("")