 
####1. Write a function to read a sentence and return a list of the length
####of each word.
####1.a use the function to read a file and return the length of each word
####on each line

#### Example from Stack: print([len(x) for x in test.split()])

# def word_measure(text):
#     len_list = []
#     for x in text.split():
#         len_list.append(len(x))
#     print(len_list)

# test = "This is a string to measure"
# word_measure(test)

# #1a. Needs a txt file accessible in project folder.
# test_file = open("1-8_files_exceptions_exercises.txt")
# for line in test_file:
#     word_measure(line)

####2.a Write a function to read a sentence and reverse every word that
####starts with an 'a'.
####2.b Use a function to read from a file, reverse each with that starts
#### with an 'a' and save the result into another file.


# string = input("Please enter an input: ")
# print(string[::-1])

# def word_reverse(text):
#     words = text.split()
#     result = []

#     for i in words:
#         if i[0] == 'a':
#             result.append(i[::-1])

#         else:result.append(i)
#     end = " ".join(result)
#     return end

# test = input("Enter: ")
# print(word_reverse(test))


####3. Write a function: replace_all that takes 3 parameters:
# - list
# - list of numbers to be replaced
# - list of numbers to use as replacement

# for example: replace_all([1,2,5,6,2,7,1,2], [2,4], [200, 400])
#  result: [1,200,5,6,200,7,1,200]
#
# def num_list_replace(num_list, search_list, replace_list):
#     result = []
#     for i in num_list:
#         if i == search_list[0]:
#             result.append(replace_list[0])
#         elif i == search_list[1]:
#             result.append(replace_list[1])
#         else:
#             result.append(i)
#     return result
#
#
# number_list = []
# search_list = []
# replace_list = []
#
# number = int(input("Enter a list of numbers. To end, input a null value: "))
# while number != 0:
#     number_list.append(number)
#     number = int(input("Enter a list of numbers. To end, input a null value: "))
#     if number == 0:
#         print("This is the completed number list: ", number_list)
#         break
#
# search = int(input("Enter a list of numbers to search for. To end, input a null value: "))
# while search != 0:
#     search_list.append(search)
#     search = int(input("Enter a list of numbers to search for. To end, input a null value: "))
#     if search == 0:
#         print("This is the completed search list: ", search_list)
#         break
#
# replace = int(input("Enter a number to be used as a replacement. To end, input a null value: "))
# while replace != 0:
#     replace_list.append(replace)
#     replace = int(input("Enter a number to be used as a replacement. To end, input a null value: "))
#     if replace == 0:
#         print("This is completed replacement list: ", replace_list)
#         break
#
# input("Press 'enter' to run the program")
# print(num_list_replace(number_list, search_list, replace_list))
#

####4. Write a function to replace every third word in a 
#sentence with 'hello'
#use the function to read from a file, and output into
#another file.
#
# def hello_step(string):
#     sen_split = string.split(" ")
#     for i in range(2, len(sen_split), 3):
#         sen_split[i] = "hello"
#     final = " ".join(sen_split)
#     return final
#
# # import shutil
# # shutil.copyfile("1-8_files_exceptions_exercises.txt", "1-8_files_copy.txt")
#
#
# in_file = open("1-8_files_exceptions_exercises.txt", "r")
# out_file = open("result.txt", "w")
#
# for text in in_file:
#     out_file.write(hello_step(text) + "\n")
#
# in_file.close()
# out_file.close()


####5. Write a function to replace every word that is longer than
# 6 characters with the word 'blah'
# use the function to read from a file, and output into
# another file

test = "Here is a test sentence with considerably longer words"
test_split = test.split(" ")
for length in test_split:
    if len(length) >= 6:
        length = "blah"
    end = " ".join(test_split)
print(end)


####6. Write a program that reads a file and generates a dictionary
# - a list of unique words. Save the words to a new file
# one word per line
























####Exercise 1####

# input_file = open("twinkle.txt", "r")
#
# len = []
# for i in input_file.split(" "):
#
# ####Exercise 1 solution####
# s = input("Enter a sentence: ")
# ls = []
# words = s.split()
# for w in words:
#     ls.append(len(w))
# print(ls)

####Exercise 1 in function####
# def calculate_len(s):
#     ls = []
#     words = s.split()
#     for w in words:
#         ls.append(len(w))
#     return ls
#
# ####Exercise 1 calling function####
# s = input("Enter a sentence: ")
# print(calculate_len(s))
# l = calculate_len(s)
# print(l[2])

####Exercise 1 with try####

# try:
#     fo = open("twinkle.txt", "r")
#     for line in fo:
#         print(calculate_len(line))
#     fo.close()
# except IOError:
#     print("File not available.")

####Exercise 2 ####
# def reverse_a(s):
#     words = s.split()
#     new_words = []
#
#     for w in words:
#         if w[0] == "a":
#             new_words.append(w[::-1])
#         else:
#             new_words.append(w)
#     new_s = " ".join(new_words)
#     return new_s
#
#
# try:
#     fo = open("twinkle.txt", "r")
#
#     for line in fo:
#         print(reverse_a(line))
#     fo.close()
#
# except IOError:
#     print("File not available. ")
#





