from turtle import Turtle

STARTING_POSITION = (0,280)
ALIGN = "center"
FONT = ("Arial",10,"bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("intermediate/OOP/snake_game/data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.ht()
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGN,font=FONT)
    
    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("intermediate/OOP/snake_game/data.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGN,font=FONT)