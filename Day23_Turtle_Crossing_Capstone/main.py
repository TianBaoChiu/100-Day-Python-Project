import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
score = Scoreboard()

player = Player()
screen.onkey(player.move, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(score.level)
    screen.update()

    car.create_car()
    car.move()

    # 檢查烏龜和車體的碰撞
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()

    # 檢查烏龜是否到達對面
    if player.ycor() > 280:
        player.go_to_start()
        score.increase_level()


screen.exitonclick()
