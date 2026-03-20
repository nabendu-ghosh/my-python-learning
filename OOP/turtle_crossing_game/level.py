from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 8, "normal")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.goto(280,280)
        self.level = 1
        self.write(arg=f"Level ${self.level}",align=ALIGN,font=FONT)