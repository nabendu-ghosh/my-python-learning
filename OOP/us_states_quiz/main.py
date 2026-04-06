import turtle
import pandas

screen = turtle.Screen()
image = "OOP/us_states_quiz/blank_states_img.gif"
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("OOP/us_states_quiz/50_states.csv")
states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 states correctly guessed", prompt="Enter state name").title()
    
    if user_input == "Exit":
        break

    elif user_input in states and user_input not in guessed_states:
        state_data = states_data[states_data.state == user_input]
        kurmo = turtle.Turtle()
        kurmo.ht()
        kurmo.penup()
        kurmo.goto(state_data.x.item(),state_data.y.item())
        kurmo.write(user_input)
        guessed_states.append(user_input)

if len(guessed_states) < 50:
    print("Generating csv file with the states to learn")

    missing_states = [state for state in states if state not in guessed_states]
    new_df = pandas.DataFrame(missing_states)
    new_df.to_csv("OOP/us_states_quiz/states_to_learn.csv")