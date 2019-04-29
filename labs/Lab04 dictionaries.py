#CS 232 Spring 2019
#Luis Ruiz and Jacob Castro

#Problem 1
#Expects no arguements, returns nothing
#prints the number of key-value pairs in PRICE_DICT
#   all of the keys and values in PRICE_DICT as a list
#   Updates and then prints the value associated with 'apples' to 1.99
#   adds then prints 'grapes' and 2.68 to dictionary
#   the result of a boolean expression True if 'cauliflower' is a key found in dictionary
#   A statement that removes the item with the key 'broccoli'
#       and confirms on screen that it has been removed
#   the sum of all values in the dictionary

PRICE_DICT = {"apples" : 0.99, "bananas" : 0.49, "pears" : 1.25,
              "carrots" : 1.99, "broccoli" : 0.89}

def problem_1():
    print("The number of key value pairs is ",len(PRICE_DICT))
    
    print("The value corresponding to the key 'carrots' is ", PRICE_DICT['carrots'])
    values_list = list(PRICE_DICT.values())
    keys_list = list(PRICE_DICT.keys())
    
    print(keys_list)
    print(values_list)
    
    PRICE_DICT.update({'apples': 2.68})
    
    print(PRICE_DICT['apples'])

    add_to_dict = {'grapes': 2.68}
    
    PRICE_DICT.update(add_to_dict)
    
    print(add_to_dict)
          
    if(PRICE_DICT.keys() == 'cauliflower'):
          return True
          
    del PRICE_DICT['broccoli']   
    print("Broccoli removed.")
          
    values_list = list(PRICE_DICT.values())
          
    sum = 0
    for i in values_list:
          sum += i

    print(sum)

#problem 2
# max_coordinate_value: dict, int-> int
# purpose: takes a dictionary and an integer(0 for x,1 for y)
#       return max value of that coordinate within all of the tuples in dictionary

my_points = { 'a': (4,3), 'b':(1,2),'c':(5,1)}
def max_coordinate_value(a_dict, integer):
    if integer == 0:
        a_list = []
        for i in a_dict:
            a_list.append(a_dict[i][integer])
        return max(a_list)
    else:
        b_list = []
        for i in a_dict:
            b_list.append(a_dict[i][integer])
        return max(b_list)
