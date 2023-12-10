import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day25/us-states-game/blank_states_img.gif"
screen .addshape(image)
turtle.shape(image)

us_data = pandas.read_csv("Day25/us-states-game/50_states.csv")
states_list = us_data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed = []
        for state in states_list:
            if state not in guessed_states:
                not_guessed.append(state)
        learn = pandas.DataFrame(not_guessed)
        learn.to_csv("Day25/us-states-game/states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = us_data[us_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)