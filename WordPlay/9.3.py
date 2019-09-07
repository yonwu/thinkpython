import string

ALPHABET = list(string.ascii_lowercase)

fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def avoids(w, l):
    for c in l:
        if w.count(c) != 0:
            return False
            break
        else:
            continue
    return True


def words_avoids(f, l):
    n = 0
    for line in f:
        word = line.strip()
        if avoids(word, l):
            n = n + 1
    return n


def rank_of_forbidden():
    rank = {}
    for c in ALPHABET:
        fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')
        result = words_avoids(fin, c)
        rank[c] = result
    result = sorted(rank, key=rank.get, reverse=True)
    return result[:5]


if __name__ == "__main__":
    result = rank_of_forbidden()
    print(result)
