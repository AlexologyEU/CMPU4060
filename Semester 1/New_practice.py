
# full_name = lambda first, last: f'Full Name: {first.title()} {last.title()}'
# print(full_name("alex", "murphy"))

# print((lambda x, y: x + y)(2, 3))

# cubeFunc = lambda x: x*x*x
# print("The cube of 5 is: ", cubeFunc(5))

#
# def convert(num_list, n):
#     new_list = []
#     for i in num_list:
#         new_list.append(n(i))
#     return new_list
#
#
# def cube(num):
#     return num*num*num
#
#
# num_list = [2, 3, 4, 5]
# print("Original: ", num_list)
# new_list = convert(num_list, cube)
# print("Modified: ", new_list)
#
# num_list.pop(0)
# print(num_list)
#

# print("Welcome to the Tic Tac Toe game, you have the first turn: ")

# a_1 = ""
# a_2 = ""
# a_3 = ""
# b_1 = ""
# b_2 = ""
# b_3 = ""
# c_1 = ""
# c_2 = ""
# c_3 = ""
#
# while game_over is false:
#
#     choice = input("Your turn: ")

import tkinter as tk
from tkinter import *
from tkinter import ttk

class space(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("first time")
        self.button1 = Button(self, text = "Click Here", width = 25,
                              command = self.new_window)
        self.button1.grid(row = 0, column = 1, columnspan = 2, sticky = W+E+N+S)








