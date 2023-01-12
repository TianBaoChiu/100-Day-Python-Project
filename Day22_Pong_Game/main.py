from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # 關閉螢幕追蹤器


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')


screen.update()
game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 檢查牆壁的碰撞
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 檢查球和平板的碰撞
    if ball.xcor() > 320 and ball.distance(right_paddle.pos()) < 50 or ball.xcor() < -320 and ball.distance(left_paddle.pos()) < 50:
        ball.bounce_x()

    # 當球沒被平板接到
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
