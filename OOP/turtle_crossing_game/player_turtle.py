from turtle import Turtle

TURTLE_COLOUR = "black"
STARTING_POSITION = (0,-280)
PLAYER_MOVE = 20

class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color(TURTLE_COLOUR)
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        self.forward(PLAYER_MOVE)
    
    def player_reset(self):
        self.goto(STARTING_POSITION)