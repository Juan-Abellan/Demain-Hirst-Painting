# TODO. IMPORTS
import turtle

import colorgram
from turtle import Turtle, Screen, dot
from random import randint, choice


# TODO. FUNCTIONS
def extract_colors(picture_name, num_colors):
    """
    Function extracting the color from the selected image.
    :return: tuple (r, g, b)
    """
    color_list = []
    colors = colorgram.extract(picture_name, num_colors)
    for index in range(len(colors)):
        color_list.append((colors[index].rgb[0], colors[index].rgb[1], colors[index].rgb[2]))
    return color_list


# print(extract_colors(picture_name="image.jpg", num_colors=30))
# TODO. STARTING CONDITIONS
turtle.colormode(255)

extracted_colors = [(131, 165, 204), (220, 149, 109), (30, 41, 62), (200, 134, 146), (166, 58, 48), (141, 184, 162),
                    (41, 104, 153), (236, 213, 95), (149, 60, 67), (215, 82, 72), (235, 165, 157), (52, 112, 91),
                    (33, 60, 55), (171, 29, 32), (156, 33, 30), (52, 44, 49), (229, 162, 166), (170, 188, 220),
                    (17, 96, 71), (57, 51, 48), (30, 60, 110), (182, 103, 113), (108, 126, 158), (175, 200, 188),
                    (34, 150, 210), (65, 66, 57)]

dot_num = 100

# TODO. SETTING THE TURTlE A.K.A. t

t = Turtle()
s = Screen()

s.bgcolor((246, 244, 243))
t.color()

t.speed(10)
t.hideturtle()
t.setheading(225)
t.penup()
t.fd(320)
t.setheading(0)

for dot in range(1, dot_num + 1):
    t.dot(20, choice(extracted_colors))
    t.penup()
    t.fd(50)
    if dot % 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)

s.exitonclick()
