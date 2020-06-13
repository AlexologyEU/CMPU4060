
# full_name = lambda first, last: f'Full Name: {first.title()} {last.title()}'
# print(full_name("alex", "murphy"))

# print((lambda x, y: x + y)(2, 3))

# cubeFunc = lambda x: x*x*x
# print("The cube of 5 is: ", cubeFunc(5))


def convert(num_list, n):
    new_list = []
    for i in num_list:
        new_list.append(n(i))
    return new_list


def cube(num):
    return num*num*num


num_list = [2, 3, 4, 5]
print("Original: ", num_list)
new_list = convert(num_list, cube)
print("Modified: ", new_list)

num_list.pop(0)
print(num_list)






