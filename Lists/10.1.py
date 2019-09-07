def nested_sum(l):
    result = 0
    for c in l:
        result = result + sum(c)
    return result


if __name__ == "__main__":
    print(nested_sum([[1, 2], [3], [4, 5, 6]]))
