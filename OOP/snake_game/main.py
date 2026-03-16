from snake import Snake
from turtle import Turtle, Screen
import time

kurmo = Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
game_on = True

while game_on:
    screen.update()
    time.sleep(.05)
    snake.move()
    
screen.exitonclick()