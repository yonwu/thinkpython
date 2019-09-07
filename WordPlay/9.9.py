def equal_if_reverse(m, n):
    return str(m).zfill(2)[::-1] == str(n).zfill(2)


def find_gap_age(gap, count):
    n = 0
    my_age = []
    mum_age = []
    age = {}
    flag = False
    for m in range(120):
        if equal_if_reverse(m, m + gap):
            n = n + 1
            my_age.append(m)
            mum_age.append(m + gap)
            if n == count:
                age[gap] = [my_age, mum_age]
                flag = True
    if flag:
        return age
    else:
        return False


if __name__ == "__main__":
    for i in range(15, 50):
        result = find_gap_age(i, 8)
        if result:
            print(i)
            print(result.get(i)[0])
            print(result.get(i)[1])
