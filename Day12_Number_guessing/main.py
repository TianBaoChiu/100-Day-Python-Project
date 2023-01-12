import random
import os
from logo import logo


def number_gen():
    """
    隨機產生一個1到100之間的數字

    Args: 
        無

    return:
        target (int) :一個隨機的整數 介於1到100之間
    """
    target = random.randint(1, 100)
    return target


start_game = True
while start_game:
    os.system('cls')
    print(logo)
    start_game_input = input(
        "Welcome to the guessing number game !!!  Type 'y' to start or type 'n' to quit. :").lower()
    if start_game_input == 'n':
        start_game = False
        break

    level_input = input("easy of hard? : ").lower()
    if level_input == 'easy':
        life = 10
    elif level_input == 'hard':
        life = 5
    else:
        print("Wrong input!!!")
        start_game = False
        break

    target = number_gen()
    print(target)
    alive = True
    keep_game = True
    while alive and keep_game:
        user_input = int(input("Input a number: "))
        if user_input > target:
            print("Too High!")
            life -= 1
            print(f"You have {life} life")
        elif user_input < target:
            print("Too Low!")
            life -= 1
            print(f"You have {life} life")
        else:
            print("Correct number!!!")
            keep_game = False

        if life == 0:
            print("You loss")
            alive = False
    start_game_input = input("Tru again? 'y' or 'n'").lower()
    if start_game_input == 'n':
        start_game = False
