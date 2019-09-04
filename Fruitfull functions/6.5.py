def gcd(a, b):
    if a == 0 and b == 0:
        return None
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    result = gcd(2, 20)
    print(result)
