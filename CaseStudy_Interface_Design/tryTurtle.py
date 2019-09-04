import turtle
bob = turtle.Turtle()
def draw(t, length, n):
    if n == 0:
        return
    angle = 60
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

if __name__=="__main__":
    draw(bob, 10, 4)
    turtle.mainloop()