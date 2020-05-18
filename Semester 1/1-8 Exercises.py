####Lab Exercise 1####

# input_file = open("twinkle.txt", "r")
# out_file = open("twinkle_2.txt", "w")
# try:
#     for line in input_file:
#         out_file.write(line)
#         out_file.write("\n")
# except IOError:
#     print("Error, no such file exists!")
# else:
#     print("The file copied successfully")
#
# input_file.close()
# out_file.close()

####Lab Exercise 2####

# input_file = open("twinkle.txt", "r")
# out_file = open("twinkle_2.txt", "w")
# try:
#
#     for line in input_file:
#         out_file.write(line[::-1].strip())
#         out_file.write("\n")
#
# except IOError:
#     print("Error, no such file exists!")
# else:
#     print("The file copied successfully")
#
# input_file.close()
# out_file.close()

####Lab Exercise 3####

# input_file = open("twinkle.txt", "r")
# out_file = open("twinkle_2.txt", "w")
# try:
#
#     for line in input_file:
#         if line[0:4] == "When":
#             out_file.write(line)
#             out_file.write("\n")
#
# except IOError:
#     print("Error, no such file exists!")
# else:
#     print("The file copied successfully")
#
# input_file.close()
# out_file.close()


####Lab Exercise 4####

# input_file = open("twinkle.txt", "r")
# out_file = open("twinkle_2.txt", "w")
# try:
#
#     for line in input_file:
#         out_file.write(str(len(line)))
#         out_file.write("\n")
#
# except IOError:
#     print("Error, no such file exists!")
# else:
#     print("The file copied successfully")
#
# input_file.close()
# out_file.close()