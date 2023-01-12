import random
import os
from art import logo, vs
from data import data


def random_pick_people(person_data):
    """
    從傳入的列表中隨機抽取出一名人物的資料

    Args:
        person_data (list) : 包含各種人物資訊的列表

    Return:
        person_data (list) :抽取出一名人物資訊後的列表
        A_people (dic) : 第一號人物的資料 key包含:name、follower_count、description、country
    """
    people = person_data.pop(random.randint(0, len(person_data)-1))

    return person_data, people


def get_follower_from_people(people):
    """
    取得該名人物當下的追蹤數

    Args:
        people (dic) :人物的資料 key包含:name、follower_count、description、country

    Return:
        people_follower (int) : 人物的追蹤數
    """
    people_follower = people['follower_count']

    return people_follower


def compare_follower(A_people_follower, B_people_follower):
    """
    比較兩者的分數高低

    Args:
        A_people_follower (int) : A人物的追蹤人數
        B_people_follower (int) : B人物的追蹤人數

    Return:
        "A" (str) : 代表A人物的追蹤數較高
        "B" (str) : 代表B人物的追蹤數較高
    """
    if A_people_follower > B_people_follower:
        return "A"
    else:
        return "B"


def pre_winner(higher_people, A_people, B_people):
    """
    根據比較結果，將當前獲勝者儲存下來

    Args:
        higher_people (str) : 顯示誰是勝者
        A_people (dic) : A人物的資料
        B_people (dic) : B人物的資料

    Return:
        A_people (dic) : A人物的資料
        B_people (dic) : B人物的資料
    """
    if higher_people == 'A':
        return A_people
    else:
        return B_people


def main():

    person_data = data
    # 抽選出兩名人物
    person_data, A_people = random_pick_people(person_data)
    person_data, B_people = random_pick_people(person_data)

    # 找出兩名人物的追蹤人數，先給予一個狀態
    A_people_follower = get_follower_from_people(A_people)
    B_people_follower = get_follower_from_people(B_people)
    print(f"A有{A_people_follower}人追蹤")
    print(f"B有{B_people_follower}人追蹤")
    higher_people = compare_follower(A_people_follower, B_people_follower)
    winner = pre_winner(higher_people, A_people, B_people)

    # 主要流程
    print(logo)
    print(
        f"Compare A: {A_people['name']}, {A_people['description']}, from {A_people['country']}.")
    print(vs)
    print(
        f"Against B: {B_people['name']}, {B_people['description']}, from {B_people['country']}.")

    Game = True
    score = 0
    while Game == True:
        player_input = input(
            "Who has more followers? Type 'A' or 'B' : ").upper()
        if player_input == higher_people:
            score += 1
            os.system('cls')
            print(logo)
            print(f"You are Right! Current score = {score}")
            Game = True
        else:
            os.system('cls')
            print(logo)
            print(f"You loss! Final score = {score}")
            Game = False
            break
        A_people = winner
        person_data, B_people = random_pick_people(person_data)
        A_people_follower = get_follower_from_people(A_people)
        B_people_follower = get_follower_from_people(B_people)
        higher_people = compare_follower(A_people_follower, B_people_follower)
        winner = pre_winner(higher_people, A_people, B_people)

        print(
            f"Compare A: {A_people['name']}, {A_people['description']}, from {A_people['country']}.")
        print(vs)
        print(
            f"Against B: {B_people['name']}, {B_people['description']}, from {B_people['country']}.")


main()
