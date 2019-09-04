import turtle
import math


def arc(t, r, angle):
    pi = math.pi
    circumference = 2 * pi * r
    side = 20
    polygon(t, circumference / side, side, angle)


def polygon(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle / n)
    turtle.mainloop()


bob = turtle.Turtle()

arc(bob, 100, 180)
