# fundamentals: lesson 6.14

import turtle

def draw_mandala(t):
    brad.color("#2E7D32")
    t.begin_fill()
    for x in range(0, 6):
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.left(60)
    t.end_fill()
    t.left(150)
    brad.color("#F4511E")
    t.fill(True)
    t.circle(100)
    t.fill(False)
    t.left(60)
    brad.color("#C2185B")
    for x in range(0, 6):
        t.fill(True)
        t.circle(50)
        t.fill(False)
        t.right(30)
        t.forward(100)
        t.left(90)
    t.right(45)

window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.speed(5)

draw_mandala(brad)

window.exitonclick()