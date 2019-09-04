fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')


def avoids(word, s):
    if word.find(s) == -1:
        return True

