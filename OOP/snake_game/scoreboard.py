from turtle import Turtle

STARTING_POSITION = (0,280)
ALIGN = "center"
FONT = ("Arial",10,"bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",10,"bold"))
