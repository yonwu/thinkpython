def if_double_word(w):
    i = 0
    while i < len(w) - 1:
        if w[i] == w[i + 1]:
            return True
        else:
            i = i + 1
            continue
    return False


def three_double(w):
    i = 0
    num = 0
    while i < len(w) - 1:
        if w[i] == w[i + 1]:
            num = num + 1
            if num == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2 * num
            num = 0
    return False


def three_double_word(f):
    list_uses_all = []
    for line in f:
        word = line.strip()
        if three_double(word):
            list_uses_all.append(word)
    return list_uses_all


if __name__ == "__main__":
    fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')
    result = three_double_word(fin)
    print(result)

