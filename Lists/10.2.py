def cumsum(l):
    result = []
    e = 0
    for c in l:
        e = e + c
        result.append(e)
    return result


if __name__ == "__main__":
    print(cumsum([1, 2, 3]))
