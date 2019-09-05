import math


def mysqrt(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y


def diff(a):
    return math.fabs(mysqrt(a) - math.sqrt(a))


if __name__ == "__main__":
    for a in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]:
        print("%f  %f  %f  %f" % (a, mysqrt(a), math.sqrt(a), diff(a)))
