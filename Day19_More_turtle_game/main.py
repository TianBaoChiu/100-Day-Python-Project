from turtle import Turtle, Screen
import random


colors = ['red', 'yellow', 'green', 'blue', 'black', 'purple']
game_on = False

screen = Screen()
screen.setup(width=500, height=400)
player_input = screen.textinput(
    title='Make your bet!', prompt='Which turtle will win a race? Enter a color...')

y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if player_input:
    game_on = True

while game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winner_color = turtle.pencolor()
            if winner_color == player_input:
                print(f"You win the game, the {winner_color} turtle is winner")
            else:
                print(
                    f"You loss the game, the {winner_color} turtle is winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
