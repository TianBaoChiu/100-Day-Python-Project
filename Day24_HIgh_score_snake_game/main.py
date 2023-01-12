from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  # 關閉螢幕追蹤器


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

games_on = True

while games_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # 食物碰撞檢測
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()

    # 牆壁碰撞檢測
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # 尾巴碰撞檢測
    for snake_tail in snake.my_snake[1:]:
        if snake.head.distance(snake_tail) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
