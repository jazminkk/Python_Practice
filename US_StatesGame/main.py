import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = Turtle()
state_name.penup()
state_name.hideturtle()

data = pd.read_csv("./50_states.csv")
states_list = data["state"].str.lower().to_list()

count = 0
states_correct = []
while count <= 50:
    if count == 0:
        answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()
    else:
        answer = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?").lower()
    if answer == "exit":
        break
    if answer in states_list:
        count += 1
        state_data = data[data["state"].str.lower() == answer]
        state_name.setpos(int(state_data['x'].values[0]), int(state_data['y'].values[0]))
        name = state_data['state'].values[0]
        state_name.write(name, move=False, align='left', font=('Arial', 8, 'normal'))
        states_correct.append(name.lower())

learn_list = [state.title() for state in states_list if state not in states_correct]
missing_states = pd.DataFrame(learn_list, columns=["missing states"])
missing_states.to_csv("states_to_learn.csv")

