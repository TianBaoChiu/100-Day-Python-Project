import random
import os
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
print(logo)

#創建遊戲狀態
keep_going = True
#讓用戶輸入一個字母，檢查該字母有沒有在被挑出來的單字當中
while keep_going:
  live = len(stages)
  end_of_game = False
  #從單字列表中隨機選擇一個單字
  word = random.choice(word_list)
  print(word)

  #創建一個"_"的列表
  empty_list = []
  for i in range(len(word)):
      empty_list.append("_")
  print(empty_list)
  while not end_of_game:
      user_input = input("Please type a letter: ").lower()

      os.system('cls')

      if user_input in empty_list:
        print("You have already guess this word!")

      for i in range(len(word)):
          if word[i] == user_input:
              empty_list[i] = user_input

      if not '_' in empty_list:
          print("You win!\n")
          end_of_game = True
      print("\n")
      print(empty_list)

      if user_input not in word:
          live -= 1
          print(stages[live])
          print(f"You only have {live} lives\n")
      
      if live == 0:
          print("You loss!\n")
          end_of_game = True
  state = input("Try again? Y/N").lower()
  if state == 'n':
    keep_going = False