#CS 232 lab 09
#Luis Ruiz

#Problem 1#
#gettysburg: single char string -> int
#expects: a single character string
#returns: int value of how many words in Gburg Address start w that letter
#side effects: prints a formatted output to screen
import os
os.chdir("C:\\Users\\lr165\\Desktop")
my_file = open("GettysburgAddress.txt", 'rt')
my_string = my_file.read()
my_list = my_string.split()

def gettysburg(var):
    counter = 0
    for i in my_list:
        if(i[0] == var):
            counter += 1
    print("There are ", counter, " words in the Getysburg Address that start with '", var, "'")


#Problem 2#
#count_sentences: string -> int
#expects: filename as a string
#returns: int value of how many sentences found in that file
#side effects: prints a formatted output to screen.

import re
def count_sentence(file):
    counter = 0
    my_file = open(file, 'rt')
    my_string = my_file.read()
    my_list = my_string.split()
    for i in my_list:
        if(i[-1] == '!' or i[-1] == '.' or i[-1] == '?'):
            counter += 1
    print("there are ", counter, "sentences in ", file)
    
    

    

    
