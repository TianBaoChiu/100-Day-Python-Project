import random
import os
from logo import logo


def take_a_card(cards):
    """
    從cards當中隨機抽取出一張卡牌

    Args:
        cards

    Yields:
        card (int) : 從cards當中隨機抽選出的卡牌
        cards (list) : 一個包含所有卡牌的列表 每次都被取之後卡牌數都會少1
    """
    pop_num = random.randint(0, len(cards)-1)  # 這邊注意
    card = cards.pop(pop_num)
    return card, cards


def sum_cards(current_value, cards):
    """
    將卡組當中的卡牌值相加

    Args:
        current_value (int) :當前的值
        cards (list) : 要相加的卡牌組合

    Return:
        current_value (int) : 相加過後的值 

    """
    for item in cards:
        current_value += item
    return current_value


def blackjack():
    """
    blackjack遊戲主要流程

    """
    # 遊戲開始
    player_cards = []
    pc_cards = []
    # 玩家部分
    for _ in range(2):
        card, cards = take_a_card(ori_cards)
        player_cards.append(card)

    player_current_value = sum_cards(0, player_cards)

    print(f"Your cards: {player_cards},current score: {player_current_value}")

    # 電腦部分
    for _ in range(2):
        card, cards = take_a_card(cards)
        pc_cards.append(card)

    pc_current_value = sum_cards(0, pc_cards)
    print(f"Computer's first card: {pc_cards[0]}")

    # 玩家補抽
    keep = True
    while keep:
        keep_input = input(
            "Type 'y' to get anther card, type 'n' to pass: ").lower()
        if keep_input == 'n':
            keep = False
            break
        # 繼續抽卡
        card, cards = take_a_card(cards)
        player_cards.append(card)
        player_current_value = sum_cards(0, player_cards)
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(f"Computer's first card: {pc_cards[0]}")
        if player_current_value > 21:
            keep = False

    # 電腦補抽
    keep = True
    while keep:
        if pc_current_value >= 17:
            keep = False
            break
        card, cards = take_a_card(cards)
        pc_cards.append(card)
        pc_current_value = sum_cards(0, pc_cards)

    # 比較 雙方爆>莊家爆>玩家爆>玩家贏>平手>莊家贏
    if player_current_value > 21 and pc_current_value > 21:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("Tie!!!")
    elif player_current_value <= 21 and pc_current_value > 21:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("pc loss!!!")
    elif player_current_value > 21 and pc_current_value <= 21:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("You went over. You loss")
    elif player_current_value > pc_current_value:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("You Win!!!")
    elif player_current_value == pc_current_value:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("Tie !!!")
    else:
        print(
            f"Your cards: {player_cards},current score: {player_current_value}")
        print(
            f"Computer's final hand: {pc_cards}, final score: {pc_current_value}")
        print("You loss!!!")
    game = True
    game_input = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    if game_input == "n":
        game = False
    return game


game = True
print(logo)
game_input = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
if game_input == "n":
    game = False
while game:
    os.system('cls')
    print(logo)

    # 定義一個卡夾，包含4種花色的卡，共4*13 = 52張
    print("Reset cards")
    ori_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
                 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game = blackjack()
