#CS232-01-lr165.py
#Luis Ruiz
#Last Modified: 07 February 2019


#problem 1*****
#multiples_in_range: number number number -> int
#purpose: expects three integer values returns each 
#           of the values of the numeric value that 
#           fall strictly between the beginning and
#           ending values
#side effects: prints the number that is a multiple
#               of the numeric value in question.
#               also prints the number of total multiples
#               of the numeric value given to the function

def multiples_in_range(numeric_value, beginning, ending):
    i = beginning
    multiple_counter = 0
    for i in range(beginning + 1, ending):
        if(i % numeric_value == 0):
            multiple_counter += 1
            print(i)
    return multiple_counter


#problem 2*****
#letter_grade: float -> string
#purpose: expects a numeric grade greater than 0.0 represented as a float
#           returns the letter grade corresponding to the numeric grade
#side effects: prints the corresponding letter grade as a result.

def letter_grade(N):
    if(N >= 90.0):
        print('A', end = '')
        if(N > 97.0):
            print('+')
        elif(N >= 90.0 and N < 93.0):
            print('-')
        return 'A'
    elif(N >= 80.0 and N < 90.0):
        print('B', end = '')
        if(N >= 87.0 and N < 90.0):
            print('+')
        elif(N >= 80.0 and N < 83.0):
            print('-')
        return 'B'
    elif(N >= 70.0 and N < 80.0):
        print('C', end = '')
        if(N >= 77.0 and N < 80.0):
            print('+')
        elif(N >=70.0 and N < 73.0):
            print('-')
        return 'C'
    elif(N >= 60.0 and N < 70.0):
        print('D', end = '')
        if(N >= 67.0 and N < 70.0):
            print('+')
        elif(N >=60.0 and N < 63.0):
            print('-')
        return 'D'
    else:
        print('F')
        return 'F'


#problem 3*****
#bump_it: int -> int + 1, float + 0.1,
#           string -> string + '!', bool -> opposite of given value
#           any other molecular data type -> same value that was passed
#purpose: expects an int, float, string, or bool.
#           returns int + 1, float + 0.1, string  + '!',
#           or boolean's opposite value respectively.
#           any other arguement is echoed back
#side effects: if int: prints value + 1, if float: prints value + 0.1
#               if string: prints value + '!', if bool: prints boolean opposite
#               if anything else, prints value

def bump_it(value):
    if type(value) == int:
        return value + 1
    elif type(value) == float:
        return value + 0.1
    elif type(value) == str:
        return value + '!'
    elif type(value) == bool:
        return not value
    else:
        return value


#problem 4*****
#my_nickname: string -> string
#purpose: expects a one word first name string
#           prints and returns a goofy nickname
#           always with a capitalized first letter
#           if the length of the name is less than
#           5 letters the name will not be "nickname-ized"
#           if the length of name is more than 5 letters,
#           name will be "nickname-ized" by taking the first
#           5 letters of the name, discarding the rest and:
#           if 5th letter is 'y', strip off the y
#           if 5th letter is not 'y', append a 'y' to the nickname
#side effects: returns a nickname for any name 5 letters or longer
#               returns full ame otherwise

def my_nickname(name):
    name = name.capitalize()
    if (len(name) < 5):
        return name
    else:
        name_list = list(name)
        del name_list[5:]
        if name_list[4] == 'y':
            del name_list[4]
        else:
            name_list.append('y')
        name = ''.join(str(x) for x in name_list)
        return name


#problem 5*****
#flip_case: string -> string
#purpose: if arguement is all upper, returns all lower
#           if all lower, returns all upper
#           if neither of these cases apply:
#               look at first char.
#                   if upper, return string with lowercase first char
#                   if lower, return string with uppercase first char
#side effects: prints nothing. returns all lower if arg is upper
#               returns all upper if arg is lower
#               if neither, capitalizes if first char is lower
#                           lowercases if first char is upper

def flip_case(word):
    if word.isupper():
        return word.lower()
    elif word.islower():
        return word.upper()
    else:
        if(word[0].islower()):
            return word.capitalize()
        else:
            word = word[0].lower() + word[1:]
            return word


#problem 6*****
#fibonacci_list: positive integer -> list
#purpose: expects a positive integer value
#           returns a list of fibonacci numbers
#           of the given length
#side effects: returns list of fibo numbers

def fibonacci_list(length):
    fibo_list = [0, 1]
    for i in range(1, length):
        fibo_list.append(fibo_list[i] + fibo_list[i - 1])
    return fibo_list
