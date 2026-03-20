from turtle import Turtle

TURTLE_COLOUR = "black"
STARTING_POSITION = (0,-280)

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color(TURTLE_COLOUR)
        self.penup()
        self.goto(STARTING_POSITION)
