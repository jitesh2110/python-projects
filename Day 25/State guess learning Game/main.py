from turtle import Screen,Turtle
import pandas
from pen import Pen


screen = Screen()
screen.addshape("blank_states_img.gif")
screen.title("Guess the state")
screen.setup(725,491)
screen.tracer(0)

rock = Turtle()
rock.shape('blank_states_img.gif')

pen = Pen()

correct_guess = []
count = 0
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

print(states)
while count <51:
    screen.update()
    guess = screen.textinput(title=f"{count}/50 Type 'Exit' to end game! ",prompt="Name of the state:").title()
    if guess == 'Exit':
        break
    if guess in states and guess not in correct_guess:
        correct_guess.append(guess)
        count += 1
        pen.update(guess)

states_to_learn =['state']
for state in states:
    if state not in correct_guess:
        states_to_learn.append(state)
file = pandas.DataFrame(states_to_learn)
file.to_csv("States_to_Learn")
