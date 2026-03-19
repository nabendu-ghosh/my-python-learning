from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

#Initialize screen/game
screen = Screen()
left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
game_on = True

#Screen setup
screen.setup(width=800,height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

#Paddle control
screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

while game_on:
    time.sleep(.2)
    screen.update()
    ball.move()

screen.exitonclick()