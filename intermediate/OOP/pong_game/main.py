from turtle import Screen
from intermediate.OOP.pong_game.paddle import Paddle
from intermediate.OOP.pong_game.ball import Ball
from intermediate.OOP.pong_game.scoreboard import Scoreboard
import time

#Initialize screen/game
screen = Screen()
left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()
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
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bounce when collide with upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    
    # bounce when collide with paddle
    if  ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
    
    # ball misses paddle
    if ball.xcor() > 390:
        ball.ball_home()
        scoreboard.increase_score("left")
    elif ball.xcor() < -390:
        ball.ball_home()
        scoreboard.increase_score("right")
screen.exitonclick()