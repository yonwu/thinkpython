fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')
fin2 = open('/Users/yonwu/thinkpython/WordPlay/words.txt')
total = len(fin2.readlines())


def has_no_e(w):
    return w.count('e') == 0


def word_has_no_e(f):
    list_of_no_e = []
    n = 0
    for line in f:
        word = line.strip()
        if has_no_e(word):
            list_of_no_e.append(word)
            n = n + 1
    return [list_of_no_e, n / total]


if __name__ == "__main__":
    result = word_has_no_e(fin)
    print(result[1])
    print(result[0])

