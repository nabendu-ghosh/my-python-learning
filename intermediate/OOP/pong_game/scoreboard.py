from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.display_score()
    
    def increase_score(self, side: str):
        self.side = side
        if side == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.display_score()
    
    def display_score(self):
        self.goto(-40,250)
        self.write(arg=self.left_score,align=ALIGN,font=FONT)
        self.goto(40,250)
        self.write(arg=self.right_score,align=ALIGN,font=FONT)