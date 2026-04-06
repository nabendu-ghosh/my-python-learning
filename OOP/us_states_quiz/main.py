import turtle
import pandas

screen = turtle.Screen()
image = "OOP/us_states_quiz/blank_states_img.gif"
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

user_input = screen.textinput("Guess the state", "Enter state name")
states_data = pandas.read_csv("OOP/us_states_quiz/50_states.csv")

while True:
    print(states_data[states_data.state == user_input.title()])
    user_input = screen.textinput("Guess the state", "Enter state name")

screen.exitonclick()