from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        for position in STARTING_POSITION:
            new_tail = Turtle(shape="square")
            new_tail.color("white")
            new_tail.penup()
            new_tail.goto(position)
            self.snake_body.append(new_tail)
    
    def move(self):
        for tail in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[tail - 1].xcor()
            y = self.snake_body[tail - 1].ycor()
            self.snake_body[tail].goto(x,y)
        self.snake_body[0].forward(MOVE_DISTANCE)
