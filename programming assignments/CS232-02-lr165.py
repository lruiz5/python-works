#CS232-02-lr165
#Luis Ruiz
#Last Modified: 26 Feb 2019

#Problem 1

#letter_freq: string -> dict
#purpose: expects a string(sentence, phrase, or other such language fragment
#           containing only letters or spaces. no punctuation.
#           returns a python dictionary with each character in the string
#           as the key(lowercase) and the number of times found in the string
#           as a value.
#side effects: prints the dictionary of characters paired with frequency of each char.

def letter_freq(a_sentence):
    sentence_dict = {}

    a_sentence = a_sentence.lower()

    a_sentence = sorted(a_sentence)

    for i in a_sentence:
        sentence_dict.update({i : a_sentence.count(i)})

    return sentence_dict

#Problem 2

#freq_bar_chart: dictionary -> returns nothing
#purpose: expects a dictionary of letter frequencies (prob 1)
#           returns nothing.
#side effects: prints to the screen a horizontal bar chart of the letter
#               frequencies found in the dictionary passed to it.

def freq_bar_chart(a_dict):
    print('***LETTER FREQUENCY CHART***')

    for key,val in a_dict.items():
        if(key.isalpha()):
            print(key, '-', end = ' ')
            for i in range(0, val):
                print('X', end = '')
            print('\n')


#Problem 3
# ASSIGNMENT 2 - CODE TO INSERT BEFORE PROBLEM 3
# DO NOT ALTER THIS CODE IN ANY WAY!
# max_coordinate_value: dict int -> int
# Expects a dictionary of letters and ordered pairs,
#     and an index value
# Returns the maximum value of the X coordinates if
#     the index value is 0, and the maximum value of
#     the Y coordinates if the index value is 1

def max_coordinate_value(the_dict, the_index):
    max_val = 0
    for a_point in the_dict:
        the_ordered_pair = the_dict[a_point]
        # max_val will have the largest value found so far
        if max_val < the_ordered_pair[the_index]:
            max_val = the_ordered_pair[the_index]

    return max_val

#plot_points: dictionary -> returns nothing
#Expects a dictionary of letters and ordered pairs
#Returns nothing
#Side effects: prints a graph of the key plotted
#               at the ordered pair on screen

def plot_points(points_dict):
    max_x = max_coordinate_value(points_dict, 0)
    max_y = max_coordinate_value(points_dict, 1)
    yline = max_y#counter for  plane

    graph = []

    for i in range(0, max_y + 1):
        graph.append([])
        for j in range(0, max_x + 1):
            graph[i].append('.')

    a = list(points_dict.get('a', 'none'))

    for key, value in points_dict.items():
        

    graph[0].remove('.')
    graph[0].insert(, 'a')

    graph[1].remove('.')
    graph[1].insert(1, 'b')

    graph[2].remove('.')
    graph[2].insert(6, 'c')
    
    for k in graph:
        print(yline, end = ' ')#print the line numbers for y plane
        print(*k)
        yline -= 1#decrement
    print(' ', end = ' ')
    for index in range(0, max_x + 1):
        print(index, end = ' ')#print the line numbers for x plane


#Problem 4
# ASSIGNMENT 2 - CODE TO INSERT BEFORE PROBLEM 4
# DO NOT ALTER THIS CODE IN ANY WAY!

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-. "

# relative_prime: int int -> bool
# Expects two positive integers >= 2
# Returns True if the integers are relatively prime
# (that is, is their Greatest Common Divisior is 1)
# DO NOT ALTER THIS CODE!

def relative_prime(num_1, num_2):
    a, b = num_1, num_2
    while (b > 0):
        gcd = b
        b = a % b
        a = gcd
    return gcd == 1

# create_code_ring: int -> dict
# Expects a "seed" integer to initialize code mapping
# Returns a dictionary that maps each character in the
# string constant ALPHABET to an int from 1 to the
# length of the alphabet
# DO NOT ALTER THIS CODE!

def create_code_ring(seed):
    '''Expects an integer
       Returns a dictionary mapping each letter of a string
       constant ALPHABET to an integer from 1 to len(ALPHABET)'''
    
    alphabet_len = len(ALPHABET)
    
    # Use seed to set a usable (relatively prime) increment value
    inc_val = seed % alphabet_len
    if inc_val <= 1:
        inc_val = 2
    while not relative_prime(inc_val, alphabet_len):
        inc_val += 1

    # Inititalize index value and code_ring dictionary
    cur_idx = alphabet_len - 1
    code_ring = {}

    for i in list(ALPHABET):
        # Set next index value for mapping
        next_idx = (cur_idx + inc_val) % alphabet_len
        # print(i, " ", next_idx + 1) # UNCOMMENT TO SEE MAPPING
        code_ring.update({ i : next_idx + 1 })
        cur_idx = next_idx
    return code_ring

#encode_message: string, int -> list
#expects a string to be encoded and a seed number.
#returns a list of int values, the numbers that corrospond
#to the letters inthe string as found in the code ring dict
#side effects: will print the list of int values to screen

def encode_message(sentence,seed):
   code_ring = create_code_ring(seed)
   code = []
   the_message = list(sentence.upper())
   for i in the_message:
     if i in code_ring.keys():
         code.append(code_ring[i])
     elif i not in code_ring.keys():
         code.append(99999)
   return code

#decode_message: list, int -> string
#expects a list of int values that represent an encoded message
#       along with an integer seed value.
#returns the decoded message as a string
#side effects: will print the decoded message string to screen

def decode_message(code,seed):
    code_ring = create_code_ring(seed)
    decode = []
    inverse_dict = {a_value: a_key for a_key, a_value in code_ring.items()}
    for i in code:
        if i in inverse_dict.keys():
            decode.append(inverse_dict[i])
        elif i == 99999:
            decode.append('@')
    message = ''.join(decode)
    return message
