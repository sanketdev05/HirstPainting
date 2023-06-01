import turtle as t
import random

tim = t.Turtle()

# tim.shape("turtle")
# Timothy.color("red")

# draws a dashed line
# for _ in range(16):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
# tim.color("red")

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "wheat", "SlateGray", "SeaGreen"]


# draws shapes like triangle square hexagon etc.
# def shapes(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for side in range(3, 11):
#     colors = random.choice(colours)
#     tim.color(colors)
#     shapes(side)

# Draw random walk
# direction = [0, 90, 180, 270]
# t.colormode(255)
# tim.pensize(15)
# tim.speed(0)
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# Draw a spirograph
t.colormode(255)
tim.speed(0)

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
