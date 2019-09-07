def is_sorted(l):
    if sorted(l) == l:
        return True
    return False


if __name__ == "__main__":
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))
