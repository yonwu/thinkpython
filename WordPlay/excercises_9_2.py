fin = open('/Users/yonwu/thinkpython/WordPlay/words.txt')



# exercises 9.1



def has_no_e(fin):
    list_no_e = []
    line_lenth = 0
    for line in fin:
        line_lenth = line_lenth + 1
        word = line.strip()
        if word.find('e') == -1:
            list_no_e.append(word)
            print(word)
    print(len(list_no_e)/line_lenth)


has_no_e(fin)
