fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def more_than_twenty(f):
    list_of_bigword = []
    for line in f:
        word = line.strip()
        if len(word)>20:
            list_of_bigword.append(word)
    return list_of_bigword


if __name__ == "__main__":
    print(more_than_twenty(fin))
