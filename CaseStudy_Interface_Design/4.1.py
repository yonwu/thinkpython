import turtle


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()


bob = turtle.Turtle()

square(bob)
