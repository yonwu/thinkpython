import turtle

bob = turtle.Turtle()


def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    angle = 60
    koch(t, length/3)
    t.lt(angle)
    koch(t, length/3)
    t.rt(2 * angle)
    koch(t, length/3)
    t.lt(angle)
    koch(t, length/3)

def snowflake(t, length):
    for i in range(3):
        koch(t,length)
        t.rt(120)


if __name__ == "__main__":
    snowflake(bob, 90)
    turtle.mainloop()
