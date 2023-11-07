# import turtle

# timmy_the_turtle = turtle.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("orchid")

#Drawing a square
#Option 1
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#Option 2
# while True:
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     if abs(timmy_the_turtle.pos()) < 1:
#         break

#Drawing a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#Drawing different shapes
# import random
# steps = [3, 4, 5, 6, 7, 8, 9, 10]
# colors = ["red", "blue", "green", "yellow", "pink", "purple", "orchid", "black", "SlateGray", "SeaGreen"]
# for shape in steps:
#     timmy_the_turtle.pencolor(random.choice(colors))
#     for _ in range(0, shape):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/shape)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#Random walk
#import random
#colors = ["red", "blue", "green", "yellow", "pink", "purple", "orchid", "black", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed(10)
# for _ in range(100):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(50)

#Make a spirograph
tim.speed(15)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()