# fundamentals: lesson 6

import turtle
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(3)
    brad.shapesize(1.2,1.2)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    window.exitonclick()


draw_square()
