#####4. Write a program to find and print the sum of digits of a
####number entered by the user.

number = input("Please enter a string of numbers: ")
total = 0
for i in number:
    total = total + int(i)
print(total)