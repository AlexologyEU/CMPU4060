#### LAB 7- Lists ####

####Question 1: Program to write all the numbers in a list####
# num = [1, 2, 3]
# b = sum(num)
# print(b)

####Question 2: Function to get the largest number from a list####
# l_1 = []
# num = int(input("Please enter a number, enter a negative to end: "))
# while num >= 0:
#     l_1.append(num)
#     print(l_1)
#     num = int(input("Please enter a number, enter a negative to end: "))
# print("The largest number in the list is: ", max(l_1))


####Question 3: Function that takes a list of words and counts
# how many begin with 'a'#### FOR STATEMENT MESSES IT UP ASK#####
# word_list = []
# word = str(input("Please enter a word, type 'stop' to end: "))
# count = 0
# while word != "stop":
#     word_list.append(word)
#     # for i in word_list:
#     if word[0] == "a" or word[0] == "A":
#         count += 1
#     word = str(input("Please enter a word, type 'stop' to end: "))
# print(word_list)
# print(count)

####Question 4: Function that takes a list of words and a
# character and counts how many of the words begin with that char#### Check with teacher ####
# word_list = []
# word = str(input("Please enter a word, type 'stop' to end: "))
# char = str(input("Please select a character to search for: "))
# count = 0
# while word != "stop":
#     word_list.append(word)
#     if word[0] == char or word[0] == char.capitalize():
#         count += 1
#     word = str(input("Please enter another word, type 'stop' to end: "))
# print(word_list)
# print(count)

####Question 5: Function that takes a list of numbers ad returns a new list with
# only the even numbers####
# num_list = []
# num = int(input("Please enter a number, enter a negative to end: "))
# while num >= 0:
#     if num % 2 == 0:
#         num_list.append(num)
#     num = int(input("Please enter a number, enter a negative to end: "))
# print(num_list)