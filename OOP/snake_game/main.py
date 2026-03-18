from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(.15)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.move_food()
    
screen.exitonclick()