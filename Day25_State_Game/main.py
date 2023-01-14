import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

image_path = "Day25_State_Game/blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)


answer_state = screen.textinput(
    title="Guess the state", prompt="What's the state's name?").title()
game_on = True
df = pd.read_csv("Day25_State_Game/50_states.csv")
df_state_list = df['state'].to_list()
correct_list = []
if (answer_state in df_state_list):
    if answer_state not in correct_list:
        state_loc = df[df['state'] == answer_state]
        pen.goto(int(state_loc['x']), int(state_loc['y']))
        pen.write(answer_state, align='center')
        df_state_list.remove(answer_state)
        correct_list.append(answer_state)
    else:
        print("You've already guess the sate")
elif answer_state == 'Stop':
    print("Stop the game")
    game_on = False
elif len(correct_list) == 50:
    game_on = False
else:
    print("Guess the state...")

while game_on:
    answer_state = screen.textinput(
        title=f"{len(correct_list)}/50 States Correct", prompt="What's the state's name?").title()
    if (answer_state in df_state_list):
        if answer_state not in correct_list:
            state_loc = df[df['state'] == answer_state]
            pen.goto(int(state_loc['x']), int(state_loc['y']))
            pen.write(answer_state, align='center')
            df_state_list.remove(answer_state)
            correct_list.append(answer_state)
        else:
            print("You've already guess the sate")
    elif answer_state == 'Stop':
        print("Stop the game")
        states_to_learn = pd.DataFrame(df_state_list)
        states_to_learn.to_csv('Day25_State_Game/states_to_learn.csv')
        game_on = False
    elif len(correct_list) == 50:
        print("You finished the game!!! Great job")
        game_on = False
    else:
        print("Guess the state...")


screen.exitonclick()


# 取得圖片上的座標
# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
