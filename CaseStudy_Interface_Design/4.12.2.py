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



def flower(t, r, n):
    for i in range(n):
        leaf(t, r)
        t.lt(360/n)


def leaf(t, r):
    angle = 60
    arc(t, r, angle)
    t.lt(180- angle)
    arc(t, r, angle)
    t.lt(180- angle)


bob = turtle.Turtle()


flower(bob, 50, 7)

turtle.mainloop()
