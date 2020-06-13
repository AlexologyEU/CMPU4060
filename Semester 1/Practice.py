
####5. Write a program that will 'encrypt' a string. Add 1 to the
####ASCII code ('a' becomes 'b')
####use ord + chr

y = chr(65)
print(type(y), y)



for i in range(65, 65 + 26):
    print(chr(i), end="")