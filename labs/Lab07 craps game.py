#CS 232 Spring 2019 - Week 07 Lab
#Luis Ruiz

import random

def dice_roller():
    while True:
        first = random.randint(1,6)
        second = random.randint(1,6)
        total = first + second
        yield total

roll_dice = dice_roller()

#play_craps:nothing->bool
#expects: nothing 
#returns: a boolean value, True for win False for you lose
def play_craps():
    first_roll = next(roll_dice)
    if first_roll == 7 or first_roll == 11:
        return True
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    else:
        point = first_roll

    next_roll = next(roll_dice)
        
    while next_roll != 7 or next_roll != point:
        next_roll = next(roll_dice)
        if next_roll == point:
            return True
        elif next_roll == 7:
            return False

        
#run_trails int->nothing
#expects: positive integer
#returns: nothing
#side effects: prints out how many of the craps game played were won, 
#how many were lost, and overall winning percentage 
def run_trials(positiveint):
    game_counter, win_counter = 0, 0
    for i in range(0,positiveint):
       result = play_craps()
       game_counter += 1
       if result == True:
           win_counter += 1

    lose_counter = game_counter - win_counter
    win_percentage = (win_counter / game_counter) * 100
    print('I won ', win_counter, 'times and lost ',lose_counter, 'times.')
    print('Overall winning percentage was %', win_percentage)

    
