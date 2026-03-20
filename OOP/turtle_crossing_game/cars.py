from turtle import Turtle
import random

CAR_COLOURS = ("red","blue","green","yellow","purple","orange","cyan")
START_XCORD = 350
MOVE = 10

class Cars():
    def __init__(self):
        self.cars = []
        self.generate_car()
    
    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=1.5,stretch_wid=1)
        new_car.color(random.choice(CAR_COLOURS))
        new_car.penup()
        new_car.goto(START_XCORD,random.randint(-280,280))
        new_car.seth(180)
        self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE)
    


