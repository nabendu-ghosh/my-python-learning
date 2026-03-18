from turtle import Turtle

STARTING_POSITION = (0,280)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.write("Score: 0",align="center",font=("Arial",10,"bold"))