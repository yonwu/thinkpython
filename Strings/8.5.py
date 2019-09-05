def rotate_word(s, n):
    new_s = []
    for c in s:
        c = ord(c) + n
        new_s.append(chr(c))
    return new_s


if __name__ == "__main__":
    print(rotate_word("abc", 2))
