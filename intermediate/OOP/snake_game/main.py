from intermediate.OOP.snake_game.snake import Snake
from intermediate.OOP.snake_game.food import Food
from intermediate.OOP.snake_game.scoreboard import Scoreboard
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

    # check if snake eats food
    if snake.snake_head.distance(food) < 15:
        food.move_food()
        scoreboard.increase_score()
        snake.extend_tail_onscreen()
    
    #check if snake hit wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.game_reset()
        snake.reset()

    # check if snake hit itself
    for tail in snake.snake_body[1:]:
        if snake.snake_head.distance(tail) <10:
            scoreboard.game_reset()
            snake.reset()

    
screen.exitonclick()