from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(350,0)

    def up(self):
        self.forward(20)
    def down(self):
        self.backward(20)