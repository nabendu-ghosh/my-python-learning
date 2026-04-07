import turtle as t
import random
from intermediate.OOP.dot_art.extract_colour import ExtractColours

kurmo = t.Turtle()
screen = t.Screen()
screen.colormode(255)
kurmo.pensize(10)
kurmo.ht()

colours = ExtractColours("OOP/dot_art/spot_painting2.jpg", 30)
colour_palette = colours.get_colours()
starting_position = kurmo.position()

def draw_spots(dots):
    for _ in range(dots):
        x = -250
        y = -250
        y = y + 50 * _
        kurmo.penup()
        kurmo.goto(x, y)

        for circle in range(dots):
            size = [18, 19, 20]
            kurmo.dot(random.choice(size), random.choice(colour_palette))
            kurmo.penup()
            kurmo.forward(50)

draw_spots(10)

screen.exitonclick()

