def chop(l):
    l.pop(0)
    l.pop(-1)
    return None


if __name__ == "__main__":
    t = [1, 2, 3, 4]
    chop(t)
    print(t)
