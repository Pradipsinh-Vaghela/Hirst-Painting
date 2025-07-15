from turtle import Turtle, Screen, colormode
import random
# import colorgram

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
print(tim)

# rgb_colors = []
# colors = colorgram.extract('Image_1.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b,)
#     rgb_colors.append(new_color)

rgb_colors = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45),
              (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91),
              (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]

y_axes = -250
for _ in range(10):
    tim.penup()
    tim.setx(-250)
    tim.sety(y_axes)
    for _ in range(10):
        color = random.choice(rgb_colors)
        tim.dot(20, color)
        tim.forward(50)
    y_axes += 50



screen = Screen()
screen.exitonclick()
