# fundamentals: lesson 13

import turtle

def draw_square_circle(t):
    for x in range(0, 24):
        draw_square(t)
        t.right(15)


def draw_square(t):    
    for x in range(0, 4):
        t.right(90)
        t.forward(100)


window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("white")
brad.speed(7)

draw_square_circle(brad)

window.exitonclick()