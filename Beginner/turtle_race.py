from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
colours = ["red", "blue", "green", "black", "yellow"]
user_choice = screen.textinput(title="Choose your Turtle", prompt="Pick a colour: ")

turtle = {}
y = -100
pace = [5, 7, 8, 9, 10]
play = True
winner = ""

def generate_turtles():
    global y
    for colour in colours:
        turtle[colour] = Turtle(shape="turtle")
        turtle[colour].color(colour)
        turtle[colour].penup()
        turtle[colour].goto(-240, y)
        y += 50

def race_turtle():
    for colour in colours:
        turtle[colour].forward(random.randint(0, 10))

def winnier_turtle():
    global winner
    for colour in colours:
        if turtle[colour].xcor() >= 240:
            print(f"Winning Turtle: {colour}")
            if colour == user_choice:
                print("You Win")
            else:
                print("You Lose")
            return False  
    return True
        

if user_choice:
    generate_turtles()

while play:
    race_turtle()
    play = winnier_turtle()

screen.exitonclick()