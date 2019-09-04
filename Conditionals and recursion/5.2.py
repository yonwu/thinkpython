import math


def check_fermat(a, b, c, n):
    """

    :type n: integer
    """
    if pow(a, n) + pow(b, n) == pow(c, n):
        print("fermat was wrong")
    else:
        print("no, that doesn't work")


if __name__ == "__main__":
    a = input("please give a value to a ")
    b = input("please give a value to b ")
    c = input("please give a value to c ")
    d = input("please give a value to d ")
    check_fermat(int(a), int(b), int(c), int(d))
