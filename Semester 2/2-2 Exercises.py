                    ####Lab 2-2 Dictionary Exercises ####

####Exercise 1####
#Function that takes dictionary and office number and prints
#prints the name of person in that office#

# contacts = {'John': '001',
#             'Alex': '002',
#             'Bill': '003',
#             'Jane': '004'}
#
# def room_name(x):
#     return ['x']['0']
#
# room_name(contacts)


####Exercise 1####
#function to add an entry to dictionary#
#
contacts = {'John': ['0987', 'room 1'],
            'Alice': ['0977', 'room 2'],
            'Claire': ['0966', 'room 3'],
            'Jake': ['0955', 'room 4']}
#
# def add_contact(a, b, c):
#     """to add to a dictionary"""
#     contacts.update({a: [b, c]})
#
# a = input("Please enter a name: ")
# b = input("Please enter a phone number: ")
# c = input("Please enter a room number: ")
# add_contact(a, b, c)
#
# print(contacts)

####Exercise 2####
#Function that will find certain letter####

# dictionary = input("Please enter a dictionary to search: ")
# letter = input("Please enter a letter to search for: ")
#
# word_list = []
# for i in dictionary:
#     if i[0] == letter:
#         word_list.append(i)
# print(word_list)

# test = "Alex is working on Python"
#
# letter = input("Please enter a letter to search for: ")
# count = 0
# for i in test[0:]:
#     if i == letter.upper():
#         count += 1
# print(count)

# dictionary = input("Please enter a dictionary to search: ")
# letter = input("Please enter a letter to search for: ")
#
# name_list = []
# for i in dictionary:
#     if i[0:] is letter.upper():
#         name_list.append(i)
#
# print(name_list)

test = ["alex", "Atnon", "Rachel"]

print(test[0])

