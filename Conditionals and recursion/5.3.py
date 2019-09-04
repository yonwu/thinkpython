def is_triangle(a, b, c):
    d = sorted([a, b, c])
    print(d)
    if d[-1] > d[0] + d[1]:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    a = input("please give a value to a ")
    b = input("please give a value to b ")
    c = input("please give a value to c ")

    is_triangle(int(a), int(b), int(c))
