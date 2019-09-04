def print_grid():
    print_plus_and_minus()
    do_four(print_dash)
    print_plus_and_minus()
    do_four(print_dash)
    print_plus_and_minus()


def print_plus_and_minus():
    print('+', '-' * 4, '+', '-' * 4, '+')


def do_four(f):
    f()
    f()
    f()
    f()


def print_dash():
    print('|', ' ' * 4, '|', ' ' * 4, '+')


print_grid()