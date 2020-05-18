                        ####LAB 6- Functions####



####Lab exercise 1: Function takes and number and prints range from 1 to that number####
# Can't add end to print_range


# def print_range(int):
#     for i in range(1, int + 1):
#         print(i, end="")
#
#
# number = int(input("Please enter a number: "))
# print_range(number)

####Lab exercise 2: Function that takes a number and iterates from 0 to that number.
# Check if the number is even or odd####

# def even_or_odd(int):
#     for i in range(1, int + 1):
#         if i % 2 == 0:
#             print("The number", i, "is even")
#         else:
#             print("The number", i, "is odd")
#
#
# number = int(input("Please enter a number: "))
# even_or_odd(number)

####Lab Exercise 3: Function that takes a number, iterates from 0 to that number. For each iteration multiply by 9
# print the result: '2 * 9 = 18'####

# def multiple(a):
#     for i in range(a + 1):
#         print(i, "* 9 = ", i * 9)
#
# number = int(input("Please enter a number: "))
# multiple(number)

####Lab Exercise 4: Function that asks for a number and prtins the sum from 1 to the number####

# def sum_range(a):
#     x = sum(range(0, a + 1))
#     print(x)
#
#
# number = int(input("Please enter a number: "))
# sum_range(number)


####Lab Exercise 5: Function to print a factorial of a number####

# def fac_range(a):
#     x = 1
#     for i in range(a + 1):
#         result = x * i
#         # print(result)
#
# num = int(input("Please enter a number: "))
# print(fac_range(num))

# def sum_numbers(number):
#     num_mult = 1
#     for i in range(number, 0, -1):
#         num_mult *= i;
#     return num_mult
#
# print(sum_numbers(int(input("Enter a number: "))))


####Lab Exercise 6: Function that takes a string and returns a string made of the first and last 2 characters.
# Check if string is less that 4


# def jumbotron(myStr):
#     if len(myStr) <= 4:
#         print("Error! Too short.")
#     else:
#         return myStr[:2] + myStr[-2:]
#
# print(jumbotron(input("Enter a string of over 4 chars to be clipped: ")))

####Lab Exercise 7: Program to remove characters with odd index. Return new string

####Lab Exercise 8: Function to get first half of string of even length
#eg. 'Python' should return Pyt

####Lab Exercise 9: Function to insert string in the middle of a string.
#CHECK FUNCTIONS LAB FOR COMPLEX EXAMPLE####

####Lab Exercise 10: Function that takes a string and 2 indices,
#and then removes the part between the indicies.
#eg. 'Hello there': Hehere

