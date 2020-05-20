 
####1. Write a function to read a sentence and return a list of the length
####of each word.
####1.a use the function to read a file and return the length of each word
####on each line

#### Example from Stack: print([len(x) for x in test.split()])

# #1.
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

def word_reverse(text):
    words = text.split()
    result = []

    for i in words:
        if i[0] == 'a':
            result.append(i[::-1])

        else:result.append(i)
    end = " ".join(result)
    return end

test = input("Enter: ")
print(word_reverse(test))



























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

####Exercise 3####

# list = [1, 2, 5, 6, 2, 7, 1, 2]
# new_list = []
#
# for i in list:
#     if i == 2:
#         new_list.append(200)
#     else:
#         new_list.append(i)
# print(new_list)




