#CS 232 Spring 2019 - week 05 Lab
#Luis Ruiz and Jesse Garcia

#Problem 1
while True:
    entry = input("Enter one letter at a time, x exits ")
    if entry == 'x':
        break

#Problem 2
for i in range (0, 30):
    if i % 3 == 0:
        continue
    print(i)

#problem 3
my_list = []
for i in range (0, 30):
    if i % 3 == 0:
        continue
    my_list.append(i)

print(my_list)


#Problem 4
#alpha_dict: 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alpha_dict = {}

j = 1
for i in alphabet:
    alpha_dict.update({j : i})
    j += 1

#Problem 5
#string_list: *args -> list
#expects any number of positional arguments with no keyword args
#and returna a list of all arguments passed to the function that are type str
def string_list(*args):
    string_list = []
    for i in args:
        if(type(i) == str):
            string_list.append(i)

    return string_list

# Problem 6
# list_at_index: tuple of tuples -> list
# expects a tuple of tuples and an integer index value
# returns a list of the items in the tuples that match the index
def list_at_index(a_tuple, index):
    length = []
    item = []
    
    for tupl in a_tuple:
        length.append(len(tupl))

        if index > min(length) - 1:
            return []
        elif index < 0:
            return "Expects a positive number, try again!"
        else:
            item.append(tupl[index])
    return item


