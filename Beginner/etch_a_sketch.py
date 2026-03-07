from turtle import Turtle, Screen

kurmo = Turtle()
screen = Screen()

def forward():
    kurmo.forward(50)

def backward():
    kurmo.backward(50)

def anti_clock():
    kurmo.left(10)

def clock():
    kurmo.right(10)

def clear_screen():
    kurmo.clear()
    kurmo.penup()
    kurmo.home()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(anti_clock, "a")
screen.onkey(clock, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()