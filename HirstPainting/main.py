import colorgram
import turtle
from turtle import Turtle, Screen
import random

rgb_color_list = []
turtle.colormode(255)


def choose_image():
    colors = colorgram.extract("image_1.jpg", 30)
    # print(colors)

    for item in colors:
        r = item.rgb.r
        g = item.rgb.g
        b = item.rgb.b
        if r < 250 and g < 250 and b < 250:
            rgb_color = (r, g, b)
            rgb_color_list.append(rgb_color)


# rgb_color_list = [(219, 154, 94), (224, 164, 9), (227, 239, 232), (14, 123, 168), (235, 209, 96), (195, 86, 19), (16, 196, 111), (219, 4, 62), (1, 176, 222), (218, 68, 111), (147, 65, 108), (119, 170, 202), (212, 127, 159), (27, 137, 84), (238, 74, 40), (129, 190, 144), (246, 207, 1), (131, 225, 181), (4, 107, 68), (244, 158, 191), (225, 1, 1), (105, 110, 183), (242, 168, 155), (28, 51, 75), (38, 53, 112), (143, 218, 226), (16, 67, 46)]


def print_hirst_painting(number_of_dot):
    turtle_a = Turtle()
    turtle_a.penup()
    turtle_a.hideturtle()
    dot_gap = int(screen.window_width() / (number_of_dot + 2))
    height = int(screen.window_height() / 2) - dot_gap
    width = int(screen.window_width() / 2) - dot_gap
    for j in range(-height, height, dot_gap):
        for i in range(-width, width, dot_gap):
            turtle_a.setpos(i, j)
            dot_color = random.choice(rgb_color_list)
            turtle_a.color(dot_color)
            turtle_a.dot(size=20)
            turtle_a.penup()


screen = Screen()
screen.screensize(500, 500)
choose_image()
print_hirst_painting(number_of_dot=10)
screen.exitonclick()
