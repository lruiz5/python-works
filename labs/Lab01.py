#CS 232 Spring 2019 - Week 02 Lab
#Luis Ruiz and Amanda Ortiz

###Problem 1###
#c_to_f: float -> float
#expects a float and returns a float
#converts celcius to farenheit

def c_to_f(temp):
    return (temp * 1.8) + 32

###Problem 2###
#c_to_f_check: float->float
#expects a float, returns a float
#converts celcius to farenheit, if
#the number passed to the function is
#less than -273.16, it will write an error
#message to the screen and return -99999

def c_to_f(temp):
    if(temp < -273.16):
        print("Temperature is too low!")
        return -99999
    else:
        return (temp * 1.8) + 32

###Problem 3###
#yell_it: does not return anything.
#expects one arguement.
#if arguement is a string, print to screen
# in all uppercase followed by !!!
#else it will print "Not a String!!!"

def yell_it(arguement):
    if(type(arguement) == type(" ")):
       print(arguement.upper(), '!!!')
    else:
       print("Not a String!!!")

###Problem 4###
#divisible_by: will print to screen whether
#that int is divisible by 2,3,4 and so on up to 10 inclusive
#expects a positive integer value
#returns nothing 

def divisible_by(number):
    if(number <= 0):
        print("Invalid Value")
    else:
        for i in range(2, 10):
            if(number % i == 0):
                print(number, " is divisible by " , i)
            else:
                print(number, " is not divisible by ", i)

###Problem 5###
#test_demorgan: tests whether demorgans law works for input values
#expects two boolean values as arguements
#returns true if demorgans laws are confirmed, false otherwise

def test_demorgan(P, Q):
    if(not(P and Q) == (not(P)) or not(P and Q) == (not(Q))):
        return True
    elif(not(P or Q) == (not(P)) and (not(P or Q)) and(not(Q))):
        return True
    else:
        return False
