from turtle import Turtle


class Paddle():

    def __init__(self, position):
        self.create_paddle()
        self.move(position)

    def create_paddle(self):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()

    def move(self, position):
        self.paddle.goto(position[0], position[1])

    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def pos(self):
        return self.paddle.pos()
