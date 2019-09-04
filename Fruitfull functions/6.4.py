def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    return False


if __name__ == "__main__":
    result = is_power(8, 2)
    print(result)
