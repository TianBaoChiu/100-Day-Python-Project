import os
from Day11_The_Blackjack.logo import logo


def find_highest_bidder(play_value_db):
    '''找出出價者列表中最高價的出價者，並且打印出來

    Args:
        play_value_db (dic) : 一個包含出價者名稱和價格的字典，其對應關係為:{出價者:價格}
    
    Yields:
        無
    '''
    max_player = ''
    max_value = 0
    for key in play_value_db:
        if play_value_db[key] > max_value:
            max_player = key
            max_value = play_value_db[key]
    print(f"The winner is {max_player} with a bid of ${max_value}")

def log_the_player_and_value():
    '''用來記錄出價者和價格

    Args:
        無
    
    Yields:
        dic : 一個包含了出價者和價格的字典
    
    '''
    play_value_db = {}

    keep_auction = True
    while keep_auction:
        player = input("What is your name?")
        value = int(input("What's your bis?: $"))
        play_value_db[player] = value
        while True:
            keep_auction_input = input("Are there any other bidders? Type 'yes' or 'no'").lower()
            if keep_auction_input == 'yes':
                os.system('cls')
                break
            elif keep_auction_input == 'no':
                os.system('cls')
                keep_auction = False
                break
            else:
                print("Wrong input !")
    return play_value_db

print(logo)
print("Welcome to the secret auction program.")


play_value_db = log_the_player_and_value()
find_highest_bidder(play_value_db)