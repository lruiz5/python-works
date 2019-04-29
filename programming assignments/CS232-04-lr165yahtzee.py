# CS232-04-lr165
# Luis Ruiz
# Last modified: 16 April 2019

import random
import collections

NUM_SIDES = 6     # Number of sides on each dice
NUM_DICE = 5      # Number of dice in the game
NUM_ROLLS = 3     # Number of rolls for each test
NUM_TESTS = 1000  # Number of tests to perform
PRINT = True      # If True, print rolls to screen

# ***** Definition of Dice object class and methods go here ***
class Dice():
    def __init__(self, number_of_sides):
        self.sides = number_of_sides
        self.roll_value = 0

    def roll(self):
        self.roll_value = random.randint(1, self.sides)

    def value(self):
        return self.roll_value


# ***** End of Dice class definition **************************

# is_yahtzee: list of Dice objects -> bool
# expects a list of Dice objects
# returns True if all values of the Dice objects match
#     returns False otherwise

def is_yahtzee(my_dice):
    #create a list to hold roll values
    values = []
    for j in my_dice:
        values.append(j.roll_value)

    return all(x == values[0] for x in values)      

# ***** End of is_yahtzee function definition *****************

# list of Dice objects -> int
# expects a list of Dice objects
#    examines the values of the dice, and determines which value
#    is most common
# returns that most common value found
# Examples: the_dice values of [1, 5, 4, 5, 5] will return 5
#           the_dice values of [2, 6, 2, 6, 4] will return 2 or 6
def best_value_to_keep(my_dice):
    values = []
    for j in my_dice:
        values.append(j.roll_value)
        
    freq = dict(collections.Counter(values))

    most = list(freq.values())[0]
    key_to_return = 0
    
    for value in freq.values():
        if value > most:
            most = value

    for key, value in freq.items():
        if most == value:
            key_to_return = key

    return key_to_return

# ***** End of best_value_to_keep function definition *********

# print_dice: list of Dice objects -> nothing
# expects a list of Dice objects
# returns nothing
# side effect: prints to screen the values on the dice,
#              if the global variable PRINT is set to True

def print_dice(the_dice):
    if PRINT:
        print("The dice values are: {0}"\
              .format([i.value() for i in the_dice]))

# *************** play_yahtzee code goes here ********************

# play_yahtzee: list of Dice objects -> bool
# expects a list of Dice objects
#     Rolls the dice up to NUM_ROLLS times to try to get a "Yahtzee"
#     A Yahtzee is when all the dice have the same value
# returns True if a Yahtzee occurs, or False otherwise
# side effect: calling print_dice(the_dice) after each roll,
#     and, if global variable PRINT is set to True, prints a
#     single-line "Yahtzee" or "No Yahtzee" message at the end

def play_yahtzee(my_dice):
    rolls = 0
    for i in my_dice:
        i.roll()
        
    print_dice(my_dice)
    
    rolls += 1
    
    keep = best_value_to_keep(my_dice)

    while is_yahtzee(my_dice) == False and rolls != NUM_ROLLS:
        for j in my_dice:
            if j.value() != keep:
                j.roll()
        print_dice(my_dice)
        keep = best_value_to_keep(my_dice)
        rolls += 1

    if(is_yahtzee(my_dice)):
        print('*** YAHTZEE! ***')
    else:
        print('No Yahtzee :-(')

# *************** end play_yahtzee code **************************

# This code creates a list called my_dice[] of Dice objects

my_dice = []
for i in range(0,NUM_DICE):
    my_dice.append(Dice(NUM_SIDES))

# Write a loop to call play_yahtzee(my_dice) NUM_TIMES times.
# Use a local variable to keep track of the
# number of Yahtzees that occur, and compute the percentage of
# tests the resulted in a Yahtzee.  Print the number of tests,
# the number of Yahtzees, and the percentage of success
# to the screen in an easy to read and understand manner

yahtzees = 0

for i in range(0, NUM_TESTS):
    game = play_yahtzee(my_dice)
    if is_yahtzee(my_dice):
        yahtzees += 1

print('After {0} tests, we got {1} Yahtzees!'.format(NUM_TESTS, yahtzees))
print('The success rate was {0}'.format(yahtzees / NUM_TESTS))

# *** End of "main" code ***
