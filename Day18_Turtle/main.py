from turtle import Turtle, Screen
import random
import turtle


colors = [(232, 234, 237), (234, 232, 228), (235, 230, 233), (224, 234, 229), (48, 95, 145), (175, 49, 77), (205, 158, 92), (225, 208, 103), (135, 88, 64), (118, 177, 205), (177, 167, 38), (197, 77, 122), (210, 132, 172), (224, 72, 53), (94, 105,
                                                                                                                                                                                                                                              187), (31, 141, 89), (57, 164, 117), (127, 217, 206), (52, 55, 90), (123, 42, 70), (117, 48, 38), (226, 171, 188), (30, 181, 189), (128, 185, 162), (156, 207, 216), (231, 173, 166), (176, 186, 218), (51, 52, 70), (81, 47, 37), (43, 76, 78)]

tim = Turtle()
turtle.colormode(255)
tim.shape('turtle')
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# for i in range(3, 20):
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360 / i)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# def random_walk():
#     tim.color(random_color())
#     angles = [90, 180, 270, 360]
#     tim.right(random.choice(angles))
#     tim.forward(50)
#     tim.speed(10)


# width = 1
# for _ in range(50):

#     tim.width(width)
#     random_walk()
#     width += 0.1
# def draw_circle(degree):
#     times = int(360 / degree)
#     for _ in range(times):
#         tim.color(random_color())
#         tim.pensize(2)
#         tim.speed('fastest')
#         tim.circle(80)
#         tim.right(degree)


# draw_circle(10)

def random_color():
    color = random.choice(colors)
    return (color)


def draw_dot():
    for _ in range(10):
        tim.color(random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(40)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(40)
    tim.left(90)
    tim.forward(400)
    tim.right(180)


tim.hideturtle()
for i in range(10):
    tim.speed(0)
    draw_dot()

screen = Screen()
screen.exitonclick()  # 直到畫面被點擊才會消失
