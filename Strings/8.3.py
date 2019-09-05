

def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif len(s) > 2:
        if s == s[::-1]:
            return True
        return False


if __name__ == "__main__":
    result = is_palindrome('emme')
    print(result)
