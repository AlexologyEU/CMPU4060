
####4. Write a program that will reverse a string (using a loop)

# string = input("Enter a string: ")
# end = ""
#
# for i in string.split()[::-1]:
#     end += i
#
# print(end)

string1 = "Hello there"
string2 = ""

i = len(string1)-1

while(i >= 0):
    string2 = string2 + string1[i]
    i = i-1
print(string2)