import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

data = [rock, paper, scissors]

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(data[player_choose])

pc_choose = random.randint(0, len(data)-1)
print("Computer chose:\n")
print(data[pc_choose])

if player_choose == 0:
    if pc_choose == 0 :
        print("tie!")
    elif pc_choose == 1 :
        print("You lose!")
    else :
        print("You win!")
elif player_choose == 1:
    if pc_choose == 0 :
        print("You lose!")
    elif pc_choose == 1 :
        print("tie!")
    else :
        print("You lose!")
else:
    if pc_choose == 0 :
        print("You lose!")
    elif pc_choose == 1 :
        print("You win!")
    else :
        print("tie!")