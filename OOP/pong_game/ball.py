from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.seth(45)
        self.penup()
    
    def move(self):
        self.forward(20)