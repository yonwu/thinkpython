def is_palindrome(s, start, end):
    if len(str(s)) <= 1:
        return True
    elif len(str(s)) > 2:
        s = str(s)[start:end]
        if s == s[::-1]:
            return True
        return False


if __name__=="__main__":
    result =[]
    for s in range(100000, 999999):
        if is_palindrome(s, 2,6) and is_palindrome(s+1, 1, 6) and is_palindrome(s+2, 1, 5) and is_palindrome(s+3, 0, 6):
            result.append(s)
    print(result)
