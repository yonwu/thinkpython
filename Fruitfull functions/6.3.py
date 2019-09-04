def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if len(s) == 2:
        return first(s) == last(s)
    elif len(s) > 2:
        if first(s) == last(s):
            return is_palindrome(middle(s))
        return False


if __name__ == "__main__":
    result = is_palindrome('emme')
    print(result)
