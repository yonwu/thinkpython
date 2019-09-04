import turtle
import math


def circle(t, r):
    pi = math.pi
    circumference = 2 * pi * r
    polygon(t, circumference / 10, 10)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()


bob = turtle.Turtle()

circle(bob, 100)
