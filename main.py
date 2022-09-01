from turtle import Turtle, Screen
import random
import turtle

timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.shape("turtle")
timmy.color("blue")
#timmy.speed()
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 30):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)



#directions = [0,90,180,270]

#timmy.pensize(15)
timmy.speed("fastest")

def draw_spirographs(size_of_gap):

    for i in range(int(360/size_of_gap)):

            timmy.color(random_color())
            timmy.circle(100)
            timmy.setheading(timmy.heading() + size_of_gap)


draw_spirographs(0.36)

# for i in range(200):
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     timmy.color(random_color())


screen = Screen()
screen.exitonclick()


