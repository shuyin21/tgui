import turtle as t
import random
tim = t.Turtle()
t.colormode(255)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rd_color = (r, g, b)
    return rd_color


turtle_movement = [90, 180, 270, 0]

colors = ['red', 'lawn green', 'steel blue', 'deep pink', 'purple', 'lavender']
counter = 3
angle = 360 / counter
tim.pensize(1)
# tim.hideturtle()
tim.speed('fastest')
# for x in range(8):
#     for side in range(counter):
#         tim.right(angle)
#         tim.forward(100)
#     counter = counter + 1
#     angle = 360 / counter
#     tim.color(random.choice(colors))


#random movement


# for x in range(300):
#     tim.setheading(random.choice(turtle_movement))
#     tim.forward(30)
#
#     tim.color(random_color())
#

def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)



















screen = t.Screen()


screen.exitonclick()