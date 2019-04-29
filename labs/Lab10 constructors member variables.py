# CS 232 Spring 2019 - Week 10 Lab
# Luis Ruiz

#Simulates a car moving on a grid
#focus of this lab is constructors and
#member variables. 
import math

class Car():
    def __init__(self, x_pos, y_pos):
        self.x_position = x_pos
        self.y_position = y_pos
        self.direction = 0
        self.speed = 0

    def turn(self, left_or_right):
        if self.direction == 3 and left_or_right == 'right':
            self.direction = 0
        if self.direction == 0 and left_or_right == 'left':
            self.direction = 3
        elif left_or_right == 'left':
            self.direction -= 1
        elif left_or_right == 'right':
            self.direction += 1
        
    
    def drive(self, time):
        if self.direction == 0:
            self.y_position += self.speed * time
        elif self.direction == 1:
            self.x_position += self.speed * time
        elif self.direction == 2:
            self.x_position -= self.speed * time
        elif self.direction == 3:
            self.x_position -= self.speed * time
            
    def print_status(self):
        print('current position is ({0}, {1})'.format(self.x_position, self.y_position))
        print('Current speed is {0}'.format(self.speed))
        if self.direction == 0:
            print('Current direction is up')
        elif self.direction == 1:
            print('Current direction is right')
        elif self.direction == 2:
            print('Current direction is down')
        elif self.direction == 3:
            print('Current direction is left')
        
    
    def accelerate(self, amount):
        self.speed = amount

    def stop(self):
        self.speed = 0
    
    def distance_from_origin(self):

        answer = math.sqrt(self.x_position**2 + self.y_position**2)
        print("my_car's distance from (0,0) is {0:.2f} units".format(answer))

my_car = Car(0,0)
my_car.print_status()
my_car.accelerate(10)
my_car.drive(3)
my_car.print_status()
my_car.turn('left')
my_car.drive(2)
my_car.print_status()
my_car.stop()
my_car.print_status()

my_car.distance_from_origin()




