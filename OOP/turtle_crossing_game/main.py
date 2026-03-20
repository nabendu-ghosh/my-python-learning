from turtle import Screen
import time
from cars import Cars
from player_turtle import PlayerTurtle
from level import Level

# Set up screen
screen = Screen()
screen.bgcolor("white")
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Road")

# Initialize game
game_on = True
cars = Cars()
player = PlayerTurtle()
level = Level()

screen.listen()
screen.onkey(player.move_up, "Up")

while game_on:
    cars.generate_car()
    cars.move_cars()
    time.sleep(level.car_speed)
    screen.update()

    if player.ycor() >= 280:
        player.player_reset()
        level.increase_level()
    
    for car in cars.cars:
        if player.distance(car) < 25:
            game_on = False

screen.exitonclick()