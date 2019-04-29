#CS 232 Spring 2019 - Week 8 Lab
#Luis Ruiz

#more_vowels: string, string -> int
#expects: two strings, returns int
#side effects: prints a statement for the string
#                that has more vowels in it
from collections import Counter

def more_vowels(string1, string2):
    vowels = ['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U']

    c1 = 0
    c2 = 0

    count1 = Counter(string1)
    count2 = Counter(string2)
    
    for i in count1:
        if i in vowels:
            c1 += 1
            
    for j in count2:
        if j in vowels:
            c2 += 1

    if c1 < c2:
        print('The first string has more vowels')
        return 1
    elif c2 < c1:
        print('The second string has more vowels')
        return 2
    else:
        print('The strings have an equal number of vowels')
        return 0
