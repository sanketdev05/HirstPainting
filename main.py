import turtle as t
import random
# import colorgram
#
# rgb_color = []
# colors = colorgram.extract('hirst_image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

color_list = [
    (229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227),
    (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
    (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
    (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
    (46, 73, 62), (47, 66, 82)
]

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setposition(-200, -250)
# print(tim.position())


def draw_hirst():
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)

y = -200
for _ in range(10):
    draw_hirst()
    tim.sety(y)
    tim.setx(-200)
    y += 50

# print("after execution")
# print(tim.position())

screen.exitonclick()