from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_ANGLE = 90


class Snake:

    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        self.new_snake = Turtle(shape="square")
        self.new_snake.color("white")
        self.new_snake.penup()
        self.new_snake.goto(position)
        self.my_snake.append(self.new_snake)

    def extend(self):
        self.add_snake(self.my_snake[-1].position())

    def move(self):
        for self.snake_num in range(len(self.my_snake)-1, 0, -1):
            self.new_x = self.my_snake[self.snake_num-1].xcor()
            self.new_y = self.my_snake[self.snake_num-1].ycor()
            self.my_snake[self.snake_num].goto(self.new_x, self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for snake in self.my_snake:
            snake.goto(1000, 1000)
        self.my_snake.clear()
        self.create_snake()
        self.head = self.my_snake[0]
