import turtle


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()


bob = turtle.Turtle()

polygon(bob, 100, 6)
