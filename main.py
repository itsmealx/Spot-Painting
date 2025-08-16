import random
import turtle
from colors import get_colors

turtle.colormode(255) #setting the color mode to 255 to support rgb, if not; will throw and error
screen = turtle.Screen()
squirtle = turtle.Turtle()
squirtle.speed("fastest") #speed of animation
squirtle.hideturtle() #hiding the turtle indicator

colors = get_colors() #get colors from the colors.py

#move to starting position
squirtle.penup()
squirtle.setheading(225)
squirtle.forward(320)
squirtle.setheading(0)

for distance in range(1, 101): # setting the size 10x10
    squirtle.dot(20, random.choice(colors))
    squirtle.forward(50)

    if distance % 10 == 0:
        squirtle.setheading(90)
        squirtle.forward(50)
        squirtle.setheading(180)
        squirtle.forward(500)
        squirtle.setheading(0)

screen.exitonclick()