fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def is_abecedarian(w):
    return sorted(list(w)) == list(w)


def word_is_abecedarian(f):
    list_uses_all = []
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            list_uses_all.append(word)
    return list_uses_all


if __name__ == "__main__":
    result = word_is_abecedarian(fin)
    print(result)
