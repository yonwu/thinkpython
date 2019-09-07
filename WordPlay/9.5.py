import string

ALPHABET = list(string.ascii_lowercase)

fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def uses_all(w, l):
    for c in l:
        if c not in w:
            return False
            break
        else:
            continue
    return True


def word_uses_all(f, l):
    list_uses_all = []
    for line in f:
        word = line.strip()
        if uses_all(word, l):
            list_uses_all.append(word)
    return list_uses_all


if __name__ == "__main__":
    result = word_uses_all(fin, "aeiouy")
    print(result)
