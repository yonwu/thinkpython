import string

ALPHABET = list(string.ascii_lowercase)

fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def uses_only(w, l):
    for c in w:
        if c not in l:
            return False
            break
        else:
            continue
    return True


def word_uses_only(f, l):
    list_uses_only = []
    for line in f:
        word = line.strip()
        if uses_only(word, l):
            list_uses_only.append(word)
    return list_uses_only


if __name__ == "__main__":
    result = word_uses_only(fin, "acefhlo")
    print(result)
