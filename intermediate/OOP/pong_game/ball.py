from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
    
    def move(self):
        x_cord = self.xcor() + self.x_move
        y_cord = self.ycor() + self.y_move
        self.goto(x_cord,y_cord)
    
    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
   
    def ball_home(self):
        self.home()
        self.paddle_bounce()
        self.ball_speed = 0.1
