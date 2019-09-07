def has_duplicates(l):
    c = 0
    while c < len(l) - 1:
        if l[c] == l[c + 1]:
            return True
        else:
            c = c + 1
            continue
    return False


if __name__=="__main__":
    print(has_duplicates("wcbc"))
    print(has_duplicates("wbc"))