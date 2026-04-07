from turtle import Turtle
import random

CAR_COLOURS = ("red","blue","green","yellow","purple","orange","cyan")
CAR_LENGTHS = (1.5, 2.0, 2.5)
CAR_LANES = range(-250,260,25)
START_XCORDS = (300,310,320,330)
MOVE = 10

class Cars():
    def __init__(self):
        self.cars = []
        self.generate_car()
    
    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=random.choice(CAR_LENGTHS),stretch_wid=1)
        new_car.color(random.choice(CAR_COLOURS))
        new_car.penup()
        new_car.goto(random.choice(START_XCORDS),random.choice(CAR_LANES))
        new_car.seth(180)
        self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars[:]:
            car.forward(MOVE)
            if car.xcor() < -310:
                car.ht()
                self.cars.remove(car)