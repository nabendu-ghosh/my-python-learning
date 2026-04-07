from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(self.position,0)

    def up(self):
        if self.ycor() < 240:
            self.forward(20)
    def down(self):
        if self.ycor() > -240:
            self.backward(20)