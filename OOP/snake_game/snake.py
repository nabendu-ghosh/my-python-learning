from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake_body()
        self.snake_head = self.snake_body[0]
    
    def create_snake_body(self):
        for position in STARTING_POSITION:
            self.add_snake_tail(position)
    
    def add_snake_tail(self, position):
        new_tail = Turtle(shape="square")
        new_tail.color("white")
        new_tail.penup()
        new_tail.goto(position)
        self.snake_body.append(new_tail)
    
    def extend_tail_onscreen(self):
        self.add_snake_tail(self.snake_body[-1].position())
    
    def move(self):
        for tail in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[tail - 1].xcor()
            y = self.snake_body[tail - 1].ycor()
            self.snake_body[tail].goto(x,y)
        self.snake_head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)