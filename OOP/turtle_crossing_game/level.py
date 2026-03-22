from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "bold")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.penup()
        self.goto(-250,270)
        self.level = 1
        self.write(arg=f"Level: {self.level}",align=ALIGN,font=FONT)
        self.car_speed = 0.2
    
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level {self.level}",align=ALIGN,font=FONT)
        self.car_speed *= 0.5
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",align=ALIGN,font=FONT)