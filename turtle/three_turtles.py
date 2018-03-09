# fundamentals: lesson 9-11

import turtle

def draw_square(t):    
    for x in range(0, 4):
        t.right(90)
        t.forward(100)

def draw_circle(t):
    t.circle(100)

def draw_triangle(t):
    for x in range(0, 3):
        t.right(120)
        t.forward(100)


window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("white")

angie = turtle.Turtle()
angie.shape("circle")
angie.color("red")

penny = turtle.Turtle()
penny.shape("triangle")
penny.color("blue")

draw_square(brad)
draw_circle(angie)
draw_triangle(penny)

window.exitonclick()
